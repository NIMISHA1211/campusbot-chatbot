#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys


# In[ ]:


# Add path to your utils folder
sys.path.append(r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot")

from chromadb import PersistentClient
from utils.embedder import load_embedding_model, get_embeddings

# === Configuration ===
CHROMA_DB_DIR = r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot\chroma_store"

# Load embedding model
model = load_embedding_model()

# Load ChromaDB collection
client = PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection(name="faq_collection")

print("🎓 Welcome to the GMU University FAQ Chatbot")
print("Type 'exit' to quit.\n")

while True:
    query = input("💬 You: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Embed query and search
    embedding = get_embeddings(model, [query])[0]
    results = collection.query(query_embeddings=[embedding], n_results=1)

    answer = results["documents"][0][0]
    print(f"🤖 Bot: {answer}\n")


# In[ ]:




