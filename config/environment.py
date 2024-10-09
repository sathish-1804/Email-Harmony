import os
from dotenv import load_dotenv

def load_environment():
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve sensitive data from environment variables
    api_keys = {
        "GENAI_API_KEY": os.getenv("GENAI_API_KEY"),
        "NYLAS_API_KEY": os.getenv("NYLAS_API_KEY"),
        "NYLAS_API_URI": os.getenv("NYLAS_API_URI"),
        "NYLAS_EMAIL": os.getenv("NYLAS_EMAIL"),
        "NYLAS_CALENDAR_ID": os.getenv("NYLAS_CALENDAR_ID"),
        "PINECONE_API_KEY": os.getenv("PINECONE_API_KEY"),
    }
    return api_keys
