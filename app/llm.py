from openai import OpenAI
from langchain_openai import ChatOpenAI
from app.config import Config


class LLMClient:

    def __init__(self):

        self.client = OpenAI(
            base_url=Config.AZURE_OPENAI_ENDPOINT,
            api_key=Config.AZURE_OPENAI_API_KEY,
        )

        self.langchain_llm = ChatOpenAI(
            model=Config.AZURE_OPENAI_DEPLOYMENT,
            base_url=Config.AZURE_OPENAI_ENDPOINT,
            api_key=Config.AZURE_OPENAI_API_KEY,
        )

    def ask(self, prompt):

        response = self.client.responses.create(
            model=Config.AZURE_OPENAI_DEPLOYMENT,
            input=prompt,
        )

        return response.output_text