from app.services.embedder import get_embedding
from app.db.pinecone_client import index

def retrieve(query):
    query_vector = get_embedding(query)

    results = index.query(
        vector=query_vector,
        top_k=5,
        include_metadata=True
    )

    docs = [match["metadata"]["text"] for match in results["matches"]]
    return docs