import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))