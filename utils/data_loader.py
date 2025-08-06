import json
from langchain.schema import Document

def load_documents_from_json(json_path):
    """
    Loads a JSON dataset of intents and patterns and returns a list of LangChain Document objects.

    Parameters:
        json_path (str): Path to the Uni_Dataset.json file

    Returns:
        List[Document]: List of LangChain documents with question-answer pairs
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    for intent_data in data["intents"]:
        intent = intent_data.get("intent", "unknown")
        response = " ".join(intent_data.get("responses", []))

        for pattern in intent_data.get("text", []):
            content = f"Q: {pattern}\nA: {response}"
            documents.append(Document(page_content=content, metadata={"intent": intent}))

    return documents

Add data loader utility
