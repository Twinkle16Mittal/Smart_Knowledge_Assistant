import requests, os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
API_URL = os.getenv("API_URL", "http://localhost:8000")

def upload_documents(file, owner="default_user"):
    files = {
        "file": (file.name, file.getvalue(), file.type or "application/octet-stream")
    }
    data = {"owner": owner}
    res = None
    try:
        res = requests.post(f"{API_URL}/upload/", files=files, data=data)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Request Failed: {e}")
        if res is not None:
            st.text(f"Response content:\n{res.text}")
        else:
            st.text("No response received from API.")
        return None

def query_documents(query) -> dict:
    """
    calling query calling for documnets
    """
    return requests.post(f"{API_URL}/query/", json={"query": query}).json()

def list_documents() -> dict:
    """
    list all the documents
    """
    return requests.get(f"{API_URL}/docs/").json().get("documents", [])



