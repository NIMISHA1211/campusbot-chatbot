#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import sys
import os


# In[4]:


# Add the path to your 'utils' folder
sys.path.append(r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot")

from chromadb import PersistentClient
from utils.embedder import load_embedding_model, get_embeddings
from utils.data_loader import load_documents_from_json


# In[5]:


# === Configuration ===
CHROMA_DB_DIR = r"C:\Nimisha docs and Files\Thinkround NGO\Chatbot\gmu-faq-chatbot\chroma_store"

# === Initialize ===
model = load_embedding_model()
client = PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection(name="faq_collection")

# === Streamlit UI ===
st.set_page_config(page_title="University FAQ Chatbot")
st.title("University FAQ Chatbot")

query = st.text_input("💬 Ask me a question about university policies, fees, OPT, CPT, etc:")

if query:
    embedding = get_embeddings(model, [query])[0]
    results = collection.query(query_embeddings=[embedding], n_results=1)

    if results["documents"]:
        response = results["documents"][0][0]
        st.success(f"🤖 {response}")
    else:
        st.warning("Sorry, I don't have an answer for that.")

