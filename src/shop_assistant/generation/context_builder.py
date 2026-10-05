class ContextBuilder:

    def __init__(self, retrieved_documents: list[str]):
        self.retrieved_documents = retrieved_documents

    def build(self: str) -> str:
        return "\n".join(
            retrieved_document["text"]
            for retrieved_document in self.retrieved_documents
        )
