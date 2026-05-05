import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

# TWSE API config
TWSE_BASE_URL = "https://openapi.twse.com.tw/v1"