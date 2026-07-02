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

## System Architecture

```text
                      User
                       │
                       ▼
                   FastAPI API
                 ┌─────────────┐
                 │             │
                 ▼             ▼
          POST /upload    POST /query
                 │             │
                 ▼             ▼
      Read & Chunk Document   User Question
                 │             │
                 ▼             ▼
     Generate Embeddings   Generate Query Embedding
                 │             │
                 ▼             ▼
          Store in Qdrant ──► Semantic Search
                               │
                               ▼
                     Top-K Relevant Chunks
                               │
                               ▼
                     Context Construction
                               │
                               ▼
                  Groq (Llama 3.1 8B Instant)
                               │
                               ▼
                       Grounded Answer
```

## RAG Pipeline

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

## Screenshots

### API Overview
<img width="1861" height="528" alt="Intelligence System FastAPI-1" src="https://github.com/user-attachments/assets/4ff59a5c-11d0-4f38-8b90-5e713bcc132d" />

### Document Upload
<img width="1790" height="454" alt="Intelligence System File Upload-2" src="https://github.com/user-attachments/assets/2ab88751-08a7-4ace-9012-9bc2de764fb1" />

### Document Upload Response
<img width="1806" height="844" alt="Inteligence System File Upload Success Response-3" src="https://github.com/user-attachments/assets/c52c33e1-e7a3-4926-bdfa-94589f77c420" />

### Querying Documents
<img width="679" height="258" alt="Intelligence System Query-4" src="https://github.com/user-attachments/assets/2ad2336b-22ea-4802-9bac-4e465f5052c6" />

### AI Genrated Query Response
<img width="1641" height="265" alt="Intelligence System Query Response-5" src="https://github.com/user-attachments/assets/45ecc2fc-2ef8-4f84-8e11-0028fc186e25" />

## Future Improvements

- Conversation memory
- Source citations
- Multi-document querying
- Hybrid search (Keyword + Vector)
- Authentication
- Frontend interface

## Author

**Gopalakrishna S Chinta**

MCA Graduate | Aspiring AI/ML Engineer | Python & RAG Developer
