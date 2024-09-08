from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Initialize HuggingFace Embeddings
def initialize_embeddings(model_path):
    return HuggingFaceEmbedding(model_name=model_path)
