import streamlit as st

# ✅ Page config (UI improvement)
st.set_page_config(page_title="Smart Notes AI", layout="centered")

# ---------------- LOGIN FUNCTION ----------------
def check_login(username, password):
    with open("auth/users.txt") as f:
        users = f.readlines()

    for user in users:
        u, p = user.strip().split(",")
        if u == username and p == password:
            return True
    return False


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN UI ----------------
if not st.session_state.logged_in:
    st.title("🔐 Login - Smart Notes AI")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

# ---------------- AFTER LOGIN ----------------
else:
    st.sidebar.success("✅ Logged in")
    st.sidebar.write("Go to Home / Search")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("📚 Smart Notes AI")
    st.write("Use sidebar to navigate →")
