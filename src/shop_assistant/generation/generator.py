from openai import OpenAI
import os


class Generator:
    def __init__(self, model: str = "gemma4:e4b-it-qat"):
        self.model = model

        self.client = OpenAI(
            # base_url="http://localhost:11434/v1",
            # api_key="ollama",  # dummy value
            base_url="https://api.gapgpt.app/v1",
            api_key=os.environ["OPENAI_API_KEY"],
        )

    def answer(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model, messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
