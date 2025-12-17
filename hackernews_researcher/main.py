"""
Main Entry Point for HackerNews Researcher.
Author: Danish (Dan-445)
"""
import streamlit as st
import os

from config import OPENAI_API_KEY, APP_TITLE, APP_ICON, setup_logging
from hn_team import create_hackernews_team

# Initialize logging
setup_logging()

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")
    
    # Initialize session state for api key if not present
    if "api_key" not in st.session_state:
        st.session_state.api_key = OPENAI_API_KEY

    st.title(f"{APP_ICON} {APP_TITLE}")
    st.caption("Research top stories, users, and trends on HackerNews with a multi-agent team.")

    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        provider = st.radio(
            "Model Provider",
            ["OpenAI", "Ollama (Local)"],
            help="Choose between cloud-based OpenAI or local Llama models via Ollama."
        )
        
        # Determine internal provider string
        provider_code = "OpenAI" if provider == "OpenAI" else "Ollama"

        api_key_input = ""
        if provider_code == "OpenAI":
            api_key_input = st.text_input(
                "OpenAI API Key",
                value=st.session_state.api_key,
                type="password",
                help="Required for OpenAI models."
            )
            # Update state if changed
            if api_key_input != st.session_state.api_key:
                st.session_state.api_key = api_key_input
        else:
            st.info("Ensure Ollama is running locally (`ollama serve`).")
            st.info("Using default model: llama3.2")
    
    # Main Chat Interface
    query = st.text_input("Enter your research topic or query", placeholder="What are the top AI stories today?")

    if st.button("Start Research") and query:
        # Validation
        if provider_code == "OpenAI" and not st.session_state.api_key:
            st.warning("⚠️ Please provide an OpenAI API Key.")
            return

        try:
            with st.spinner(f"Agents are researching '{query}' using {provider}..."):
                # Create the team dynamically based on selection
                team = create_hackernews_team(
                    provider=provider_code,
                    api_key=st.session_state.api_key if provider_code == "OpenAI" else None
                )
                
                # Execute
                response = team.run(query, stream=False)
                
                # Display Result
                st.markdown("### 📝 Research Report")
                st.markdown(response.content)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
            if provider_code == "Ollama":
                 st.info("Troubleshooting: Make sure Ollama is installed and running. Try `ollama pull llama3.2` if model is missing.")

if __name__ == "__main__":
    main()
