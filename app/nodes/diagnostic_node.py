from app.planner import Planner
from app.tools import TOOLS
from app.ssh_client import LinuxSSHClient
from app.config import Config
from app.llm import LLMClient

planner = Planner()
llm = LLMClient()

ssh = LinuxSSHClient(
    host=Config.VM_HOST,
    username=Config.VM_USERNAME,
    key_path=Config.SSH_KEY_PATH
)


def diagnostic_node(state):

    print("\nDiagnostic Node Started...")

    permission = input(
        "\nAgent wants to connect to your Linux VM. Allow? (yes/no): "
    )

    if permission.lower() != "yes":
        return {
            "response": "Operation cancelled."
        }

    plan = planner.select_tools(state["user_prompt"])

    outputs = ""

    for tool in plan["tools"]:

        if tool not in TOOLS:
            continue

        command = TOOLS[tool]["command"]

        print(f"\nExecuting : {command}")

        result, error = ssh.execute_command(command)

        outputs += f"""

Tool:
{tool}

Command:
{command}

Output:
{result}

Error:
{error}

"""

    prompt = f"""
You are a Senior Linux Administrator.

User Request:

{state["user_prompt"]}

Linux Outputs:

{outputs}

Provide:

1. Overall Health
2. Problems Found
3. Root Cause
4. Recommendation
"""

    reply = llm.ask(prompt)

    return {
        "response": reply
    }