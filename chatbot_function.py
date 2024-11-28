import os
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

openai_api_key = os.getenv(
    "OPENAI_API_KEY"
)  # get the api key which is kept inside the .env file
client = OpenAI()
