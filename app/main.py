import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generation.llm import get_llm
from generation.prompt import get_prompt
from retrieval.retriever import get_retriever
from Chains.rag_chain import create_rag_pipeline
from retrieval.vector_store import load_vector_store,create_vector_store,file_exists_in_db    
from ingest_documents import ingest_documents
from ingestion.embedder import get_embeddings
from Config import config


#creating a vector store from documents and saving it to disk

#userinput=r'https://en.wikipedia.org/wiki/Andhra_Pradesh'
#userinput=r'D:\intellipaat\Rag\data'

def start_rag_system(userinput):
    path='../saved_vector_store.pkl'    
    if os.path.exists(path):
        vector_store = load_vector_store(path, get_embeddings())
        if not file_exists_in_db(vector_store,os.path.basename(userinput)):
            chunks,embeddings=ingest_documents(path=userinput)
            vector_store=create_vector_store(chunks,embeddings,path)
        else:
            print("File is already exist in data base")
    else:
        chunks,embeddings=ingest_documents(path=userinput)
        vector_store=create_vector_store(chunks,embeddings,path)

    llm = get_llm()
    prompt = get_prompt()
    vector_store = load_vector_store(path, get_embeddings())
    retriever = get_retriever(vector_store,k=3)

    rag_chain = create_rag_pipeline(retriever, prompt, llm)
    return rag_chain

if __name__ == "__main__":
    userinput=r'D:\intellipaat\Rag\data\chandrababu_naidu_lifestyle_family.txt'
    
    rag_chain = start_rag_system(userinput)
    
    print("=" * 50)
    print("Welcome to the RAG Query Interface")
    print("=" * 50)
    print("\nType 'quit' or 'exit' to close the program.\n")
        
    while True:
            try:
                user_query = input("📝 Enter your query: ").strip()
                
                # Check for exit commands
                if user_query.lower() in {"quit", "exit"}:
                    print("\n👋 Thank you for using the RAG interface. Goodbye!\n")
                    break
                
                # Skip empty inputs
                if not user_query:
                    print("⚠️  Please enter a valid query.\n")
                    continue
                
                # Process the query
                print("\n🔍 Processing your query...\n")
                response = rag_chain.invoke(user_query)
                print(f"📋 Response:\n{response}\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Program interrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"❌ Error: {e}\n")
