import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
AGENTQL_API_KEY = os.getenv("AGENTQL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not all([EMAIL, PASSWORD, AGENTQL_API_KEY]):
    raise ValueError("Missing EMAIL, PASSWORD or AGENTQL_API_KEY in .env")