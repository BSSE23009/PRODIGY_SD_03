from Contact import Contact

class ContactManagement:
    def __init__(self, totalContacts, userName):
        self._totalContacts = totalContacts
        self._userName = userName
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def deleteContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                break

    def displayContacts(self):
        print("The contacts available are:")
        for contact in self.contacts:   
            contact.displayDetails()
