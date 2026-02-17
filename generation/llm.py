from langchain_openai import ChatOpenAI
from Config import config
from pydantic import BaseModel, Field
from typing import Literal,Union

class user_input(BaseModel):
    Topic:  str =   Field(description="The topic to be discussed")
    Summary:str =   Field(description="""Summary of the topic in 7 to 9 lines and if you don't know the answer, " \
                        say you "Based on provided context i don't have information about {Topic}" don't write anything other that .""")
    Conclusion:str= Field(description="Final conclusion on the topic")
    
    def __str__(self):
        return f"\nTopic: {self.Topic}\n\nSummary: {self.Summary}\n\nConclusion: {self.Conclusion}"


def get_llm(temperature:float=0.7, max_tokens:int=3000):
    """
    Create a language model instance.
    The LLM will choose between NoAnswerResponse or AnswerResponse based on context.
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=config.OPENAI_API_KEY,
    )
                  
    
    return llm.with_structured_output(user_input)
