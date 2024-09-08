from llama_index.core import Settings


# Configure LLM and Embeddings
def configure_settings(llm, chunk_size, embed_model):
    Settings.llm = llm
    Settings.chunk_size = chunk_size
    Settings.embed_model = embed_model
