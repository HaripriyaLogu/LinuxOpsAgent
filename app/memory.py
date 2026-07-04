class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append(
            {
                "role": role,
                "content": content
            }
        )

    def get_history(self):
        return self.history

    def format_history(self):

        conversation = ""

        for message in self.history:

            conversation += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        return conversation

    def clear(self):
        self.history = []