from datetime import datetime, timedelta

# Store all vehicle test info here
pollution_records = []

def new_record():
    print("\n=== Add New Vehicle Record ===")
    owner = input("Enter owner's name: ").strip()
    number = input("Enter vehicle number: ").strip()
    date_str = input("Enter test date (DD-MM-YYYY or similar): ").strip()
    level = input("Enter pollution level (Low/Medium/High): ").strip().capitalize()

    record = {
        "owner": owner,
        "vehicle": number,
        "test_date": date_str,
        "pollution": level
    }
    pollution_records.append(record)
    print(f"\nRecord for vehicle '{number}' has been successfully added.\n")

def show_all_records():
    print("\n=== All Vehicle Test Records ===")
    if not pollution_records:
        print("No records to show.\n")
        return

    for idx, rec in enumerate(pollution_records, start=1):
        print(f"{idx}. Owner: {rec['owner']} | Vehicle: {rec['vehicle']} | Test Date: {rec['test_date']} | Pollution: {rec['pollution']}")
    print()

def check_validity():
    print("\n=== Check Pollution Certificate Expiry ===")
    if not pollution_records:
        print("No data available.\n")
        return
    
    today = datetime.now().date()
    expired_found = False

    for rec in pollution_records:
        try:
            # Accept multiple date formats
            for fmt in ("%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y", "%d %m %Y"):
                try:
                    test_date = datetime.strptime(rec["test_date"], fmt).date()
                    break
                except ValueError:
                    test_date = None

            if not test_date:
                raise ValueError

            valid_until = test_date + timedelta(days=180)
            if valid_until < today:
                expired_found = True
                print(f"Expired: {rec['vehicle']} (Owner: {rec['owner']}) - expired on {valid_until.strftime('%d-%m-%Y')}")
        except ValueError:
            print(f"Wrong date format for vehicle '{rec['vehicle']}'. Please use DD-MM-YYYY or similar.")

    if not expired_found:
        print("All vehicles are still valid.\n")

def menu():
    print("=== VEHICLE POLLUTION CONTROL RECORD SYSTEM ===")
    while True:
        print("\nPlease select an option:")
        print("1) Add Record")
        print("2) Show Records")
        print("3) Check Expiry")
        print("4) Exit")

        option = input("Enter choice (1-4): ").strip()

        if option == "1":
            new_record()
        elif option == "2":
            show_all_records()
        elif option == "3":
            check_validity()
        elif option == "4":
            print("\nExiting program. Goodbye!\n")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    menu()