"""Pre-trained model wrappers for embedding and generation."""

from __future__ import annotations

from typing import List, Union

import numpy as np


class EmbeddingModel:
    """Wrapper around a sentence-transformers embedding model.

    Lazy-loads the model on first use to avoid import-time cost.

    Args:
        model_name: Hugging Face model identifier.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        self.model_name = model_name
        self._model = None

    def _load(self) -> None:
        from sentence_transformers import SentenceTransformer  # type: ignore

        self._model = SentenceTransformer(self.model_name)

    def encode(
        self,
        texts: Union[str, List[str]],
        batch_size: int = 32,
    ) -> np.ndarray:
        """Encode text(s) into dense embedding vectors.

        Args:
            texts: A single string or list of strings.
            batch_size: Batch size for encoding.

        Returns:
            NumPy array of shape (N, embedding_dim).
        """
        if self._model is None:
            self._load()

        if isinstance(texts, str):
            texts = [texts]

        return self._model.encode(texts, batch_size=batch_size, show_progress_bar=False)
