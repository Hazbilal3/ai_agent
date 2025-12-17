"""
Configuration settings for Chat with PDF.
Author: Danish (Dan-445)
"""
import os
import logging

# App Info
APP_TITLE = "📄 Chat with PDF (Llama 3.2)"
APP_ICON = "📄"

# Logging functionality
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
