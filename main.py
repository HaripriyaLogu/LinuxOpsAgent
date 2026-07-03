from app.agent import LinuxOpsAgent

agent = LinuxOpsAgent()

print("=" * 60)
print("CloudOps AI Assistant")
print("=" * 60)

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        break

    reply = agent.chat(user)

    print("\nAgent:\n")

    print(reply)