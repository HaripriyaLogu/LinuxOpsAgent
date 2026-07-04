import json
from app.llm import LLMClient
from app.tools import TOOLS


class Planner:

    def __init__(self):
        self.llm = LLMClient()

    def select_tools(self, user_prompt):

        tool_descriptions = ""

        for tool_name, tool in TOOLS.items():

            tool_descriptions += f"""
Tool: {tool_name}
Description: {tool['description']}
"""

        prompt = f"""
You are a Senior Linux Administrator.

A user asked:

{user_prompt}

Available tools:

{tool_descriptions}

Select the required tools.

Return ONLY JSON.

Example:

{{
    "tools":[
        "filesystem",
        "memory"
    ]
}}
"""

        response = self.llm.ask(prompt)

        return json.loads(response)