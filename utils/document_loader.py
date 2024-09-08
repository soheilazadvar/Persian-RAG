from llama_index.core import SimpleDirectoryReader

# Load Documents
def load_documents(file_path):
    return SimpleDirectoryReader(input_files=[file_path]).load_data()
