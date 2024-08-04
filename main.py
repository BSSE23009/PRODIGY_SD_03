from Contact import Contact
from ContactManagement import ContactManagement

def main():
    cm = ContactManagement(0, "Alisher")

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            mail = input("Enter mail: ")
            reg = input("Enter reg: ")
            contact = Contact(name, number, mail, reg)
            cm.addContact(contact)
            cm._totalContacts += 1
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            cm.deleteContact(name)
        elif choice == '3':
            cm.displayContacts()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
