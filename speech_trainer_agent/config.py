"""
Configuration settings for the Speech Trainer Agent.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")

# App Info
APP_TITLE = "AI Speech Trainer Agent"
APP_ICON = "🎙️"

# Logging functionality
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
