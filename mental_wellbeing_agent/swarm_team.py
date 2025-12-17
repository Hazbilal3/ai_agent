"""
Mental Wellbeing Swarm Team Logic.
Author: Danish (Dan-445)
"""
import streamlit as st
from autogen import (SwarmAgent, SwarmResult, initiate_swarm_chat, OpenAIWrapper, AFTER_WORK, UPDATE_SYSTEM_MESSAGE)
import logging

logger = logging.getLogger(__name__)

SYSTEM_MESSAGES = {
    "assessment_agent": """
    You are an experienced mental health professional speaking directly to the user. Your task is to:
    1. Create a safe space by acknowledging their courage in seeking support
    2. Analyze their emotional state with clinical precision and genuine empathy
    3. Ask targeted follow-up questions to understand their full situation
    4. Identify patterns in their thoughts, behaviors, and relationships
    5. Assess risk levels with validated screening approaches
    6. Help them understand their current mental health in accessible language
    7. Validate their experiences without minimizing or catastrophizing

    Always use "you" and "your" when addressing the user. Blend clinical expertise with genuine warmth and never rush to conclusions.
    """,
    "action_agent": """
    You are a crisis intervention and resource specialist speaking directly to the user. Your task is to:
    1. Provide immediate evidence-based coping strategies tailored to their specific situation
    2. Prioritize interventions based on urgency and effectiveness
    3. Connect them with appropriate mental health services while acknowledging barriers (cost, access, stigma)
    4. Create a concrete daily wellness plan with specific times and activities
    5. Suggest specific support communities with details on how to join
    6. Balance crisis resources with empowerment techniques
    7. Teach simple self-regulation techniques they can use immediately

    Focus on practical, achievable steps that respect their current capacity and energy levels. Provide options ranging from minimal effort to more involved actions.
    """,
    "followup_agent": """
    You are a mental health recovery planner speaking directly to the user. Your task is to:
    1. Design a personalized long-term support strategy with milestone markers
    2. Create a progress monitoring system that matches their preferences and habits
    3. Develop specific relapse prevention strategies based on their unique triggers
    4. Establish a support network mapping exercise to identify existing resources
    5. Build a graduated self-care routine that evolves with their recovery
    6. Plan for setbacks with self-compassion techniques
    7. Set up a maintenance schedule with clear check-in mechanisms

    Focus on building sustainable habits that integrate with their lifestyle and values. Emphasize progress over perfection and teach skills for self-directed care.
    """
}

def update_assessment_overview(assessment_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["assessment"] = assessment_summary
    # UI side effect - might want to callback instead, but streamlit context works here
    st.sidebar.success('Assessment: ' + assessment_summary[:50] + "...") 
    return SwarmResult(agent="action_agent", context_variables=context_variables)

def update_action_overview(action_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["action"] = action_summary
    st.sidebar.success('Action Plan: ' + action_summary[:50] + "...")
    return SwarmResult(agent="followup_agent", context_variables=context_variables)

def update_followup_overview(followup_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["followup"] = followup_summary
    st.sidebar.success('Follow-up Strategy: ' + followup_summary[:50] + "...")
    return SwarmResult(agent="assessment_agent", context_variables=context_variables)

def update_system_message_func(agent: SwarmAgent, messages) -> str:
    system_prompt = SYSTEM_MESSAGES[agent.name]
    current_gen = agent.name.split("_")[0]
    
    if agent._context_variables.get(current_gen) is None:
        system_prompt += f"Call the update function provided to first provide a 2-3 sentence summary of your ideas on {current_gen.upper()} based on the context provided."
        agent.llm_config['tool_choice'] = {"type": "function", "function": {"name": f"update_{current_gen}_overview"}}
    else:
        agent.llm_config["tools"] = None
        agent.llm_config['tool_choice'] = None
        system_prompt += f"\n\nYour task\nYou task is write the {current_gen} part of the report. Do not include any other parts. Do not use XML tags.\nStart your reponse with: '## {current_gen.capitalize()} Design'."    
        k = list(agent._oai_messages.keys())[-1]
        agent._oai_messages[k] = agent._oai_messages[k][:1]

    system_prompt += f"\n\n\nBelow are some context for you to refer to:"
    for k, v in agent._context_variables.items():
        if v is not None:
            system_prompt += f"\n{k.capitalize()} Summary:\n{v}"

    agent.client = OpenAIWrapper(**agent.llm_config)
    return system_prompt

def run_mental_health_swarm(task: str, api_key: str):
    """
    Runs the AutoGen Swarm for mental wellbeing.
    """
    llm_config = {
        "config_list": [{"model": "gpt-4o", "api_key": api_key}]
    }

    state_update = UPDATE_SYSTEM_MESSAGE(update_system_message_func)

    assessment_agent = SwarmAgent(
        "assessment_agent", 
        llm_config=llm_config,
        functions=update_assessment_overview,
        update_agent_state_before_reply=[state_update]
    )

    action_agent = SwarmAgent(
        "action_agent",
        llm_config=llm_config,
        functions=update_action_overview,
        update_agent_state_before_reply=[state_update]
    )

    followup_agent = SwarmAgent(
        "followup_agent",
        llm_config=llm_config,
        functions=update_followup_overview,
        update_agent_state_before_reply=[state_update]
    )

    assessment_agent.register_hand_off(AFTER_WORK(action_agent))
    action_agent.register_hand_off(AFTER_WORK(followup_agent))
    followup_agent.register_hand_off(AFTER_WORK(assessment_agent))

    result, _, _ = initiate_swarm_chat(
        initial_agent=assessment_agent,
        agents=[assessment_agent, action_agent, followup_agent],
        user_agent=None,
        messages=task,
        max_rounds=13, # Allows enough turns for hand-offs
    )
    
    return result
