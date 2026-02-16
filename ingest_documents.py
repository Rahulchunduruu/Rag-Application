from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from ingestion.embedder import get_embeddings
from retrieval.vector_store import create_vector_store,load_vector_store
from Config import config

def ingest_documents(path):
    """
        Ingest documents by loading, splitting and embedding them.
    """
    documents=load_documents(path)
    chunks=split_documents(documents)
    embeddings=get_embeddings()
    return chunks,embeddings


if __name__=="__main__":
    path=r'https://en.wikipedia.org/wiki/Telangana'
    chunks,embeddings=ingest_documents(path=path)
    print(chunks[10].page_content,chunks[10].metadata)
    