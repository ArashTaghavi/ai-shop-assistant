class ChatHistory:
    def __init__(
        self,
        summarizer,
        max_messages: int = 10,
        keep_recent: int = 4,
    ):
        self.messages = []
        self.summary = ""
        self.summarizer = summarizer
        self.max_messages = max_messages
        self.keep_recent = keep_recent

    def _add_message(self, message: str, role: str):
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )

    def add_user_message(self, message: str):
        self._add_message(message, "user")

    def add_ai_message(self, message: str):
        self._add_message(message, "assistant")
        self._summarize_if_needed()

    def _summarize_if_needed(self):
        if len(self.messages) <= self.max_messages:
            return

        old_messages = self.messages[: -self.keep_recent]

        self.summary = self.summarizer.summarize(
            messages=old_messages,
            previous_summary=self.summary,
        )

        self.messages = self.messages[-self.keep_recent :]

    def get_messages(self, for_history=False):
        if not for_history:
            return self.messages

        recent_history = "\n".join(
            f"{message['role']}: {message['content']}" for message in self.messages
        )

        return f"""
[خلاصه مکالمات قبلی]:
{self.summary}

[مکالمات اخیر]:
{recent_history}
""".strip()

    def clear(self):
        self.messages = []
        self.summary = ""
