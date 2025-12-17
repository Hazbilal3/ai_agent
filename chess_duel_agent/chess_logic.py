"""
Logic for AI Chess Agent.
Author: Danish (Dan-445)
"""
import chess
import chess.svg
from autogen import ConversableAgent, register_function

class ChessGameManager:
    def __init__(self):
        self.board = chess.Board()
        self.made_move = False
        self.move_history = []  # List of SVG strings
        
    def reset(self):
        self.board.reset()
        self.made_move = False
        self.move_history = []

    def get_board_svg(self):
        return chess.svg.board(self.board, size=300)

    def available_moves(self) -> str:
        """Get legal moves."""
        moves = [str(move) for move in self.board.legal_moves]
        return "Available moves are: " + ",".join(moves)

    def execute_move(self, move: str) -> str:
        """Make a move on the board."""
        try:
            chess_move = chess.Move.from_uci(move)
            if chess_move not in self.board.legal_moves:
                return f"Invalid move: {move}. Please call available_moves() to see valid moves."
            
            # Update board state
            self.board.push(chess_move)
            self.made_move = True

            # Generate visualization for history
            board_svg = chess.svg.board(
                self.board,
                arrows=[(chess_move.from_square, chess_move.to_square)],
                fill={chess_move.from_square: "gray"},
                size=400
            )
            self.move_history.append(board_svg)

            # Get piece information for description
            moved_piece = self.board.piece_at(chess_move.to_square)
            piece_unicode = moved_piece.unicode_symbol()
            piece_type_name = chess.piece_name(moved_piece.piece_type)
            piece_name = piece_type_name.capitalize() if piece_unicode.isupper() else piece_type_name
            
            # Description
            from_sq = chess.SQUARE_NAMES[chess_move.from_square]
            to_sq = chess.SQUARE_NAMES[chess_move.to_square]
            move_desc = f"Moved {piece_name} ({piece_unicode}) from {from_sq} to {to_sq}."

            # Game validations
            if self.board.is_checkmate():
                winner = 'White' if self.board.turn == chess.BLACK else 'Black'
                move_desc += f"\nCheckmate! {winner} wins!"
            elif self.board.is_stalemate():
                move_desc += "\nGame ended in stalemate!"
            elif self.board.is_insufficient_material():
                move_desc += "\nGame ended - insufficient material to checkmate!"
            elif self.board.is_check():
                move_desc += "\nCheck!"
    
            return move_desc

        except ValueError:
            return f"Invalid move format: {move}. Please use UCI format (e.g., 'e2e4')."

    def check_made_move(self, msg):
        if self.made_move:
            self.made_move = False
            return True
        else:
            return False

def setup_chess_agents(api_key: str, game_manager: ChessGameManager):
    """Sets up the White, Black, and Game Master agents."""
    
    config_list = [{"model": "gpt-4o-mini", "api_key": api_key}]

    agent_white = ConversableAgent(
        name="Agent_White",
        system_message="You are a professional chess player and you play as white. "
        "First call available_moves() first, to get list of legal available moves. "
        "Then call execute_move(move) to make a move.",
        llm_config={"config_list": config_list, "cache_seed": None},
    )

    agent_black = ConversableAgent(
        name="Agent_Black",
        system_message="You are a professional chess player and you play as black. "
        "First call available_moves() first, to get list of legal available moves. "
        "Then call execute_move(move) to make a move.",
        llm_config={"config_list": config_list, "cache_seed": None},
    )

    game_master = ConversableAgent(
        name="Game_Master",
        llm_config=False,
        is_termination_msg=game_manager.check_made_move,
        default_auto_reply="Please make a move.",
        human_input_mode="NEVER",
    )

    # Register tools
    # We register the methods of the specific game_manager instance
    for agent in [agent_white, agent_black]:
        register_function(
            game_manager.execute_move,
            caller=agent,
            executor=game_master,
            name="execute_move",
            description="Call this tool to make a move.",
        )
        register_function(
            game_manager.available_moves,
            caller=agent,
            executor=game_master,
            name="available_moves",
            description="Get legal moves.",
        )

    # Nested chats
    agent_white.register_nested_chats(
        trigger=agent_black,
        chat_queue=[{"sender": game_master, "recipient": agent_white, "summary_method": "last_msg"}],
    )

    agent_black.register_nested_chats(
        trigger=agent_white,
        chat_queue=[{"sender": game_master, "recipient": agent_black, "summary_method": "last_msg"}],
    )

    return agent_white, agent_black
