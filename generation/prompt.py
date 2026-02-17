from langchain_core.prompts import PromptTemplate


def get_prompt():
    """"
        create a prompt template for question answering.
    """
    print("Creating prompt template...")
    prompt=PromptTemplate(input_variables=["context","question"],
                          template="""Answer the question based on the context below.

                          Context: {context}

                          Question: {question}

                          Instructions:
                          - Answer based only on the provided context and you are allowed to paraphase it but don't change the original meaning
                          - Use **bold text** for important terms, names, and key points
                          - Use **bold headings** to organize information
                          - If the answer cannot be found in the context, respond with "I don't know"
                          - Do not make up information

                          Note:Convert all headings in this text to normal paragraph text. 
                              Remove heading formatting and display the content as regular body text without any special styling or emphasis.
                          
                          Answer:
                          """)

    return prompt
