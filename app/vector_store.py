import os

import chromadb

from sentence_transformers import SentenceTransformer

from chromadb.config import Settings


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.PersistentClient(
            path="database/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="linuxops_docs"
        )

    def add_document(self, doc_id, text):

        embedding = self.model.encode(text).tolist()

        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding]
        )

    def search(self, query, top_k=3):

        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return results["documents"][0]