"""
Configuration settings for the Home Renovation Agent.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "") # Alternate name

# Use GOOGLE_API_KEY as primary if available
if not GOOGLE_API_KEY and GEMINI_API_KEY:
    GOOGLE_API_KEY = GEMINI_API_KEY

# Model IDs
DEFAULT_MODEL = "gemini-2.5-flash"

# App Info
APP_TITLE = "AI Home Renovation Planner 🏠"
APP_ICON = "🔨"

# Logging functionality
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
