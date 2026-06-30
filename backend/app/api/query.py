from fastapi import APIRouter

from pydantic import BaseModel

from app.embeddings.encoder import (
    generate_embeddings
)

from app.vectorstore.qdrant_store import (
    search_chunks
)

from app.llm.groq_client import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    doc_category: str | None = None

@router.post("/query")
def query_documents(
    request : QueryRequest
):
    query_vector = generate_embeddings(
        [request.question]
    )[0]

    results = search_chunks (
        query_vector,
        request.doc_category
    )

    matches = []
    context = []

    if not results:
        return {
            "question": request.question,
            "answer": "No relevant information was found in the selected documents.",
            "matches": []
        }

    for result in results :

        matches.append({
            "score": result.score,

            "filename": 
            result.payload["filename"],

            "chunk_id":
            result.payload["chunk_id"],

            "text":
            result.payload["text"][:300],

            "doc_category":
            result.payload["doc_category"]
        })

        context.append(
    (
        f"Source: {result.payload['filename']}\n"
        f"Category: {result.payload['doc_category']}\n"
        f"Chunk: {result.payload['chunk_id']}\n\n"
        f"{result.payload['text']}\n\n"
        "----------------------------------------"
    )
    )
    context = "\n\n".join(context)

    answer = generate_answer(
    request.question,
    context
    )
    return {
        "question": request.question,
        "answer": answer,
        "matches": matches
    }