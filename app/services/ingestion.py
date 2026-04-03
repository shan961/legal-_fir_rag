from pypdf import PdfReader
from app.services.embedder import get_embedding
from app.db.pinecone_client import index
import uuid
import io
import re


# 1. Clean text (VERY IMPORTANT)
def clean_text(text: str):
    text = re.sub(r'\s+', ' ', text)          # remove extra spaces/newlines
    text = re.sub(r'[\u0900-\u097F]+', '', text)  # remove Hindi (optional)
    return text.strip()


# 2. Extract text
def extract_text_from_bytes(file_bytes):
    pdf = PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return clean_text(text)


# 3. Better semantic chunking (NOT raw slicing)
def chunk_text(text, chunk_size=800, overlap=100):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])

        chunk = clean_text(chunk)

        if len(chunk) > 50:   # ignore tiny/noisy chunks
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# 4. Main ingestion
def process_pdf_file(file_bytes):
    print("📄 Extracting text...")
    text = extract_text_from_bytes(file_bytes)

    print("✂️ Creating clean chunks...")
    chunks = chunk_text(text)

    vectors = []

    print(f"📦 Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)

        # skip empty embeddings
        if not chunk or len(chunk) < 50:
            continue

        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embedding,
            "metadata": {
                "text": chunk
            }
        })

        print(f"✅ Chunk {i+1}/{len(chunks)} processed")

    print("📤 Uploading to Pinecone...")
    index.upsert(vectors=vectors)

    print("🎉 Done!")

    return {
        "chunks_created": len(chunks),
        "vectors_uploaded": len(vectors)
    }