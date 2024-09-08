from config import PATH_FILE, SYSTEM_PROMPT, EMBED_MODEL_PATH, API_KEY, GPT_MODEL, API_BASE
from utils.document_loader import load_documents
from utils.embeddings import initialize_embeddings
from utils.llm_initializer import initialize_llm
from utils.vector_store import initialize_vector_index
from utils.query_engine import initialize_query_engine
from utils.node_splitter import create_node_splitter
from utils.setting import configure_settings

def main():
    # Load documents
    documents = load_documents(PATH_FILE)

    # Initialize models
    embed_model = initialize_embeddings(EMBED_MODEL_PATH)
    llm = initialize_llm(API_KEY, GPT_MODEL, API_BASE, SYSTEM_PROMPT)

    # Split documents into nodes
    splitter = create_node_splitter(embed_model)
    nodes = splitter.get_nodes_from_documents(documents=documents)

    # Configure settings
    configure_settings(llm, chunk_size=1024, embed_model=embed_model)

    # Initialize vector index
    vector_index = initialize_vector_index(nodes)

    # Initialize query engine
    query_engine = initialize_query_engine(vector_index)

    # Query processing (replace with your query)
    query_text = ""  # Your query here
    response = query_engine.query(query_text)
    print(str(response.response))

if __name__ == "__main__":
    main()
