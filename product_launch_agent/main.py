"""
Main Entry Point for Product Launch Agent.
Author: Danish (Dan-445)
"""
import streamlit as st
import os

from config import OPENAI_API_KEY, FIRECRAWL_API_KEY, APP_TITLE, APP_ICON, setup_logging
from launch_team import create_product_team, expand_competitor_report, expand_sentiment_report, expand_metrics_report
from agno.run.agent import RunOutput

# Initialize logging
setup_logging()

def main():
    st.set_page_config(
        page_title=APP_TITLE, 
        page_icon=APP_ICON, 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    if "competitor_response" not in st.session_state:
        st.session_state.competitor_response = None
    if "sentiment_response" not in st.session_state:
        st.session_state.sentiment_response = None
    if "metrics_response" not in st.session_state:
        st.session_state.metrics_response = None

    # Sidebar: API Keys
    with st.sidebar:
        st.header("🔑 API Configuration")
        openai_key = st.text_input("OpenAI API Key", type="password", value=OPENAI_API_KEY)
        firecrawl_key = st.text_input("Firecrawl API Key", type="password", value=FIRECRAWL_API_KEY)
        
        st.divider()
        st.markdown("### 🤖 System Status")
        if openai_key and firecrawl_key:
            st.success("✅ Team Ready")
            product_team = create_product_team(openai_key, firecrawl_key)
        else:
            st.error("❌ API Keys Required")
            product_team = None

        st.divider()
        st.markdown("### 🎯 Coordinated Team")
        st.markdown("""
        **🔍 Product Launch Analyst**
        *Strategic GTM expert*
        
        **💬 Market Sentiment Specialist**
        *Consumer perception expert*
        
        **📈 Launch Metrics Specialist**
        *Performance analytics expert*
        """)

    # Main Content
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.markdown("*AI-powered insights for GTM, Product Marketing & Growth Teams*")
    st.divider()

    col1, col2 = st.columns([3, 1])
    with col1:
        company_name = st.text_input("Company Name", placeholder="e.g. OpenAI, Tesla, Spotify")
    with col2:
        if company_name:
            st.success(f"✓ Target: **{company_name}**")

    st.divider()

    # Tabs
    tab1, tab2, tab3 = st.tabs(["🔍 Competitor Analysis", "💬 Market Sentiment", "📈 Launch Metrics"])

    # TAB 1: Competitor Analysis
    with tab1:
        st.markdown("### 🔍 Competitor Launch Analysis")
        if company_name:
            if st.button("🚀 Analyze Strategy", key="btn_comp"):
                if not product_team:
                    st.error("Please provide API keys first.")
                else:
                    with st.spinner("Analyzing competitive strategy..."):
                        try:
                            bullets: RunOutput = product_team.run(
                                f"Generate up to 16 evidence-based insight bullets about {company_name}'s most recent product launches.\n"
                                f"Format requirements:\n"
                                f"• Start every bullet with exactly one tag: Positioning | Strength | Weakness | Learning\n"
                                f"• Follow the tag with a concise statement (max 30 words) referencing concrete observations."
                            )
                            report = expand_competitor_report(product_team, bullets.content, company_name)
                            st.session_state.competitor_response = report
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {e}")
        
        if st.session_state.competitor_response:
            st.markdown(st.session_state.competitor_response)

    # TAB 2: Market Sentiment
    with tab2:
        st.markdown("### 💬 Market Sentiment Analysis")
        if company_name:
            if st.button("📊 Analyze Sentiment", key="btn_sent"):
                if not product_team:
                    st.error("Please provide API keys first.")
                else:
                    with st.spinner("Analyzing market sentiment..."):
                        try:
                            bullets: RunOutput = product_team.run(
                                f"Summarize market sentiment for {company_name} in <=10 bullets. "
                                f"Cover top positive & negative themes with source mentions."
                            )
                            report = expand_sentiment_report(product_team, bullets.content, company_name)
                            st.session_state.sentiment_response = report
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {e}")
                            
        if st.session_state.sentiment_response:
            st.markdown(st.session_state.sentiment_response)

    # TAB 3: Launch Metrics
    with tab3:
        st.markdown("### 📈 Launch Performance Metrics")
        if company_name:
            if st.button("📈 Analyze Metrics", key="btn_met"):
                if not product_team:
                    st.error("Please provide API keys first.")
                else:
                    with st.spinner("Analyzing launch metrics..."):
                        try:
                            bullets: RunOutput = product_team.run(
                                f"List (max 10 bullets) the most important publicly available KPIs & qualitative signals for {company_name}'s recent launches."
                            )
                            report = expand_metrics_report(product_team, bullets.content, company_name)
                            st.session_state.metrics_response = report
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {e}")

        if st.session_state.metrics_response:
            st.markdown(st.session_state.metrics_response)

if __name__ == "__main__":
    main()
