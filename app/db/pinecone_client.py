from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("❌ PINECONE_API_KEY not found in .env")

pc = Pinecone(api_key=api_key)

index_name = "legal"

existing_indexes = [i["name"] for i in pc.list_indexes()]

# Create index if not exists
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,   # ✅ FIXED (MiniLM embedding size)
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print(f"✅ Index '{index_name}' created")

index = pc.Index(index_name)

print("✅ Pinecone connected successfully!")