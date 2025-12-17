"""
Main Entry Point for Mental Wellbeing Agent.
Author: Danish (Dan-445)
"""
import streamlit as st
import os

from config import OPENAI_API_KEY, APP_TITLE, APP_ICON, setup_logging
from swarm_team import run_mental_health_swarm

# Initialize logging
setup_logging()

# Disable Docker for Autogen
os.environ["AUTOGEN_USE_DOCKER"] = "0"

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")
    
    st.title(f"{APP_ICON} {APP_TITLE}")
    
    # Sidebar
    st.sidebar.title("Configuration")
    api_key_input = st.sidebar.text_input("OpenAI API Key", type="password", value=OPENAI_API_KEY)
    
    # Safety Warning
    st.sidebar.warning("""
    ## ⚠️ Important Notice
    
    This application is a supportive tool and does not replace professional mental health care. 
    If you're experiencing thoughts of self-harm or severe crisis:
    
    - Call National Crisis Hotline: 988
    - Call Emergency Services: 911
    - Seek immediate professional help
    """)
    
    st.info("""
    **Meet Your Mental Wellbeing Agent Team:**
    
    🧠 **Assessment Agent** - Analyzes your situation and emotional needs
    🎯 **Action Agent** - Creates immediate action plan and connects you with resources
    🔄 **Follow-up Agent** - Designs your long-term support strategy
    """)

    # User Inputs
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        mental_state = st.text_area("How have you been feeling recently?", 
            placeholder="Describe your emotional state, thoughts, or concerns...")
        sleep_pattern = st.select_slider(
            "Sleep Pattern (hours per night)",
            options=[f"{i}" for i in range(0, 13)],
            value="7"
        )
        
    with col2:
        stress_level = st.slider("Current Stress Level (1-10)", 1, 10, 5)
        support_system = st.multiselect(
            "Current Support System",
            ["Family", "Friends", "Therapist", "Support Groups", "None"]
        )

    recent_changes = st.text_area(
        "Any significant life changes or events recently?",
        placeholder="Job changes, relationships, losses, etc..."
    )
    
    current_symptoms = st.multiselect(
        "Current Symptoms",
        ["Anxiety", "Depression", "Insomnia", "Fatigue", "Loss of Interest", 
         "Difficulty Concentrating", "Changes in Appetite", "Social Withdrawal",
         "Mood Swings", "Physical Discomfort"]
    )

    if st.button("Get Support Plan"):
        if not api_key_input:
            st.error("Please enter your OpenAI API key in the sidebar.")
            return
            
        with st.spinner('🤖 AI Agents are analyzing your situation...'):
            try:
                task = f"""
                Create a comprehensive mental health support plan based on:
                
                Emotional State: {mental_state}
                Sleep: {sleep_pattern} hours per night
                Stress Level: {stress_level}/10
                Support System: {', '.join(support_system) if support_system else 'None reported'}
                Recent Changes: {recent_changes}
                Current Symptoms: {', '.join(current_symptoms) if current_symptoms else 'None reported'}
                """
                
                # Run the swarm
                result = run_mental_health_swarm(task, api_key_input)
                
                # Extract results from chat history
                # Assuming the last 3 messages correspond to the final outputs of each agent
                # This logic mimics the original script, though robust extraction by agent name is better
                
                if len(result.chat_history) >= 3:
                    assessment_content = result.chat_history[-3]['content']
                    action_content = result.chat_history[-2]['content']
                    followup_content = result.chat_history[-1]['content']
                    
                    with st.expander("Situation Assessment", expanded=True):
                        st.markdown(assessment_content)

                    with st.expander("Action Plan & Resources", expanded=True):
                        st.markdown(action_content)

                    with st.expander("Long-term Support Strategy", expanded=True):
                        st.markdown(followup_content)
                    
                    st.success('✨ Mental health support plan generated successfully!')
                else:
                    st.warning("The agents discussed the topic but did not produce the expected structured output. Please check the logs.")
                    st.write(result.chat_history)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
