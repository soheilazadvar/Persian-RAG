from llama_index.llms.openai import OpenAI

# Initialize Language Model (LLM)
def initialize_llm(api_key, model, api_base, system_prompt, temperature=0.2):
    return OpenAI(api_key=api_key, model=model, api_base=api_base, system_prompt=system_prompt, temperature=temperature)
