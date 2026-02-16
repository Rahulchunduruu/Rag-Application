from langchain_core.prompts import PromptTemplate


def get_prompt():
    """"
        create a prompt template for question answering.
    """
    print("Creating prompt template...")
    prompt=PromptTemplate(input_variables=["context","question"],
                          template="""Answer the question based on the context below.\n\n
                          Context: {context}\n\n
                          Question: {question}\n\n
                          Answer:you must answer the question based on the context provided.amd if needed paraphrase the context to answer the question you are allowed to do it.
                          Note:If the question cannot be answered based on the context, say I don't know
                          and don't make up an answer.
                          """)

    return prompt
