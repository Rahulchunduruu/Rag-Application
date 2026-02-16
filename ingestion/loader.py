import os
from langchain_community.document_loaders import ( PyPDFLoader,
                                                  TextLoader,
                                                  DirectoryLoader,
                                                  WebBaseLoader,
                                                  DirectoryLoader
                                                )

os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def load_documents(data:str):
    """
    Load documents from a directory containing PDF, TXT and HTML files.
    Args:  data (str): The path to the directory containing the documents.
    Returns: list: A list of loaded documents."""
    
    pdf_loader = None
    text_loader = None
    Web_loader = None
    
    if os.path.isdir(data):
        pdf_loader=DirectoryLoader(path=data,
                                glob="*.pdf",
                                loader_cls=PyPDFLoader)
        
        text_loader=DirectoryLoader(path=data,
                                    glob="*.txt",
                                    loader_cls=TextLoader)

        Web_loader=DirectoryLoader(path=data,
                                    glob="*.html",
                                    loader_cls=WebBaseLoader)
    else:
        if data.endswith('.pdf'):
            pdf_loader=PyPDFLoader(data)
        elif data.endswith('.txt'):
            text_loader=TextLoader(data)
        elif data.endswith('.html') or data.startswith('http'):
            Web_loader=WebBaseLoader(data)
        else:
            raise ValueError("Unsupported file format. Please provide a PDF, TXT, or HTML file.")
        
    documents=[]

    if pdf_loader:
        documents.extend(pdf_loader.lazy_load())
    if text_loader:
        documents.extend(text_loader.lazy_load())
    if Web_loader:
        documents.extend(Web_loader.lazy_load())

    return documents

if __name__=="__main__":
    data=r'https://en.wikipedia.org/wiki/Telangana'
    documents=load_documents(data)
    for document in documents:
        print(document.metadata)