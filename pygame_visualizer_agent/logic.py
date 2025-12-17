"""
Logic for AI 3D Pygame R1.
Author: Danish (Dan-445)
"""
import streamlit as st
from openai import OpenAI
from agno.agent import Agent as AgnoAgent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat as AgnoOpenAIChat
from langchain_openai import ChatOpenAI 
from browser_use import Browser
from browser_use import Agent as BrowserAgent
import asyncio

def generate_pygame_reasoning(query: str, deepseek_key: str) -> str:
    """Generates reasoning for Pygame code using DeepSeek R1."""
    if not deepseek_key:
        raise ValueError("DeepSeek API Key is required.")

    deepseek_client = OpenAI(
        api_key=deepseek_key,
        base_url="https://api.deepseek.com"
    )

    system_prompt = """You are a Pygame and Python Expert that specializes in making games and visualisation through pygame and python programming. 
    During your reasoning and thinking, include clear, concise, and well-formatted Python code in your reasoning. 
    Always include explanations for the code you provide."""

    response = deepseek_client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        max_tokens=8000 # Increased from 1 purely for safety, though reasoning output is separate
    )
    
    return response.choices[0].message.reasoning_content

def extract_pygame_code(reasoning_content: str, openai_key: str) -> str:
    """Extracts Python code from the reasoning content using GPT-4o."""
    if not openai_key:
        raise ValueError("OpenAI API Key is required.")

    openai_agent = AgnoAgent(
        model=AgnoOpenAIChat(
            id="gpt-4o",
            api_key=openai_key
        ),
        debug_mode=True,
        markdown=True
    )

    extraction_prompt = f"""Extract ONLY the Python code from the following content which is reasoning of a particular query to make a pygame script. 
    Return nothing but the raw code without any explanations, or markdown backticks:
    {reasoning_content}"""

    code_response: RunOutput = openai_agent.run(extraction_prompt)
    return code_response.content

async def run_pygame_on_trinket(code: str, openai_key: str) -> None:
    """Automates running the Pygame code on Trinket.io using Browser Use."""
    if not openai_key:
        raise ValueError("OpenAI API Key is required.")
        
    browser = Browser()
    async with await browser.new_context() as context:
        model = ChatOpenAI(
            model="gpt-4o", 
            api_key=openai_key
        )
        
        # Navigate to Trinket
        agent1 = BrowserAgent(
            task='Go to https://trinket.io/features/pygame, thats your only job.',
            llm=model,
            browser_context=context,
        )
        
        # We need a Coder agent to Type the code?? 
        # The prompt says 'wait for the user for 10 seconds to write the code'.
        # Wait, the original code had:
        # coder = Agent(task='Coder. Your job is to wait for the user for 10 seconds to write the code in the code editor.', ...)
        # This implies it might be expecting *manual* paste or there's a missing piece where the agent *writes* the code?
        # The prompt says "Click 'Generate Visualization' to: Open Trinket... Copy and paste... Watch it run".
        # Ah, the instructions in the UI said "Copy and paste the generated code".
        # But the original code had `coder` agent... 
        # Actually, `browser-use` allows sending input. But maybe the original author intended for the USER to paste it during the wait?
        # Let's check the original UI instruction:
        # "4. Click 'Generate Visualization' to: Open Trinket.io... Copy and paste... Watch it run automatically"
        # It seems `browser-use` opens the browser, and the `coder` agent waits for the user to paste. 
        # I will preserve this logic exactly as is.
        
        coder = BrowserAgent(
            task='Coder. Your job is to wait for the user for 10 seconds to write the code in the code editor.',
            llm=model,
            browser_context=context
        )
        
        executor = BrowserAgent(
            task='Executor. Execute the code written by the User by clicking on the run button on the right.',
            llm=model,
            browser_context=context
        )
        
        viewer = BrowserAgent(
            task='Viewer. Your job is to just view the pygame window for 10 seconds.',
            llm=model,
            browser_context=context,
        )

        await agent1.run()
        # Here the user pastes the code? Or the browser is showing?
        # `browser-use` usually runs headlessly unless configured?
        # The original `Browser()` init uses defaults. 
        # If I am refactoring, I should ensure it runs so the user can see it. 
        # Default `Browser(headless=False)`?
        # The original code just did `Browser()`.
        # I will stick to original.
        
        await coder.run()
        await executor.run() 
        await viewer.run()
