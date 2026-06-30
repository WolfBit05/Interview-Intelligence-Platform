from qdrant_client import (
    QdrantClient
)

from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct,

    Filter,
    FieldCondition,
    MatchValue
)

import uuid

client = (
    QdrantClient(
        ":memory:"
    )
)

COLLECTION = (
    "documents"
)


def create_collection():

    collections = (
        client.get_collections()
    )

    names = [
        c.name
        for c
        in collections.collections
    ]

    if COLLECTION not in names:

        client.create_collection(
            collection_name=
            COLLECTION,

            vectors_config=
            VectorParams(
                size=384,
                distance=
                Distance.COSINE
            )
        )


def insert_chunks(
    chunks,
    vectors,
    filename,
    doc_category
):

    points = []

    for i in range(
        len(chunks)
    ):

        points.append(

            PointStruct(
                id=str(uuid.uuid4()),

                vector=
                vectors[i],

                payload={
                    "text":
                    chunks[i],
                    "filename": filename,
                    "chunk_id": i,
                    "doc_category": doc_category
                }
            )
        )

    client.upsert(
        collection_name=
        COLLECTION,

        points=
        points
    )

def search_chunks(
    query_vector,
    doc_category,
    limit=3
):

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=limit,
        with_payload=True,
        query_filter = Filter(
            must=[
                FieldCondition(
                    key = "doc_category",
                    match = MatchValue(
                        value = doc_category
                    )
                )
            ]
        )
    )

    return results.points