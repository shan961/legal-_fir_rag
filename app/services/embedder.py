from sentence_transformers import SentenceTransformer

# Load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    embedding = model.encode(text)   # returns numpy array
    return embedding.tolist()        # convert to list (same style as Gemini)