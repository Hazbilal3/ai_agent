"""
Main Entry Point for AI 3D Pygame R1.
Author: Danish (Dan-445)
"""
import streamlit as st
import asyncio
from config import APP_TITLE, APP_ICON, DEEPSEEK_API_KEY, OPENAI_API_KEY, setup_logging
from logic import generate_pygame_reasoning, extract_pygame_code, run_pygame_on_trinket

# Initialize logging
setup_logging()

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")
    
    # Initialize session state for generated code
    if "generated_code" not in st.session_state:
        st.session_state.generated_code = None

    # Sidebar
    st.sidebar.title("Configuration")
    deepseek_key = st.sidebar.text_input("DeepSeek API Key", type="password", value=DEEPSEEK_API_KEY)
    openai_key = st.sidebar.text_input("OpenAI API Key", type="password", value=OPENAI_API_KEY)
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    📝 **How to use:**
    1. Enter your API keys above.
    2. Write your PyGame visualization query.
    3. Click 'Generate Code' to get the code.
    4. Click 'Generate Visualization' to:
       - Open Trinket.io PyGame editor
       - **Copy and paste** the generated code (Browser Agent will wait for you)
       - Watch it run automatically
    """)

    # Main UI
    st.title(f"{APP_ICON} {APP_TITLE}")
    example_query = "Create a particle system simulation where 100 particles emit from the mouse position and respond to keyboard-controlled wind forces"
    query = st.text_area(
        "Enter your PyGame query:",
        height=70,
        placeholder=f"e.g.: {example_query}"
    )

    col1, col2 = st.columns(2)
    generate_code_btn = col1.button("Generate Code", use_container_width=True, type="primary")
    generate_vis_btn = col2.button("Generate Visualization (Run on Trinket)", use_container_width=True)

    # Logic: Generate Code
    if generate_code_btn:
        if not deepseek_key or not openai_key:
            st.error("❌ Please provide both API keys in the sidebar.")
        elif not query:
            st.warning("⚠️ Please enter a query.")
        else:
            try:
                with st.spinner("🧠 DeepSeek R1 is thinking..."):
                    reasoning = generate_pygame_reasoning(query, deepseek_key)
                
                with st.expander("🤔 R1's Reasoning Process", expanded=False):
                    st.write(reasoning)
                    
                with st.spinner("💻 Extracting Python Code..."):
                    code = extract_pygame_code(reasoning, openai_key)
                    st.session_state.generated_code = code
                
                st.success("✅ Code generated successfully!")
                
            except Exception as e:
                st.error(f"Error: {e}")

    # Display Code if available
    if st.session_state.generated_code:
        with st.expander("📜 Generated Pygame Code", expanded=True):
            st.code(st.session_state.generated_code, language="python")

    # Logic: Visualize
    if generate_vis_btn:
        if not st.session_state.generated_code:
            st.warning("⚠️ Please generate code first.")
        else:
            if not openai_key:
                st.error("OpenAI Key required for Browser Agent.")
            else:
                st.info("🚀 Launching Browser Agent... Please verify Trinket opens.")
                try:
                    asyncio.run(run_pygame_on_trinket(st.session_state.generated_code, openai_key))
                    st.success("Done!")
                except Exception as e:
                    st.error(f"Browser automation failed: {e}")

if __name__ == "__main__":
    main()
