from fastapi import APIRouter
from app.vectorstore.qdrant_store import client, COLLECTION

router = APIRouter()

@router.get("/debug/vectors")
def vector_count():

    result = client.count(
        collection_name=COLLECTION
    )

    return {
        "points": result.count
    }