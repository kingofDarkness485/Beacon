# generator.py
import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    st.secrets["huggingface"]["key1"],
    st.secrets["huggingface"]["key2"],
    st.secrets["huggingface"]["key3"]

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error: {response.status_code} — {response.text}"
    return response.json()

def generate_roadmap(job_title):
    prompt = f"Create a career roadmap for becoming a {job_title} with steps and learning resources."
    result = query({"inputs": prompt})
    
    if isinstance(result, dict) and "error" in result:
        return f"API Error: {result['error']}"
    
    return result[0]["generated_text"]
