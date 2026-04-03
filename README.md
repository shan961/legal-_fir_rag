# ⚖️ AI Legal RAG System (FastAPI + Gemini + Pinecone)

An AI-powered Legal Assistant that allows users to upload FIR / legal PDFs and ask natural language questions.  
The system retrieves relevant context using **Pinecone vector database** and generates accurate answers using **Google Gemini AI**.

---

## 🚀 Features

- 📄 PDF Upload (FIR / legal documents)
- ✂️ Automatic text extraction & chunking
- 🔍 Semantic search using Pinecone (Vector DB)
- 🧠 AI-powered answers using Google Gemini
- 🌐 REST API using FastAPI
- 📦 Clean structured responses (Stolen item, brand, model, etc.)

---

## 🏗️ Tech Stack

- **Backend:** FastAPI
- **LLM:** Google Gemini (gemini-1.5-flash)
- **Vector DB:** Pinecone
- **Embeddings:** Custom embedding model
- **PDF Processing:** PyPDF
- **Language:** Python 3.10+
- 
legal_rag/
│
├── app/
│ ├── api/
│ │ └── routes.py
│ ├── services/
│ │ ├── ingestion.py
│ │ ├── retriever.py
│ │ ├── generator.py
│ │ └── embedder.py
│ ├── db/
│ │ └── pinecone_client.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md


## 📁 Project Str
