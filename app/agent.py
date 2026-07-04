from app.llm import LLMClient
from app.ssh_client import LinuxSSHClient
from app.config import Config
from app.tools import TOOLS
from app.planner import Planner
from app.classifier import IntentClassifier
from app.action_engine import ActionEngine
from app.safety import SafetyEngine
from app.memory import ConversationMemory
from app.logger import AgentLogger


class LinuxOpsAgent:

    def __init__(self):

        self.llm = LLMClient()
        self.classifier = IntentClassifier()
        self.planner = Planner()
        self.action_engine = ActionEngine()
        self.safety = SafetyEngine()
        self.memory = ConversationMemory()
        self.logger = AgentLogger()

        self.ssh = LinuxSSHClient(
            host=Config.VM_HOST,
            username=Config.VM_USERNAME,
            key_path=Config.SSH_KEY_PATH,
        )

    def chat(self, user_prompt):

        # Store user message
        self.memory.add("user", user_prompt)
        self.logger.log("USER", user_prompt)

        # Detect intent
        intent = self.classifier.classify(user_prompt)

        print(f"\nDetected Intent : {intent['intent']}")

        # ==========================================================
        # KNOWLEDGE MODE
        # ==========================================================

        if intent["intent"] == "knowledge":

            history = self.memory.format_history()

            prompt = f"""
You are a Senior Linux Administrator.

Conversation History:

{history}

Current User Request:

{user_prompt}

Answer professionally.
"""

            reply = self.llm.ask(prompt)

            self.memory.add("assistant", reply)
            self.logger.log("ASSISTANT", reply)

            return reply

        # ==========================================================
        # DIAGNOSTIC MODE
        # ==========================================================

        elif intent["intent"] == "diagnostic":

            permission = input(
                "\nAgent wants to connect to your Linux VM.\nAllow? (yes/no): "
            )

            if permission.lower() != "yes":
                return "Operation cancelled."

            plan = self.planner.select_tools(user_prompt)

            print(f"\nExecution Plan : {plan}")

            outputs = ""

            for tool in plan["tools"]:

                if tool not in TOOLS:
                    continue

                command = TOOLS[tool]["command"]

                print(f"\nExecuting : {command}")
                self.logger.log("COMMAND", command)

                result, error = self.ssh.execute_command(command)

                outputs += f"""
================================================

Tool:
{tool}

Command:
{command}

Output:
{result}

Error:
{error}

"""

            history = self.memory.format_history()

            analysis_prompt = f"""
You are a Senior Linux Administrator.

Conversation History:

{history}

User Request:

{user_prompt}

Linux Outputs:

{outputs}

Analyze everything carefully.

Provide:

1. Overall Health
2. Problems Found
3. Root Cause
4. Recommendations
5. Next Commands to Execute (if required)
"""

            reply = self.llm.ask(analysis_prompt)

            self.memory.add("assistant", reply)
            self.logger.log("ASSISTANT", reply)

            return reply

        # ==========================================================
        # ACTION MODE
        # ==========================================================

        elif intent["intent"] == "action":

            action = self.action_engine.generate_commands(user_prompt)

            safe, bad_command = self.safety.validate(action["commands"])

            if not safe:

                self.logger.log("BLOCKED", bad_command)

                return f"""
Execution Blocked.

Dangerous command detected:

{bad_command}
"""

            print("\nGenerated Commands:\n")

            for cmd in action["commands"]:
                print(cmd)

            permission = input(
                "\nExecute these commands? (yes/no): "
            )

            if permission.lower() != "yes":
                return "Execution cancelled."

            outputs = ""

            for cmd in action["commands"]:

                print(f"\nExecuting : {cmd}")

                self.logger.log("COMMAND", cmd)

                result, error = self.ssh.execute_command(cmd)

                outputs += f"""
===============================================

Command:
{cmd}

Output:
{result}

Error:
{error}

"""

            history = self.memory.format_history()

            analysis_prompt = f"""
You are a Senior Linux Administrator.

Conversation History:

{history}

The following commands were executed.

{outputs}

Summarize:

1. Success or Failure
2. Any Errors
3. Recommendations
"""

            reply = self.llm.ask(analysis_prompt)

            self.memory.add("assistant", reply)
            self.logger.log("ASSISTANT", reply)

            return reply

        # ==========================================================
        # UNKNOWN
        # ==========================================================

        else:

            return "Sorry, I couldn't understand the request."