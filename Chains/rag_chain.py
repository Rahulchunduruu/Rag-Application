from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def format_doc(docs):
    """Format the documents"""
    docs = [doc[0] if isinstance(doc, tuple) else doc for doc in docs] if isinstance(docs, list) and len(docs) > 0 and isinstance(docs[0], tuple) else docs
    return "\n".join(doc.page_content for doc in docs)

def create_rag_pipeline(retriever, prompt, llm):

    rag_chain=(
        {
        "context":retriever | format_doc,
        "question":RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
        )
    
    return rag_chain
