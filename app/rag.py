import os

from app.vector_store import VectorStore


class RAG:

    def __init__(self):

        self.vector_db = VectorStore()

    def chunk_text(self, text, chunk_size=500):

        chunks = []

        for i in range(0, len(text), chunk_size):

            chunks.append(text[i:i + chunk_size])

        return chunks

    def ingest_documents(self):

        folder = "knowledge"

        for file in os.listdir(folder):

            if not (file.endswith(".txt") or file.endswith(".pdf")):
                continue

            path = os.path.join(folder, file)

            # ---------- TXT ----------

            if file.endswith(".txt"):

                with open(path, "r", encoding="utf-8") as f:

                    text = f.read()

            # ---------- PDF ----------

            else:

                from pypdf import PdfReader

                reader = PdfReader(path)

                text = ""

                for page in reader.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text + "\n"

            chunks = self.chunk_text(text)

            for index, chunk in enumerate(chunks):

                self.vector_db.add_document(

                    f"{file}_{index}",

                    chunk

                )

        print("Knowledge Base Created.")

    def retrieve(self, question):

        return self.vector_db.search(question)