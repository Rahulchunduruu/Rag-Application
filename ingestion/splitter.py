from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
        Split documents into smaller chunks.
    """
    spliter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=150)

    chunks=spliter.split_documents(documents)

    return chunks

if __name__=="__main__":
    documents=[{"page_content":"This is a sample document. "
    "It contains some text that needs to be split into smaller chunks."
    " The text splitter will take care of splitting the document into manageable pieces that can be processed by the language model. "
    "This is especially useful when dealing with large documents that exceed the token limit of the model. By splitting the document,"
    " we can ensure that we can process it effectively and get the desired results."}]
    
    print(split_documents(documents[0]["page_content"]))
    