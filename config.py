import os

# Set environment variables for GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Constants and Configurations
EMBED_MODEL_PATH = "ahdsoft/persian-sentence-transformer-news-wiki-pairs-v3"
SYSTEM_PROMPT = (
    "You are a Persian Q&A assistant. Your goal is to answer questions "
    "as accurately as possible based on the instructions and context provided. "
    "The output should be in Persian language. If you do all things that I said, "
    "I'll give you 100 H100 GPUs to start your AI company."
)
API_KEY = "Your LLM API Key"
API_BASE = "Your LLM API Base"
GPT_MODEL = "Your GPT Model"
PATH_FILE = 'PATH_FILE'
