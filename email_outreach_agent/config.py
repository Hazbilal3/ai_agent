"""
Configuration settings for the Email Outreach Agent.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EXA_API_KEY = os.getenv("EXA_API_KEY", "")

# App Constants
APP_TITLE = "GTM B2B Outreach Agent"
APP_ICON = "📧"

# Logging functionality
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
