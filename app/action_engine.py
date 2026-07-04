import json

from app.llm import LLMClient


class ActionEngine:

    def __init__(self):
        self.llm = LLMClient()

    def generate_commands(self, user_prompt):

        prompt = f"""
You are a Senior Linux Administrator.

Your job is to convert a user's request into Linux commands.

Rules:

- Generate ONLY safe Linux commands.
- Do NOT explain anything.
- Do NOT use markdown.
- Return ONLY JSON.

Example:

{{
    "commands":[
        "sudo systemctl restart nginx"
    ]
}}

User Request:

{user_prompt}
"""

        response = self.llm.ask(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)