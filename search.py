with open("data/data.txt") as f:
    docs = f.readlines()

query = st.text_input("Ask something:")

if query:
    best_match = ""
    best_score = 0

    for doc in docs:
        score = sum(1 for word in query.lower().split() if word in doc.lower())

        if score > best_score:
            best_score = score
            best_match = doc

    if best_match:
        st.success("Best Answer:")
        st.write(best_match)
    else:
        st.warning("No match found")