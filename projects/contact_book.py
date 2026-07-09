contacts = {}


def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    contacts[name] = phone
    print("Contact saved.")


def find_contact():
    name = input("Name to search: ").strip()
    phone = contacts.get(name)

    if phone:
        print(f"{name}: {phone}")
    else:
        print("Contact not found.")


def show_contacts():
    if not contacts:
        print("No contacts yet.")
        return

    for name, phone in sorted(contacts.items()):
        print(f"{name}: {phone}")


def main():
    while True:
        print("\n1. Add contact")
        print("2. Find contact")
        print("3. Show contacts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            find_contact()
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
