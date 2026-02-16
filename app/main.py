import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generation.llm import get_llm
from generation.prompt import get_prompt
from retrieval.retriever import get_retriever
from Chains.rag_chain import create_rag_pipeline
from retrieval.vector_store import load_vector_store,create_vector_store    
from ingest_documents import ingest_documents
from ingestion.embedder import get_embeddings
from Config import config
import os

#creating a vector store from documents and saving it to disk
path='../saved_vector_store.pkl'

paths=r'D:\intellipaat\Rag\data\1_Cricket.txt'
chunks,embeddings=ingest_documents(path=paths)
vector_store=create_vector_store(chunks,embeddings,path)

llm = get_llm()
prompt = get_prompt()
vector_store = load_vector_store(path, get_embeddings())
retriever = get_retriever(vector_store)

rag_chain = create_rag_pipeline(retriever, prompt, llm)
input_query = input("Enter your query here: ")
response = rag_chain.invoke(input_query)

print(response)

