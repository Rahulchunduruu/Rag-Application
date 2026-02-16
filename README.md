# RAG Application

A production-ready Retrieval-Augmented Generation (RAG) system built with LangChain for intelligent document-based question answering.

## Overview

This RAG application enables you to query your documents using natural language. It processes documents, creates vector embeddings, stores them in a FAISS vector database, and uses an LLM to generate accurate answers based on retrieved context.

## Features

- 📄 Multi-format document loading (PDF, TXT, HTML)
- ✂️ Intelligent text chunking with overlap
- 🔢 Vector embeddings using OpenAI
- 🗄️ FAISS vector store for fast similarity search
- 🤖 LLM-powered answer generation
- 💬 Interactive query interface
- 💾 Persistent vector store

## Project Structure

```
Rag/
├── app/
│   └── main.py              # Application entry point
├── Chains/
│   └── rag_chain.py         # RAG pipeline logic
├── data/                    # Your documents (PDF, TXT)
├── generation/
│   ├── llm.py              # LLM configuration
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
cd d:\intellipaat\Rag
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Create/edit `.env` file:
```
open_ai_api=your_openai_api_key
grok_api=your_grok_api_key
hugging_face_api=your_huggingface_api_key
```

4. **Add your documents**

Place PDF, TXT, or HTML files in the `data/` folder.

## Usage

### Run the application

```bash
cd app
python main.py
```

The application will:
1. Load documents from the data folder
2. Create/load vector store
3. Prompt you for a query
4. Return an AI-generated answer based on your documents

### Example

```
Enter your query here: What is cricket?
```

Output: AI-generated answer based on your documents.

## How It Works

1. **Document Ingestion**: Documents are loaded and split into chunks
2. **Embedding**: Text chunks are converted to vector embeddings
3. **Storage**: Embeddings are stored in FAISS vector database
4. **Retrieval**: Relevant chunks are retrieved based on query similarity
5. **Generation**: LLM generates answer using retrieved context

## Configuration

Edit `Config.py` to customize:
- API keys
- Model selection
- Vector store paths
- Other settings

## Components

| Component | Description |
|-----------|-------------|
| **Loader** | Loads PDF, TXT, HTML documents |
| **Splitter** | Splits documents into chunks (1000 chars, 200 overlap) |
| **Embedder** | Creates vector embeddings using OpenAI |
| **Vector Store** | FAISS for similarity search |
| **Retriever** | Fetches top-k relevant documents |
| **LLM** | GPT-4o-mini for answer generation |
| **Chain** | Combines all components into RAG pipeline |

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls

## Troubleshooting

**Issue**: `ModuleNotFoundError`
- Solution: Run from the correct directory or check sys.path

**Issue**: `OPENAI_API_KEY not found`
- Solution: Ensure `.env` file exists with correct variable names

**Issue**: Vector store not found
- Solution: Delete `saved_vector_store.pkl` folder and re-run

## License

MIT License
