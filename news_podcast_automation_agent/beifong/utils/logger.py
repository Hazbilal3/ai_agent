"""
Logging configuration for Beifong.
Author: Danish (Dan-445)
"""
import logging
import sys

# Create a custom logger
logger = logging.getLogger("beifong")

# Configure logger if it hasn't been configured yet
if not logger.handlers:
    logger.setLevel(logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add formatter to handler
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)

def get_logger(name: str):
    """Get a logger instance with the specified name."""
    return logging.getLogger(f"beifong.{name}")
