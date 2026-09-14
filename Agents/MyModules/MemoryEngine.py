
import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"
import logging
logging.disable(logging.CRITICAL)

import chromadb
import ollama



class OllamaEmbeddingFunction:

    def __init__(self, model="nomic-embed-text"):
        self.model = model

    def __call__(self, input):

        response = ollama.embed(
            model=self.model,
            input=input
        )

        return response["embeddings"]


class MemoryEngine:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.embed_fn = OllamaEmbeddingFunction()

        self.collection = self.client.get_or_create_collection(
            name="Agent_Memory",
            embedding_function = self.embed_fn
        )

    def save_memory(self,text):
        import hashlib
        doc_id = hashlib.md5(text.encode()).hexdigest()

        self.collection.add(
            documents=[text],
            ids=[doc_id]
        )
        return "Memory Saved"

    def recall_memory(self, query, n_results=4):

        result = self.collection.query(
            query_texts=[query],
            n_results=n_results,
        )

        if result["documents"]:
            retrive_doc =result["documents"][0]
            if retrive_doc:
                context ="\nDATABASE\n"+"\n".join(retrive_doc)
                return context
        return[]
