import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    # Linux VM
    VM_HOST = os.getenv("VM_HOST")
    VM_USERNAME = os.getenv("VM_USERNAME")
    SSH_KEY_PATH = os.getenv("SSH_KEY_PATH")