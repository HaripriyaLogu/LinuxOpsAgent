import json

from app.llm import LLMClient


class IntentClassifier:

    def __init__(self):
        self.llm = LLMClient()

    def classify(self, user_prompt):

        prompt = f"""
You are an AI Intent Classifier.

Your job is ONLY to classify the user's request.

Possible intents:

1. knowledge
   - User wants explanation.
   - User wants Linux concepts.
   - User asks "how to".
   - User asks theory.

Examples:
- What is NFS?
- Explain LVM.
- How do I create a Linux user?
- What is Pacemaker?

2. diagnostic
   - User wants to inspect a real Linux server.
   - User wants troubleshooting.
   - User reports an issue.

Examples:
- Check filesystem
- Check disk usage
- My server is slow
- Analyze memory
- CPU usage is high
- Filesystem is full
- Show failed services

3. action
   - User wants to modify the Linux server.

Examples:
- Restart nginx
- Create user hari
- Install Docker
- Delete logs
- Reboot server

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT write explanations.

Return exactly like this:

{{
    "intent":"knowledge"
}}

User Request:

{user_prompt}
"""

        response = self.llm.ask(prompt)

        print("\nClassifier Response:")
        print(response)

        # Remove markdown if the model still returns it
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        try:
            result = json.loads(response)

            if result["intent"] not in [
                "knowledge",
                "diagnostic",
                "action",
            ]:
                raise ValueError("Invalid intent")

            return result

        except Exception:

            print("Classifier returned invalid JSON.")
            print("Using fallback classification.")

            prompt_lower = user_prompt.lower()

            if any(word in prompt_lower for word in [
                "check",
                "show",
                "analyze",
                "filesystem",
                "disk",
                "memory",
                "cpu",
                "slow",
                "server",
            ]):
                return {"intent": "diagnostic"}

            if any(word in prompt_lower for word in [
                "restart",
                "create",
                "delete",
                "install",
                "remove",
                "reboot",
            ]):
                return {"intent": "action"}

            return {"intent": "knowledge"}