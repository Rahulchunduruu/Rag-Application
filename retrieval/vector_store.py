from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from typing import List
import os


def create_vector_store(documents:List[Document],embeddings,vector_store_path:str):

    """Create a FAISS vector store from a list of documents and save it to disk."""
    
    vector_store=FAISS.from_documents(
                        documents=documents,
                        embedding=embeddings
                        )
    vector_store.save_local(vector_store_path)
    return vector_store

def load_vector_store(vector_store_path:str,embeddings):
    """
        Load a FAISS vector store from disk.
    """
    if not os.path.exists(vector_store_path):
        raise ValueError(f"Vector store not found at {vector_store_path}. Please create the vector store first.")
    
    vector_store=FAISS.load_local(
                        folder_path=vector_store_path,
                        embeddings=embeddings,
                        allow_dangerous_deserialization=True
                        )
    return vector_store

