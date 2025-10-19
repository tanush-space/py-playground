# Blood Bank Management System
# All data is stored in memory only

donors = []

def add_donor():
    print("\n=== Add New Donor ===")
    name = input("Enter donor's full name: ").strip()
    blood_type = input("Enter blood type (e.g., A+, O-): ").strip()
    location = input("Enter city or location: ").strip()

    donors.append({
        "Name": name,
        "BloodType": blood_type,
        "Location": location
    })

    print(f"\nDonor '{name}' has been successfully added.\n")

def search_donors():
    print("\n=== Search for Donors ===")
    blood_type = input("Enter blood type to search: ").strip()
    location = input("Enter city or location: ").strip()

    print("\n--- Matching Donors ---")
    found = False
    for donor in donors:
        if donor["BloodType"].lower() == blood_type.lower() and donor["Location"].lower() == location.lower():
            print(f"Name: {donor['Name']} | Blood Type: {donor['BloodType']} | City: {donor['Location']}")
            found = True

    if not found:
        print("No matching donors found.")
    print()

def generate_report():
    print("\n=== Donor Report ===")
    if not donors:
        print("There are no donor records to display.\n")
        return

    for idx, donor in enumerate(donors, start=1):
        print(f"{idx}. Name: {donor['Name']} | Blood Type: {donor['BloodType']} | City: {donor['Location']}")
    print()

def main():
    print("=== WELCOME TO THE BLOOD BANK MANAGEMENT SYSTEM ===")

    while True:
        print("\nPlease select an option:")
        print("1. Add Donor")
        print("2. Search Donor")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_donor()
        elif choice == '2':
            search_donors()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            print("\nThank you for using the Blood Bank Management System. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()