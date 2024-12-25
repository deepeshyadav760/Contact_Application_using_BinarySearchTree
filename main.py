from contact_bst import ContactBST    # from the file contact_bst  I am importing the class ContactBST --> containg all the methods/fucntions


# This is for the user to manually add, delete, update, search , do the partial search, export the contacts, import the contacts
# To make the application user friendly
def user():
    contacts = ContactBST()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Partial Search")
        print("7. Export Contacts to File")
        print("8. Import Contacts from File")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contacts.insert(name, phone, email)

        elif choice == "2":
            print("\nContacts:")
            contacts.display_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            result = contacts.search_contact(name)
            if result:
                print(f"Found: {result.name}, {result.phone_number}, {result.email}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            contacts.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "5":
            name = input("Enter name to delete: ")
            contacts.delete_contact(name)
            print(f"Contact '{name}' deleted.")

        elif choice == "6":
            prefix = input("Enter prefix for partial search: ")
            results = contacts.search_partial(prefix)
            if results:
                print("\nPartial Matches:")
                for res in results:
                    print(f"Name: {res.name}, Phone: {res.phone_number}, Email: {res.email}")
            else:
                print(f"No contacts found with prefix '{prefix}'.")

        elif choice == "7":
            file_path = input("Enter file path to export: ")
            contacts.export_to_file(file_path)

        elif choice == "8":
            file_path = input("Enter file path to import: ")
            contacts.import_from_file(file_path)

        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user()
