# Campusbot-chatbot
An AI-powered chatbot designed to assist  students by providing instant answers to frequently asked questions related to academics, tuition, health services, and immigration all in one centralized platform.

###  Project Objectives

- Provide instant answers to frequently asked questions for international students
- Build a light-weight, locally hosted chatbot with no paid APIs
- Enable web-based and terminal-based interaction
- Store embeddings in ChromaDB for fast vector search
  
### Features

It uses **Retrieval-Augmented Generation (RAG)** architecture with:
-  A local JSON dataset of university FAQs
-  SentenceTransformer-based embeddings
-  ChromaDB for semantic search
-  A minimal **CLI** and **Streamlit UI**

###  Project Directory Structure
```

faq-chatbot/
├── uni_dataset.json # JSON dataset of university FAQs
├── utils/
│ ├── embedder.py # Load model & generate embeddings
│ └── data_loader.py # Load dataset and convert to LangChain Documents
├── store_embeddings.py # Converts FAQs to vectors and stores in ChromaDB
├── query_bot.py # CLI interface to chat with the bot
├── chat_ui.py # Streamlit UI for the chatbot
├── chroma_store/ # Folder storing ChromaDB vector index
├── requirements.txt # Python dependencies
└── README.md
```

##  How to Run

```bash
###  Step 1: Install dependencies
pip install -r requirements.txt

### Step 2:Store embeddings in ChromaDB
python store_embeddings.py

### Step 3: Run the chatbot in CLI
python query_bot.py

### Step 4:(Optional) Run the Streamlit web UI
streamlit run chat_ui.py

```

###  Tech Stack

- **Python 3.11** – Core language used to build the chatbot  
- **LangChain** – Framework for building LLM-powered applications  
- **ChromaDB** – Vector database used for storing and querying embeddings  
- **SentenceTransformers** – Used to generate semantic embeddings from user queries and documents  
- **Streamlit** – Lightweight web framework for building the chatbot UI  
- **JSON** – Custom dataset format for storing university FAQs  


###  Sample Queries

- "What is OPT?"
- "How much are the university fees?"
- "Tell me about CPT rules"
- "List of courses offered"
- "Hi" or "Hello"

### Author
Nimisha Menat
Email: nimishamenat@gmail.com

### License
MIT License – free to use and modify!
