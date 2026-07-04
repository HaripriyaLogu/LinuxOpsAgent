from app.action_engine import ActionEngine
from app.safety import SafetyEngine
from app.ssh_client import LinuxSSHClient
from app.config import Config
from app.llm import LLMClient

action_engine = ActionEngine()
safety = SafetyEngine()
llm = LLMClient()

ssh = LinuxSSHClient(
    host=Config.VM_HOST,
    username=Config.VM_USERNAME,
    key_path=Config.SSH_KEY_PATH
)


def action_node(state):

    print("\nAction Node Started...")

    action = action_engine.generate_commands(state["user_prompt"])

    safe, bad_command = safety.validate(action["commands"])

    if not safe:
        return {
            "response": f"Execution Blocked.\nDangerous command detected:\n{bad_command}"
        }

    print("\nGenerated Commands:\n")

    for cmd in action["commands"]:
        print(cmd)

    permission = input(
        "\nExecute these commands? (yes/no): "
    )

    if permission.lower() != "yes":
        return {
            "response": "Execution cancelled."
        }

    outputs = ""

    for cmd in action["commands"]:

        print(f"\nExecuting : {cmd}")

        result, error = ssh.execute_command(cmd)

        outputs += f"""

Command:
{cmd}

Output:
{result}

Error:
{error}

"""

    prompt = f"""
You are a Senior Linux Administrator.

The following commands were executed.

{outputs}

Summarize:

1. Success or Failure
2. Errors
3. Recommendation
"""

    reply = llm.ask(prompt)

    return {
        "response": reply
    }