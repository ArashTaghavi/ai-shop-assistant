class ChatHistory:
    def __init__(self):
        self.messages: list[str] = []

    def _add_message(self, message: str, role: str):
        self.messages.append({"role": role, "content": message})

    def add_user_message(self, message: str):
        self._add_message(role="user", message=message)

    def add_ai_message(self, message: str):
        self._add_message(role="assistant", message=message)

    def get_messages(self, for_history=False):
        if for_history:
            return "\n".join(
                [
                    f"{message['role']}: {message['content']}"
                    for message in self.messages
                ]
            )

    def clear(self):
        self.messages = []
