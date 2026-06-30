from fastapi import (
    APIRouter, 
    UploadFile, File, Form
    )

from pathlib import Path

from app.services.ingestion import (
    DocumentIngestion
)
 

from app.embeddings.encoder import (
    generate_embeddings
)

from app.vectorstore.qdrant_store import (
    create_collection,
    insert_chunks
)

router = APIRouter()

UPLOAD_DIR = "app/uploads"

Path(
    UPLOAD_DIR
    ).mkdir(
    parents = True,
    exist_ok = True
)

ingestor = (
    DocumentIngestion()
)

@router.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        doc_category: str = Form(...)
):
    path = (
        f"{UPLOAD_DIR}/"
        f"{file.filename}"
    )

    with open(
        path,
        "wb"
        ) as buffer:
        
        content = (
            await file.read()
        )
        
        buffer.write(
            content
            )
        
    try:
        text = ingestor.extract_text(path)

    except ValueError as e:
        return {
        "error": str(e)
        }

    chunks = (
        ingestor.chunk_text(
            text
        )
    )

    create_collection()

    vectors = (
    generate_embeddings(
        chunks
        )
    )

    insert_chunks(
        chunks,
        vectors,
        file.filename,
        doc_category
    )

    return {
        "filename": 
        file.filename,

        "chars":
        len(text),

        "num_chunks": 
        len(chunks),

        "vectors":
        len(vectors),

        
        "chunk_preview": [
            c[:150]
            for c in chunks[:3]
        ]
    }