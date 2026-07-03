from app.langgraph_agent import app

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        break

    result = app.invoke(
        {
            "user_prompt": user
        }
    )

    print("\nAgent:\n")
    print(result.get("response"))