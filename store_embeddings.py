#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Add the path to your 'utils' folder
import sys

sys.path.append(r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot")


# In[ ]:


import os
from chromadb import PersistentClient
from utils.embedder import load_embedding_model, get_embeddings
from utils.data_loader import load_documents_from_json

# === Configuration ===

DATASET_PATH = r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot\Uni_Dataset.json"
CHROMA_DB_DIR = r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot\chroma_store"

# === Step 1: Load documents ===
print("🔍 Loading documents...")
documents = load_documents_from_json(DATASET_PATH)
texts = [doc.page_content for doc in documents]
metadatas = [doc.metadata for doc in documents]
ids = [f"doc_{i}" for i in range(len(texts))]  # Generate unique IDs

# === Step 2: Load model and generate embeddings ===
print("🧠 Generating embeddings...")
model = load_embedding_model()
embeddings = get_embeddings(model, texts)

# === Step 3: Initialize ChromaDB client ===
print("📦 Storing in ChromaDB...")
chroma_client = PersistentClient(path=CHROMA_DB_DIR)
collection = chroma_client.get_or_create_collection(name="faq_collection")

# === Step 4: Add all data at once (FAST and SAFE) ===
collection.add(
    ids=ids,
    documents=texts,
    embeddings=embeddings,
    metadatas=metadatas
)

# === Step 5: Done! ===
print(f"✅ Stored {len(texts)} documents in ChromaDB at:\n{CHROMA_DB_DIR}")

