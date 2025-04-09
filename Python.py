phone_directory = {}
todo_list = []

def display_menu():
    print("Show MENU")
    print("1. Add Name")
    print("2.Add Contact")
    print("3. Add Email")
    print("4. Add to-do")
    print("5. View to-dos")
    print("6. Exit")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            if not phone.isdigit():
                raise ValueError("Phone number must contain digits only.")
            phone_directory[name] = phone
            print(f"Contact for {name} added.")

        elif choice == 2:
            name = input("Enter name to view: ")
            try:
                print(f"{name}'s number: {phone_directory[name]}")
            except KeyError:
                print("Contact not found.")

        elif choice == 3:
            name = input("Enter name to delete: ")
            try:
                del phone_directory[name]
                print(f"Deleted contact: {name}")
            except KeyError:
                print("Contact not found.")

        elif choice == 4:
            task = input("Enter a to-do item: ")
            todo_list.append(task)
            print("To-do added.")

        elif choice == 5:
            print("\n--- TO-DO LIST ---")
            if not todo_list:
                print("No tasks.")
            else:
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task}")

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 6.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
