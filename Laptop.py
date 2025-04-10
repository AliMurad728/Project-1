contacts = {} 

def display_menu():
    print("Phone Directory Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email (optional): ")

        if not phone.isdigit():
            print("Error: Phone number must contain digits only.")
            continue

        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added.")

    elif choice == "2":
        name = input("Enter name to view: ")
        if name in contacts:
            phone = contacts[name]["phone"]
            email = contacts[name]["email"]
            print(f"{name} - Phone: {phone}, Email: {email if email else 'N/A'}")
        else:
            print("Contact not found.")

    elif choice == "3":  
        name = input("Enter name to update: ")
        if name in contacts:
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email (optional): ")

            if new_phone and not new_phone.isdigit():
                print("Error: Phone number must contain digits only.")
                continue

            if new_phone:
                contacts[name]["phone"] = new_phone
            if new_email or new_email == "":
                contacts[name]["email"] = new_email

            print(f"Contact '{name}' updated.")
        else:
            print("Contact not found.")

    elif choice == "4":  
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")

    elif choice == "5": 
        if not contacts:
            print("No contacts available.")
        else:
            for name, info in contacts.items():
                phone = info["phone"]
                email = info["email"]
                print(f"{name} - Phone: {phone}, Email: {email if email else 'N/A'}")

    elif choice == "6":  
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.") 
   
    
