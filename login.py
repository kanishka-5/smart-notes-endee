import streamlit as st

# 🔹 LOAD USERS FUNCTION
def load_users():
    users = {}

    # 👉 THIS LINE IS HERE
    with open("auth/users.txt") as f:
        for line in f:
            username, password = line.strip().split(",")
            users[username] = password

    return users


# 🔹 LOGIN FUNCTION
def login_page():
    st.title("🔐 Login Page")

    users = load_users()   # call function

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
        else:
            st.error("Invalid username or password")