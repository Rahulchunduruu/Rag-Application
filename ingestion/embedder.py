from langchain_openai import OpenAIEmbeddings
from Config import config

def get_embeddings():
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=config.OPENAI_API_KEY
    )