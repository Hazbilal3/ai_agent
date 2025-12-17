"""
Configuration settings for Beifong Agents.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model Configuration
DEFAULT_MODEL_ID = os.getenv("DEFAULT_MODEL_ID", "gpt-4o-mini")

# Logging
LOG_LEVEL = logging.INFO

def get_config_dict():
    """Return config as dictionary for debugging."""
    return {
        "model_id": DEFAULT_MODEL_ID,
        "openai_key_present": bool(OPENAI_API_KEY)
    }
