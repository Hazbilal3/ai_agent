"""
Main Entry Point for Chat with PDF.
Author: Danish (Dan-445)
"""
import os
import tempfile
import streamlit as st
import base64
from streamlit_chat import message
from config import APP_TITLE, APP_ICON, setup_logging
from logic import get_embedchain_app

# Initialize logging
setup_logging()

st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)

def display_pdf(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.caption("Chat with your PDF documents using local Llama 3.2 (via Ollama).")

    # Define the database path
    if "db_path" not in st.session_state:
        st.session_state.db_path = tempfile.mkdtemp()

    # Create a session state to store the app instance and chat history
    if 'app' not in st.session_state:
        st.session_state.app = get_embedchain_app(st.session_state.db_path)
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Sidebar for PDF upload and preview
    with st.sidebar:
        st.header("📄 PDF Upload")
        pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

        if pdf_file:
            st.subheader("Preview")
            display_pdf(pdf_file)
            
            if st.button("Add to Knowledge Base"):
                with st.spinner("Indexing PDF..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                        f.write(pdf_file.getvalue())
                        st.session_state.app.add(f.name, data_type="pdf_file")
                    os.remove(f.name)
                st.success(f"Added {pdf_file.name} to knowledge base!")

        if st.button("Clear Chat History", type="secondary"):
            st.session_state.messages = []
            st.rerun()

    # Chat interface
    for i, msg in enumerate(st.session_state.messages):
        message(msg["content"], is_user=msg["role"] == "user", key=str(i))

    if prompt := st.chat_input("Ask a question about the PDF..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        message(prompt, is_user=True)

        with st.spinner("Thinking..."):
            response = st.session_state.app.chat(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            message(response)

if __name__ == "__main__":
    main()
