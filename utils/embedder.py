from sentence_transformers import SentenceTransformer

def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    """
    Loads a sentence transformer model for embeddings.
    """
    return SentenceTransformer(model_name)

def get_embeddings(model, texts):
    """
    Returns embeddings for a list of texts using the given model.

    Parameters:
        model: SentenceTransformer model
        texts (List[str]): List of text strings to embed

    Returns:
        List[List[float]]: List of embedding vectors
    """
    return model.encode(texts, convert_to_numpy=True)


Add embedder utility
