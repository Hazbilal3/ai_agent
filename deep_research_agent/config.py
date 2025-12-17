"""
Configuration settings for the Deep Research Agent.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY", "")

# Model Config
MODEL_ID = "Qwen/Qwen3-235B-A22B-fp8-tput"

# App Info
APP_TITLE = "AI DeepResearch Agent"
APP_ICON = "🔍"

# Logging functionality
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
