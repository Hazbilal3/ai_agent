"""
Main Entry Point for Speech Trainer Agent.
Author: Danish (Dan-445)
"""
import streamlit as st
import os
import json
import tempfile
import numpy as np
import plotly.graph_objects as go
from config import APP_TITLE, APP_ICON, TOGETHER_API_KEY, setup_logging
from agents.coordinator_agent import coordinator_agent
from agno.agent import RunResponse

# Initialize logging
setup_logging()

# Page Config
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title(f"{APP_ICON} {APP_TITLE}")
    
    # Sidebar
    st.sidebar.header("Configuration")
    api_key_input = st.sidebar.text_input("Together API Key", type="password", value=TOGETHER_API_KEY)
    
    if api_key_input:
        os.environ["TOGETHER_API_KEY"] = api_key_input

    st.sidebar.info("""
    **How it works:**
    1. Upload a video of your speech.
    2. AI Agents analyze facial expressions, voice, and content.
    3. Get a detailed report with scores and feedback.
    """)

    # Session State
    if "response" not in st.session_state:
        st.session_state.response = None
    if "video_path" not in st.session_state:
        st.session_state.video_path = None

    # App Layout
    col1, col2 = st.columns([0.4, 0.6])

    with col1:
        st.subheader("📹 Video Input")
        uploaded_file = st.file_uploader("Upload a video (mp4)", type=["mp4"])
        
        if uploaded_file is not None:
             # Save temp file
            temp_dir = tempfile.gettempdir()
            unique_name = f"{int(np.random.rand()*1e8)}_{uploaded_file.name}"
            file_path = os.path.join(temp_dir, unique_name)
            
            # Simple caching mechanism: don't re-save if same name (not perfect but ok for demo)
            if st.session_state.video_path != file_path:
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                st.session_state.video_path = file_path
                st.session_state.response = None # Reset response on new video
            
            st.video(st.session_state.video_path)

            if st.button("🚀 Analyze Speech", type="primary", use_container_width=True):
                if not api_key_input:
                    st.error("Please enter a Together API Key.")
                else:
                    with st.spinner("🤖 AI Agents are analyzing your facial expressions, voice, and content..."):
                        try:
                            # Run the coordinator agent
                            prompt = f"Analyze the following video: {st.session_state.video_path}"
                            # coordinator_agent is a Team, we run it
                            resp: RunResponse = coordinator_agent.run(prompt)
                            
                            # The response content should be a CoordinatorResponse model (Pydantic)
                            # or a dict if using json_mode=True and it returns parsed json.
                            # agno Team.run() returns RunResponse.content which might be the model instance or dict.
                            
                            # Based on coordinator_agent definition, it specifies response_model=CoordinatorResponse.
                            # So resp.content should be an instance of CoordinatorResponse.
                            
                            if resp and resp.content:
                                # Convert Pydantic model to dict
                                if hasattr(resp.content, "model_dump"):
                                    data = resp.content.model_dump()
                                elif isinstance(resp.content, dict):
                                    data = resp.content
                                else:
                                    # Fallback if it's a string
                                    try:
                                        data = json.loads(resp.content)
                                    except:
                                        st.error("Failed to parse analysis results.")
                                        st.write(resp.content)
                                        return
                                
                                st.session_state.response = data
                                st.success("Analysis Complete!")
                            else:
                                st.error("No response received from agents.")
                        except Exception as e:
                            st.error(f"Analysis failed: {str(e)}")
                            st.exception(e)

    with col2:
        if st.session_state.response:
            data = st.session_state.response
            
            # Extract Feedback Scores
            # The JSON structure for feedback_response is a string (JSON string) inside the main JSON?
            # Let's check coordinator_agent.py: 
            # feedback_response: str = Field(..., description="Response from feedback agent")
            # And feedback_agent returns a JSON string.
            # So we typically need to parse it again if it's a string.
            
            try:
                feedback_json = data.get("feedback_response")
                if isinstance(feedback_json, str):
                    feedback_data = json.loads(feedback_json)
                else:
                    feedback_data = feedback_json
                
                scores = feedback_data.get("scores", {})
                total_score = feedback_data.get("total_score", 0)
                interpretation = feedback_data.get("interpretation", "")
                summary = feedback_data.get("feedback_summary", "")

                # Tabs for different views
                tab_overview, tab_details, tab_transcript = st.tabs(["📊 Overview & Scores", "🔍 Use Strengths & Weaknesses", "📝 Transcript"])
                
                with tab_overview:
                    st.subheader("🏆 Performance Summary")
                    
                    # Score Cards
                    sc1, sc2 = st.columns(2)
                    sc1.metric("Total Score", f"{total_score}/25")
                    sc2.metric("Rating", interpretation)
                    
                    st.info(f"**Feedback:** {summary}")
                    
                    st.divider()
                    
                    # Radar Chart
                    st.subheader("Skill Breakdown")
                    categories = list(scores.keys())
                    values = list(scores.values())
                    
                    fig = go.Figure(data=go.Scatterpolar(
                        r=values,
                        theta=[k.replace("_", " ").title() for k in categories],
                        fill='toself'
                    ))
                    fig.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                        showlegend=False
                    )
                    st.plotly_chart(fig, use_container_width=True)

                with tab_details:
                    st.subheader("💡 Detailed Insights")
                    
                    s_col, w_col, sug_col = st.columns(3)
                    
                    with s_col:
                        st.success("##### ✅ Strengths")
                        for s in data.get("strengths", []):
                            st.write(f"- {s}")
                            
                    with w_col:
                        st.error("##### ⚠️ Weaknesses")
                        for w in data.get("weaknesses", []):
                            st.write(f"- {w}")
                            
                    with sug_col:
                        st.warning("##### 🚀 Suggestions")
                        for s in data.get("suggestions", []):
                            st.write(f"- {s}")

                with tab_transcript:
                    st.subheader("📜 Transcript & Content")
                    
                    # Voice Analysis contains transcription
                    voice_json = data.get("voice_analysis_response")
                    if isinstance(voice_json, str):
                        voice_data = json.loads(voice_json)
                    else:
                        voice_data = voice_json
                        
                    transcript = voice_data.get("transcription", "No transcript available.")
                    st.text_area("Transcript", transcript, height=300)
                    
                    st.write("---")
                    
                    # Content Analysis
                    content_json = data.get("content_analysis_response")
                    if isinstance(content_json, str):
                        content_data = json.loads(content_json)
                    else:
                        content_data = content_json
                        
                    st.write("**Grammar Corrections:**")
                    st.write(content_data.get("grammar_corrections", []))
                    
                    st.write("**Filler Words:**")
                    st.write(content_data.get("filler_words", {}))

            except Exception as e:
                st.error(f"Error parsing agent response: {e}")
                st.write("Raw Response:", data)

        else:
            st.info("👈 Upload a video and click 'Analyze Speech' to get started.")

if __name__ == "__main__":
    main()
