from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.debug import router as debug_router
from app.api.query import (
    router as query_router
)

app = FastAPI(
    title = "Interview Intelligence API"
)

app.include_router(debug_router)

app.include_router(
    upload_router
)

app.include_router(
    query_router
)

@app.get("/")
def root():
    return {
        "message": "Interview Intelligence API running"
    }
