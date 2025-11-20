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

    # Create default admin if file does not exist
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
# FORMAT: id,item
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
# MOBILE VERIFICATION
# -------------------------------------------------------
def verify_mobile():
    mob = input("Enter Mobile Number (must start with 9 and be 10 digits): ")
    if len(mob) == 10 and mob.startswith("9") and mob.isdigit():
        return mob
    else:
        print("❌ Invalid mobile number!")
        return None


# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
def login(users):
    print("\n=== LOGIN ===")
    mobile = verify_mobile()
    if not mobile:
        return None

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password and users[username]["mobile"] == mobile:
        print("\n✔ Login Successful ✔")
        return username
    else:
        print("\n❌ Login Failed!")
        return None


# -------------------------------------------------------
# BAKERY MENU FEATURES
# -------------------------------------------------------
def view_menu(menu):
    print("\n--- Bakery Menu ---")
    for i, item in menu.items():
        print(f"{i}. {item}")


def search_item(menu):
    key = input("Enter item name to search: ").lower()
    found = False
    for i, item in menu.items():
        if key in item.lower():
            print(f"Found: {i}. {item}")
            found = True
    if not found:
        print("No matching item found.")


def add_item(menu):
    new_id = max(menu.keys()) + 1
    name = input("Enter new bakery item: ")
    menu[new_id] = name
    save_menu(menu)
    print("✔ Item added!")


def delete_item(menu):
    view_menu(menu)
    try:
        id_ = int(input("Enter ID to delete: "))
        if id_ in menu:
            del menu[id_]
            save_menu(menu)
            print("✔ Item deleted!")
        else:
            print("Invalid ID.")
    except:
        print("Invalid input.")


# -------------------------------------------------------
# EDIT USER INFO
# -------------------------------------------------------
def edit_info(username, users):
    new_mob = input("Enter new mobile (must start with 9): ")
    if len(new_mob) == 10 and new_mob.startswith("9") and new_mob.isdigit():
        users[username]["mobile"] = new_mob
        save_users(users)
        print("✔ Mobile updated!")
    else:
        print("❌ Invalid mobile number")


# -------------------------------------------------------
# ADMIN PANEL
# -------------------------------------------------------
def admin_panel(username, users, menu):
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. View Bakery Menu")
        print("2. Search Item")
        print("3. Add Item")
        print("4. Delete Item")
        print("5. Edit My Info")
        print("6. Logout")

        c = input("Enter choice: ")

        if c == "1":
            view_menu(menu)
        elif c == "2":
            search_item(menu)
        elif c == "3":
            add_item(menu)
        elif c == "4":
            delete_item(menu)
        elif c == "5":
            edit_info(username, users)
        elif c == "6":
            break
        else:
            print("Invalid option!")


# -------------------------------------------------------
# NORMAL USER PANEL
# -------------------------------------------------------
def user_panel(username, users, menu):
    while True:
        print("\n===== USER MENU =====")
        print("1. View Bakery Menu")
        print("2. Search Item")
        print("3. Edit My Info")
        print("4. Logout")

        c = input("Enter choice: ")

        if c == "1":
            view_menu(menu)
        elif c == "2":
            search_item(menu)
        elif c == "3":
            edit_info(username, users)
        elif c == "4":
            break
        else:
            print("Invalid option!")


# -------------------------------------------------------
# GUEST PANEL (Limited)
# -------------------------------------------------------
def guest_panel(menu):
    while True:
        print("\n===== GUEST MENU =====")
        print("1. View Bakery Menu")
        print("2. Logout")

        c = input("Enter choice: ")

        if c == "1":
            view_menu(menu)
        elif c == "2":
            break
        else:
            print("Invalid option!")


# -------------------------------------------------------
# MAIN SYSTEM
# -------------------------------------------------------
def main():
    users = load_users()
    menu = load_menu()

    print("\n🍰 BAKERY MANAGEMENT SYSTEM 🍰")

    username = login(users)
    if not username:
        return

    role = users[username]["role"]

    if role == "admin":
        admin_panel(username, users, menu)
    elif role == "user":
        user_panel(username, users, menu)
    else:
        guest_panel(menu)


# RUN SYSTEM
main()
