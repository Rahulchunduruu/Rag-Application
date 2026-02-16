from langchain_openai import ChatOpenAI
from Config import config

def get_llm(temperature:float=0.7,max_tokens:int=3000):
    """
        Create a language model instance.
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=config.OPENAI_API_KEY,
    )

    return llm