import streamlit as st
import os

# -------------------------------------------------------
# FILES
# -------------------------------------------------------
USER_FILE = "users.txt"
MENU_FILE = "bakery_menu.txt"

# -------------------------------------------------------
# LOAD USERS
# FORMAT: username,password,role,mobile
# -------------------------------------------------------
def load_users():
    users = {}

    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            f.write("admin,admin123,admin,9000000000\n")

    with open(USER_FILE, "r") as f:
        for line in f:
            if line.strip():
                u, p, r, m = line.strip().split(",")
                users[u] = {"password": p, "role": r, "mobile": m}
    return users

# -------------------------------------------------------
# SAVE USERS
# -------------------------------------------------------
def save_users(users):
    with open(USER_FILE, "w") as f:
        for u, d in users.items():
            f.write(f"{u},{d['password']},{d['role']},{d['mobile']}\n")

# -------------------------------------------------------
# LOAD MENU
# -------------------------------------------------------
def load_menu():
    menu = {}

    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, "w") as f:
            f.write("1,Chocolate Cake\n")
            f.write("2,Veg Puff\n")
            f.write("3,Paneer Roll\n")
            f.write("4,Cheese Sandwich\n")

    with open(MENU_FILE, "r") as f:
        for line in f:
            if line.strip():
                i, name = line.strip().split(",")
                menu[int(i)] = name

    return menu

# -------------------------------------------------------
# SAVE MENU
# -------------------------------------------------------
def save_menu(menu):
    with open(MENU_FILE, "w") as f:
        for i, v in menu.items():
            f.write(f"{i},{v}\n")

# -------------------------------------------------------
# LOGIN VALIDATION
# -------------------------------------------------------
def authenticate(users, username, mobile, password):
    if username in users:
        data = users[username]
        return data["password"] == password and data["mobile"] == mobile
    return False

# -------------------------------------------------------
# STREAMLIT UI
# -------------------------------------------------------
st.set_page_config(page_title="Bakery Management", layout="centered")
st.title("🍰 Bakery Management System")

users = load_users()
menu = load_menu()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None
if "username" not in st.session_state:
    st.session_state.username = None

# -------------------------------------------------------
# LOGIN UI
# -------------------------------------------------------
if not st.session_state.logged_in:

    st.subheader("Login")
    mobile = st.text_input("Mobile (must be 10 digits and start with 9)")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        valid_mobile = len(mobile) == 10 and mobile.startswith("9") and mobile.isdigit()

        if not valid_mobile:
            st.error("Invalid mobile number!")
        elif authenticate(users, username, mobile, password):
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.session_state.role = users[username]["role"]
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Login failed. Wrong credentials.")

# -------------------------------------------------------
# LOGGED-IN PANELS
# -------------------------------------------------------
else:
    role = st.session_state.role
    username = st.session_state.username

    st.sidebar.title("Navigation")

    if role == "admin":
        choice = st.sidebar.radio("Menu", ["View Menu", "Search Item", "Add Item", "Delete Item", "Edit My Info", "Logout"])
    elif role == "user":
        choice = st.sidebar.radio("Menu", ["View Menu", "Search Item", "Edit My Info", "Logout"])
    else:
        choice = st.sidebar.radio("Menu", ["View Menu", "Logout"])

    # View Menu
    if choice == "View Menu":
        st.subheader("Bakery Menu")
        for i, item in menu.items():
            st.write(f"{i}. {item}")

    # Search Item
    if choice == "Search Item":
        key = st.text_input("Search item:")
        if key:
            results = [f"{i}. {item}" for i, item in menu.items() if key.lower() in item.lower()]
            if results:
                st.success("\n".join(results))
            else:
                st.error("No item found.")

    # Add Item
    if choice == "Add Item" and role == "admin":
        new_item = st.text_input("New item name")
        if st.button("Add"):
            new_id = max(menu.keys()) + 1
            menu[new_id] = new_item
            save_menu(menu)
            st.success("Item added!")

    # Delete Item
    if choice == "Delete Item" and role == "admin":
        del_id = st.number_input("Enter ID to delete", step=1, min_value=1)
        if st.button("Delete"):
            if del_id in menu:
                del menu[del_id]
                save_menu(menu)
                st.success("Item deleted!")
            else:
                st.error("Invalid ID")

    # Edit Info
    if choice == "Edit My Info":
        new_mob = st.text_input("New mobile number")
        if st.button("Update"):
            if len(new_mob) == 10 and new_mob.startswith("9"):
                users[username]["mobile"] = new_mob
                save_users(users)
                st.success("Mobile updated!")
            else:
                st.error("Invalid number!")

    # Logout
    if choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = None
        st.rerun()