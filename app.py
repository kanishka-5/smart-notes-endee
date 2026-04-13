import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# UI
st.title("📚 Smart Notes AI")
st.write("Ask questions from your notes!")

# Load data
@st.cache_data
def load_data():
    with open("data.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

docs = load_data()

# Create TF-IDF vectors
@st.cache_data
def create_vectors(docs):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)
    return vectorizer, vectors

vectorizer, doc_vectors = create_vectors(docs)

# Search function
def search(query):
    query_vec = vectorizer.transform([query])
    scores = (doc_vectors @ query_vec.T).toarray()
    best_idx = np.argmax(scores)
    return docs[best_idx]

# Input
query = st.text_input("Enter your question:")

if query:
    result = search(query)
    st.success("Answer:")
    st.write(result)