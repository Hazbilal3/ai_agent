"""
Main entry point for the Deep Research Agent.
Author: Danish (Dan-445)
"""
import streamlit as st
from config import TOGETHER_API_KEY, COMPOSIO_API_KEY, APP_TITLE, APP_ICON, setup_logging
from research_logic import DeepResearchSystem

# Initialize logging
setup_logging()

# Set page config
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

def initialize_session_state():
    """Initialize Streamlit session state."""
    if 'system' not in st.session_state:
        st.session_state.system = None
    if 'api_keys' not in st.session_state:
        st.session_state.api_keys = {
            'together': TOGETHER_API_KEY,
            'composio': COMPOSIO_API_KEY
        }
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'question_answers' not in st.session_state:
        st.session_state.question_answers = []
    if 'report_content' not in st.session_state:
        st.session_state.report_content = ""
    if 'research_complete' not in st.session_state:
        st.session_state.research_complete = False

def render_sidebar():
    """Render the sidebar configuration."""
    st.sidebar.header("⚙️ Configuration")
    
    # API key inputs (pre-filled from env/config if available)
    new_together = st.sidebar.text_input(
        "Together AI API Key", 
        value=st.session_state.api_keys['together'],
        type="password",
        help="Get your API key from https://together.ai"
    )
    
    new_composio = st.sidebar.text_input(
        "Composio API Key", 
        value=st.session_state.api_keys['composio'],
        type="password",
        help="Get your API key from https://composio.ai"
    )
    
    # Update keys in state if changed
    if new_together != st.session_state.api_keys['together'] or new_composio != st.session_state.api_keys['composio']:
        st.session_state.api_keys['together'] = new_together
        st.session_state.api_keys['composio'] = new_composio
        # Reset system to force re-init with new keys
        st.session_state.system = None
        st.success("API Keys updated!")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info(
        "This AI DeepResearch Agent uses Together AI's Qwen model and Composio tools to perform comprehensive research on any topic."
    )

def main():
    initialize_session_state()
    render_sidebar()
    
    st.title(f"{APP_ICON} {APP_TITLE}")
    
    # Check for keys
    if not st.session_state.api_keys['together'] or not st.session_state.api_keys['composio']:
        st.warning("⚠️ Please enter your Together AI and Composio API keys in the sidebar to get started.")
        return

    # Initialize System if needed
    if st.session_state.system is None:
        try:
            with st.spinner("Initializing Agent System..."):
                st.session_state.system = DeepResearchSystem(
                    together_key=st.session_state.api_keys['together'],
                    composio_key=st.session_state.api_keys['composio']
                )
        except Exception as e:
            st.error(f"Failed to initialize system: {e}")
            return

    # User Inputs
    st.header("Research Topic")
    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("What topic would you like to research?", placeholder="American Tariffs")
    with col2:
        domain = st.text_input("What domain is this topic in?", placeholder="Politics, Economics, Technology...")

    # Step 1: Generate Questions
    if topic and domain:
        if st.button("Generate Research Questions"):
            with st.spinner("🤖 Generating research questions..."):
                try:
                    questions = st.session_state.system.generate_questions(topic, domain)
                    st.session_state.questions = questions
                    # Reset subsequent steps
                    st.session_state.question_answers = []
                    st.session_state.research_complete = False
                except Exception as e:
                    st.error(f"Error generating questions: {e}")

    # Display Questions
    if st.session_state.questions:
        st.header("Research Questions")
        for i, q in enumerate(st.session_state.questions):
            st.markdown(f"**{i+1}.** {q}")
        
        # Step 2: Start Research
        if st.button("Start Research"):
            st.session_state.question_answers = [] # clear previous
            progress_bar = st.progress(0)
            
            for i, question in enumerate(st.session_state.questions):
                with st.spinner(f"🔍 Researching question {i+1}/{len(st.session_state.questions)}..."):
                    answer = st.session_state.system.research_question(topic, domain, question)
                    st.session_state.question_answers.append({
                        "question": question,
                        "answer": answer
                    })
                progress_bar.progress((i + 1) / len(st.session_state.questions))
            
            st.success("Research completed!")

    # Display Research Results and Compilation
    if st.session_state.question_answers:
        st.header("Research Results")
        for i, qa in enumerate(st.session_state.question_answers):
            with st.expander(f"Q: {qa['question']}", expanded=True):
                st.markdown(qa['answer'])
        
        # Step 3: Compile Report
        if st.button("Compile Final Report"):
            with st.spinner("📝 Compiling report & creating Google Doc..."):
                try:
                    report = st.session_state.system.compile_report(
                        topic, domain, st.session_state.question_answers
                    )
                    st.session_state.report_content = report
                    st.session_state.research_complete = True
                except Exception as e:
                    st.error(f"Error compiling report: {e}")

    # Final Report Display
    if st.session_state.research_complete and st.session_state.report_content:
        st.header("Final Compiled Report")
        st.success("Report generated and saved to Google Docs!")
        st.markdown(st.session_state.report_content)

if __name__ == "__main__":
    main()
