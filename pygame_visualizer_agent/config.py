"""
Configuration settings for AI 3D Pygame R1.
Author: Danish (Dan-445)
"""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")

# App Info
APP_TITLE = "🎮 AI 3D Visualizer with DeepSeek R1"
APP_ICON = "🎮"

# Logging functionality
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
