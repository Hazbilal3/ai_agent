"""
User Interface components for the Financial Advisor Agent.
Author: Danish (Dan-445)
"""
import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, Any, Union, List

def load_custom_css():
    """Injects custom CSS for a premium dark theme makeover with high contrast."""
    st.markdown("""
        <style>
        /* Import Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        /* Global Variables */
        :root {
            --bg-color: #0e1117;
            --secondary-bg-color: #262730;
            --text-color: #fafafa;
            --text-secondary: #d1d5db;
            --accent-color: #7c3aed;
            --card-border: rgba(250, 250, 250, 0.2);
        }

        /* FORCE Dark Theme Backgrounds and Text */
        .stApp {
            background-color: var(--bg-color);
            color: var(--text-color);
        }
        
        /* Force text color for all basic elements */
        p, h1, h2, h3, h4, h5, h6, span, div, label {
            color: var(--text-color) !important;
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: var(--secondary-bg-color);
            border-right: 1px solid var(--card-border);
        }
        section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
             color: var(--text-secondary) !important;
        }

        /* Metric Cards */
        [data-testid="stMetric"] {
            background-color: var(--secondary-bg-color);
            border: 1px solid var(--card-border);
            padding: 1rem;
            border-radius: 8px;
            color: var(--text-color);
        }
        
        [data-testid="stMetricLabel"] {
            color: var(--text-secondary) !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--text-color) !important;
        }

        /* Input Fields - CRITICAL FOR VISIBILITY */
        .stTextInput input, .stNumberInput input, .stSelectbox select, .stTextArea textarea {
            background-color: #1f2937 !important; 
            color: white !important;
            border: 1px solid var(--card-border) !important;
        }

        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
            color: white !important;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: var(--secondary-bg-color);
            color: var(--text-secondary);
            border-radius: 4px;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: var(--accent-color);
            color: white !important;
        }
        
        /* Datatables */
        [data-testid="stDataFrame"] {
            background-color: var(--secondary-bg-color);
        }
        
        /* Headings Gradient override */
        h1 {
            background: linear-gradient(to right, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            color: transparent !important; /* Required for gradient text */
        }
        
        /* Reset containers to ensure no white backgrounds leak through */
        .block-container {
            background-color: transparent;
        }
        
        </style>
    """, unsafe_allow_html=True)

def display_budget_analysis(analysis: Union[Dict[str, Any], str]):
    """Display budget analysis results in Streamlit."""
    if isinstance(analysis, str):
        try:
            analysis = json.loads(analysis)
        except json.JSONDecodeError:
            st.error("Failed to parse results")
            return
            
    if not isinstance(analysis, dict):
        return

    # Charts
    if "spending_categories" in analysis:
        st.subheader("📊 Spending Breakdown")
        cats = analysis.get("spending_categories", [])
        if cats:
            vals = [c.get("amount", 0) for c in cats]
            names = [c.get("category", "Unknown") for c in cats]
            
            fig = px.pie(values=vals, names=names, hole=0.4)
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig, use_container_width=True)

    # Recommendations
    if "recommendations" in analysis:
        st.subheader("💡 Recommendations")
        for rec in analysis.get("recommendations", []):
            with st.container():
                st.markdown(f"**{rec.get('category', 'Tip')}**: {rec.get('recommendation', '')}")
                if rec.get("potential_savings"):
                    st.success(f"Potential Savings: ${rec.get('potential_savings')}")
                st.divider()

def display_savings_strategy(strategy: Union[Dict[str, Any], str]):
    """Display savings strategy results."""
    if isinstance(strategy, str):
        try: strategy = json.loads(strategy)
        except: return
        
    st.subheader("🛡️ Savings Strategy")
    
    col1, col2 = st.columns(2)
    if "emergency_fund" in strategy:
        ef = strategy["emergency_fund"]
        with col1:
            st.metric("Recommended Emergency Fund", f"${ef.get('recommended_amount', 0):,.2f}")
            st.metric("Current Status", ef.get('current_status', 'Unknown'))
            
    if "recommendations" in strategy:
        with col2:
            st.markdown("#### Allocation")
            for rec in strategy.get("recommendations", []):
                st.markdown(f"- **{rec.get('category')}**: ${rec.get('amount', 0)}")

    if "automation_techniques" in strategy:
        st.subheader("⚙️ Automation")
        for tech in strategy.get("automation_techniques", []):
            st.info(f"**{tech.get('name')}**: {tech.get('description')}")

def display_debt_reduction(plan: Union[Dict[str, Any], str]):
    """Display debt reduction plan."""
    if isinstance(plan, str):
        try: plan = json.loads(plan)
        except: return
        
    if "total_debt" in plan:
        st.metric("Total Debt", f"${plan.get('total_debt', 0):,.2f}")
        
    if "payoff_plans" in plan:
        plans = plan["payoff_plans"]
        tabs = st.tabs(["Avalanche", "Snowball"])
        with tabs[0]:
            p = plans.get("avalanche", {})
            st.metric("Total Interest", f"${p.get('total_interest', 0):,.2f}")
            st.metric("Months to Freedom", p.get('months_to_payoff', 0))
        with tabs[1]:
            p = plans.get("snowball", {})
            st.metric("Total Interest", f"${p.get('total_interest', 0):,.2f}")
            st.metric("Months to Freedom", p.get('months_to_payoff', 0))

def display_csv_preview(df: pd.DataFrame):
    """Preview CSV data."""
    if df is None or df.empty: return
    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)
