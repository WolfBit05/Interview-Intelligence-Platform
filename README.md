# Interview Intelligence Platform | AI-Powered RAG Document Question Answering System

An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to upload documents and ask natural language questions. The system retrieves semantically relevant document chunks using vector search and generates grounded answers using an LLM.

## Features

- Upload PDF and DOCX documents
- Automatic document chunking
- Semantic embeddings generation
- Vector storage with Qdrant
- Metadata-based document filtering
- Semantic document retrieval
- LLM-powered answer generation using Groq
- FastAPI REST API with Swagger UI

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- Qdrant Vector Database
- Groq API (Llama 3.1 8B Instant)
- PyTorch
- Pydantic

## Project Workflow

```
Upload Document
        ↓
Chunking
        ↓
Embedding Generation
        ↓
Store in Qdrant
        ↓
User Query
        ↓
Semantic Retrieval
        ↓
Context Construction
        ↓
Groq LLM
        ↓
Grounded Answer
```

## API Endpoints

### Upload Document

```
POST /upload
```

Uploads and indexes a document into the vector database.

### Query Documents

```
POST /query
```

Retrieves relevant document chunks and generates an AI-powered answer.

## Future Improvements

- Conversation memory
- Source citations
- Multi-document querying
- Hybrid search (Keyword + Vector)
- Authentication
- Frontend interface

## Author

**Gopalakrishna S Chinta**
