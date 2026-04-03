from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from app.services.retriever import retrieve
from app.services.generator import generate_answer
from app.services.ingestion import process_pdf_file

router = APIRouter()

class Query(BaseModel):
    query: str


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    process_pdf_file(contents)
    return {"message": "uploaded"}


@router.post("/ask")
def ask_question(data: Query):
    docs = retrieve(data.query)
    answer = generate_answer(data.query, docs)

    return {
        "query": data.query,
        "answer": answer,
        "sources": docs
    }