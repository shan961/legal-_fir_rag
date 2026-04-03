from app.services.ingestion import ingest

# Example legal text
text = """
Section 378 IPC: Theft is defined as dishonestly taking any movable property...
Punishment may include imprisonment or fine.
"""

ingest(text)

print("Data uploaded successfully!")