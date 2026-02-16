from langchain_core.retrievers import BaseRetriever


def get_retriever(vector_store,k:int=5):

    """
        Create a retriever from a vector store.
    """
    
    retriever=vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":k,
                       "lambda_mult": 0.6},
       )
    return retriever

