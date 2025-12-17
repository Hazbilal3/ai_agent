"""
Main Entry Point for AI Chess Agent.
Author: Danish (Dan-445)
"""
import streamlit as st
import chess.svg
from config import APP_TITLE, APP_ICON, OPENAI_API_KEY, setup_logging
from chess_logic import ChessGameManager, setup_chess_agents

# Initialize logging
setup_logging()

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)

    # Sidebar Config
    st.sidebar.title("Configuration")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password", value=OPENAI_API_KEY)
    
    st.sidebar.info("""
    **Note:**
    For a complete game (checkmate), max_turns > 200 is often needed.
    For this demo, we recommend 5-10 turns to save time/credits.
    """)
    
    max_turns = st.sidebar.number_input("Max Turns (per player)", min_value=1, max_value=100, value=5)

    st.title(f"{APP_ICON} {APP_TITLE}")

    # Session State for Game Manager
    if "game_manager" not in st.session_state:
        st.session_state.game_manager = ChessGameManager()

    gm = st.session_state.game_manager

    # Display Current Board
    st.subheader("Current Board")
    st.image(gm.get_board_svg())

    col1, col2 = st.columns(2)
    start_btn = col1.button("▶️ Start Game", type="primary", use_container_width=True)
    reset_btn = col2.button("🔄 Reset Board", use_container_width=True)

    if reset_btn:
        gm.reset()
        st.rerun()

    if start_btn:
        if not api_key:
            st.error("Please provide an OpenAI API Key.")
        else:
            gm.reset()
            st.info("🤖 Agents are initializing...")
            
            try:
                # Setup Agents
                white, black = setup_chess_agents(api_key, gm)
                
                # Start Chat
                st.write("Game started! White's turn.")
                with st.spinner("Agents are playing... Check terminal for live logs."):
                    chat_result = black.initiate_chat(
                        recipient=white, 
                        message="Let's play chess! You go first, its your move.",
                        max_turns=max_turns,
                        summary_method="reflection_with_llm"
                    )
                
                st.success("Game sequence completed!")
                st.markdown("### Game Summary")
                st.markdown(chat_result.summary)
                
                # Show History
                st.divider()
                st.subheader("📜 Move History")
                for i, move_svg in enumerate(gm.move_history):
                    move_by = "Agent White" if i % 2 == 0 else "Agent Black"
                    st.caption(f"Move {i + 1}: {move_by}")
                    st.image(move_svg, width=300)

            except Exception as e:
                st.error(f"Error during game: {e}")

if __name__ == "__main__":
    main()
