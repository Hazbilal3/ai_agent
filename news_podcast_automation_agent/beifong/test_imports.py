
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

try:
    print("Testing imports...")
    from agents import search_agent
    print(" - search_agent imported")
    from agents import scrape_agent
    print(" - scrape_agent imported")
    from agents import script_agent
    print(" - script_agent imported")
    from agents import image_generate_agent
    print(" - image_generate_agent imported")
    from agents import audio_generate_agent
    print(" - audio_generate_agent imported")
    from models import agent_schemas
    print(" - agent_schemas imported")
    from utils import logger
    print(" - logger imported")
    print("SUCCESS: All modules imported correctly.")
except Exception as e:
    print(f"FAILURE: Import failed with error: {e}")
    sys.exit(1)
