"""
Configuration settings for the Financial Advisor Agent.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App Configuration
APP_NAME = "finance_advisor"
USER_ID = "default_user"
PAGE_TITLE = "AI Financial Advisor with Bytez"
PAGE_ICON = "💰"

# Model Configuration
# Using a capable open source model available on Bytez
MODEL_ID = "meta-llama/Meta-Llama-3.1-70B-Instruct"

# Logging Configuration
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# API Keys
BYTEZ_API_KEY = os.getenv("BYTEZ_API_KEY")

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler()
        ]
    )
