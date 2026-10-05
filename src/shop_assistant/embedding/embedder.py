import numpy as np
from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    ) -> None:
        self.model = SentenceTransformer(model_name_or_path=model_name)

    def embed(
        self,
        texts: list[str],
        *,
        normalize_embeddings: bool = True,
    ) -> np.ndarray:
        """Return one embedding per text, preserving input order."""

        return self.model.encode(
            inputs=texts,
            convert_to_numpy=True,
            normalize_embeddings=normalize_embeddings,
        )
