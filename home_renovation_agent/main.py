"""
Main Entry Point for Home Renovation Agent.
Author: Danish (Dan-445)
"""
import streamlit as st
import asyncio
import os
from config import APP_TITLE, APP_ICON, GOOGLE_API_KEY, setup_logging

# Import the root agent from the refactored agent.py
# Note: This assumes `google-adk` is installed in the environment.
try:
    from agent import root_agent
    from google.adk.runtime import run_agent_turn 
    # Attempting to guess the runtime invocation. 
    # If standard run() exists on agent, we use that.
except ImportError:
    root_agent = None

# Initialize logging
setup_logging()

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")
    
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.caption("Plan your dream renovation with Gemini 2.5 Flash and ADK.")

    # Sidebar
    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("Google API Key", value=GOOGLE_API_KEY, type="password")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
            os.environ["GEMINI_API_KEY"] = api_key
        
        if not root_agent:
            st.error("⚠️ `google-adk` library not found or agent import failed. Please install requirements.")
            st.stop()
            
    # Session State for Chat
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display Chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "image" in msg:
                st.image(msg["image"])

    # Chat Input
    if prompt := st.chat_input("Describe your renovation idea..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Agent processing
        with st.chat_message("assistant"):
            with st.spinner("AI Planner is thinking..."):
                try:
                    # ADK Interaction Layer
                    # Assuming standard ADK run pattern. 
                    # If this is different, the user will need to adjust the invocation.
                    
                    # We create a simple context/session if needed, or just call run()
                    response = "I am ready to help, but the integration with the ADK runtime needs verification. Please ensure `RunOutput` is handled."
                    
                    if hasattr(root_agent, 'run'):
                         result = root_agent.run(prompt)
                         if hasattr(result, 'content'):
                             response = result.content
                         else:
                             response = str(result)
                    else:
                        response = "Error: Agent does not have a `run` method. Please check ADK documentation."
                    
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                except Exception as e:
                    st.error(f"Error running agent: {e}")

if __name__ == "__main__":
    main()
