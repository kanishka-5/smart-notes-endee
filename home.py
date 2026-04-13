import streamlit as st

def load_users():
    users = {}
    with open("auth/users.txt") as f:
        for line in f:
            u, p = line.strip().split(",")
            users[u] = p
    return users

users = load_users()

def login_page():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
        else:
            st.error("Invalid credentials")