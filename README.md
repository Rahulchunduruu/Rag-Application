# RAG Application

A production-ready Retrieval-Augmented Generation (RAG) system built with LangChain for intelligent document-based question answering.

## Overview

This RAG application enables you to query your documents using natural language. It processes documents, creates vector embeddings, stores them in a FAISS vector database, and uses an LLM to generate accurate answers based on retrieved context.

## Features

- 📄 Multi-format document loading (PDF, TXT, HTML, DOCX)
- ✂️ Intelligent text chunking with overlap
- 🔢 Vector embeddings using OpenAI
- 🗄️ FAISS vector store for fast similarity search
- 🤖 LLM-powered answer generation with structured output
- 💬 Interactive CLI and Web UI (Streamlit)
- 💾 Persistent vector store
- 📤 Multi-file upload support
- 🔄 Dynamic document management

## Project Structure

```
Rag/
├── app/
│   ├── main.py              # CLI application entry point
│   └── app.py               # Streamlit web interface
├── Chains/
│   └── rag_chain.py         # RAG pipeline logic
├── data/                    # Your documents (PDF, TXT)
├── generation/
│   ├── llm.py              # LLM configuration with structured output
│   └── prompt.py           # Prompt templates
├── ingestion/
│   ├── loader.py           # Document loaders
│   ├── splitter.py         # Text splitting
│   └── embedder.py         # Embedding generation
├── retrieval/
│   ├── vector_store.py     # FAISS operations
│   └── retriever.py        # Document retrieval
├── Config.py               # Configuration management
├── ingest_documents.py     # Document ingestion script
├── requirements.txt        # Python dependencies
└── .env                    # API keys (not in git)
```

## Installation

1. **Clone the repository**
```bash
cd Rag-Application
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Create/edit `.env` file:
```
open_ai_api=your_openai_api_key
```

4. **Add your documents**

Place PDF, TXT, or HTML files in the `data/` folder.

## Usage

### Option 1: CLI Interface

```bash
cd app
python main.py
```

The application will:
1. Load documents from the data folder
2. Create/load vector store
3. Prompt you for queries in an interactive loop
4. Return AI-generated answers with bold formatting

### Option 2: Web Interface (Streamlit)

```bash
cd app
streamlit run app.py
```

Features:
- Upload multiple documents (PDF, TXT, DOCX)
- Dynamic document management
- Interactive query interface
- Formatted responses with markdown support

### Example

```
Enter your query: What is cricket?
```

Output: Structured AI-generated answer with:
- **Topic**: Main subject
- **Summary**: 7-9 line summary with bold key terms
- **Conclusion**: Final takeaway

## How It Works

1. **Document Ingestion**: Documents are loaded and split into chunks
2. **Embedding**: Text chunks are converted to vector embeddings
3. **Storage**: Embeddings are stored in FAISS vector database
4. **Retrieval**: Relevant chunks are retrieved based on query similarity (top-3)
5. **Generation**: LLM generates structured answer using retrieved context

## Configuration

Edit `Config.py` to customize:
- API keys
- Model selection (GPT-4o-mini)
- Vector store paths
- Temperature and max tokens

## Components

| Component | Description |
|-----------|-------------|
| **Loader** | Loads PDF, TXT, HTML, DOCX documents |
| **Splitter** | Splits documents into chunks (1000 chars, 200 overlap) |
| **Embedder** | Creates vector embeddings using OpenAI (text-embedding-3-small) |
| **Vector Store** | FAISS for similarity search |
| **Retriever** | Fetches top-3 relevant documents |
| **LLM** | GPT-4o-mini with structured output (Topic, Summary, Conclusion) |
| **Chain** | Combines all components into RAG pipeline |
| **Web UI** | Streamlit interface with file upload and session management |

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls
- Streamlit (for web interface)

## Troubleshooting

**Issue**: `ModuleNotFoundError`
- Solution: Run from the correct directory or check sys.path

**Issue**: `OPENAI_API_KEY not found`
- Solution: Ensure `.env` file exists with correct variable names

**Issue**: Vector store not found
- Solution: Delete `saved_vector_store.pkl` folder and re-run

**Issue**: Multiple file upload not working
- Solution: Ensure files are uploaded before clicking Search, check temp directory permissions

## License

MIT License
