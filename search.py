import streamlit as st

# 🔐 Login check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first")
    st.stop()

# 📂 Load data
with open("data/data.txt") as f:
    docs = f.readlines()

st.title("🔍 Smart Search AI")

query = st.text_input("Ask something:")

# 🔍 Improved search (Top 3 results)
def search(query):
    results = []

    for doc in docs:
        score = sum(1 for word in query.lower().split() if word in doc.lower())
        results.append((score, doc))

    # sort by score
    results.sort(reverse=True)

    # return top 3
    return [r[1] for r in results[:3] if r[0] > 0]

# 🎯 Run search
if query:
    answers = search(query)

    if answers:
        st.success("Top Results:")
        for ans in answers:
            st.write("👉", ans)
    else:
        st.warning("No match found")
