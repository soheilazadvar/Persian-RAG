
# Persian Retrieval-Augmented Generation (RAG) with LlamaIndex

This project implements a **Retrieval-Augmented Generation (RAG)** system specifically for the **Persian language**, leveraging the **LlamaIndex** library. It combines a state-of-the-art Persian language model with a highly optimized retrieval mechanism, making it one of the most effective solutions for Persian question-answering tasks.

## Key Features

- **Persian Language Focus**: The system is built to handle Persian queries and provide accurate answers using Persian text documents.
- **Best-in-Class Persian Embeddings**: The embedding model used in this project is among the best available for Persian, ensuring that the semantic representation of text is highly accurate.
- **LlamaIndex Integration**: The project is powered by the **LlamaIndex** library, which enables efficient vector storage, retrieval, and query processing.
  
## Project Structure

- **Embedding**: The code utilizes the `HuggingFaceEmbedding` class to load and use a high-quality Persian sentence transformer model (`ahdsoft/persian-sentence-transformer-news-wiki-pairs-v3`) for generating document embeddings.
- **Vector Storage**: Documents are stored in memory and indexed using a vector store powered by **Qdrant**. This allows for fast retrieval based on semantic similarity.
- **Query Processing**: The project uses `RouterQueryEngine` to process user queries and return the most relevant information from the retrieved documents.
- **Split and Indexing**: The document split strategy leverages a `SemanticSplitterNodeParser` to create well-defined chunks of information for effective retrieval.
  
## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sinaaasghari/Persian-RAG.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

- The system takes a Persian query as input and retrieves the most relevant context from the document corpus. It then generates an accurate answer using the underlying GPT model.
  
- The model is integrated with **OpenAI's GPT-4**, using a custom API for Persian-specific instruction tuning.

## Future Improvements

- Add more Persian language datasets to further improve the embedding model performance.
- Optimize the retrieval mechanism for larger document collections.
