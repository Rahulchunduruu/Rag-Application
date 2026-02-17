from langchain_openai import ChatOpenAI
from Config import config
from pydantic import BaseModel, Field
from typing import Literal,Union

class user_input(BaseModel):
    Topic:  str =   Field(description="The topic to be discussed")
    context : str =   Field(description="The context to be used for generating the response excpeted between 10 to 12 lines and if you don't know about it just metioned i don't have information about {Topic} ")
    Summary:str =   Field(description="""Summary of the topic in 3 to 4 lines lines and if you don't know the answer, " \
                        say you "Based on provided context i don't have information about {Topic}" don't write anything other that .""")
    Conclusion:str= Field(description="Final conclusion on the topic should be one line")
    
    def __str__(self):
        return f"\nTopic: {self.Topic} \n\ncontex: {self.context}\n\nSummary: {self.Summary} \n\nConclusion: {self.Conclusion}"


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
