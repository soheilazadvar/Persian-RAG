from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

# Initialize Vector Store and Index
def initialize_vector_index(nodes):
    client = QdrantClient(location=":memory:")
    vector_store = QdrantVectorStore(client=client, collection_name="test")
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    return VectorStoreIndex(nodes, storage_context=storage_context)
