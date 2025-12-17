"""
Logic for Chat with PDF.
Author: Danish (Dan-445)
"""
from embedchain import App

def get_embedchain_app(db_path: str):
    """
    Creates an EmbedChain app using Llama 3.2 via Ollama.
    """
    return App.from_config(
        config={
            "llm": {
                "provider": "ollama",
                "config": {
                    "model": "llama3.2:latest",
                    "max_tokens": 250,
                    "temperature": 0.5,
                    "stream": True,
                    "base_url": 'http://localhost:11434'
                }
            },
            "vectordb": {
                "provider": "chroma",
                "config": {
                    "dir": db_path
                }
            },
            "embedder": {
                "provider": "ollama",
                "config": {
                    "model": "llama3.2:latest",
                    "base_url": 'http://localhost:11434'
                }
            },
        }
    )
