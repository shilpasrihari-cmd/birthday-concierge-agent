import os
import google.generativeai as genai

# Configure API Key: reads from the GEMINI_API_KEY environment variable.
API_KEY = os.environ.get("GEMINI_API_KEY", "")
genai.configure(api_key=API_KEY)

def get_model():
    """
    Returns the configured gemini-3.5-flash GenerativeModel.
    """
    return genai.GenerativeModel("gemini-3.5-flash")

