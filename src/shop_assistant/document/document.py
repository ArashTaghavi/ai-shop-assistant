from pathlib import Path


class Document:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self, clean: bool = True) -> list[str]:

        path = self._validate()

        documents = path.read_text(encoding="utf-8-sig").splitlines()

        if not any(line.strip() for line in documents):
            raise ValueError(f"No rules found in file: {self.file_path}")

        if not clean:
            return documents

        return self._clean(documents=documents)

    def _clean(self, documents: list[str]) -> list[str]:
        return [line.strip() for line in documents if line.strip()]

    def _validate(self) -> Path:
        file_path = self.file_path

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        if path.suffix.lower() != ".txt":
            raise ValueError("Currently only .txt files are supported.")

        return path
