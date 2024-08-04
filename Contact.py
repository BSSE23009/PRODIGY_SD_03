class Contact:
    def __init__(self, name, number, mail, reg):
        self._name = name
        self._number = number
        self._mail = mail
        self._reg = reg

    def displayDetails(self):
        print("Contact name:", self._name)
        print("Contact number:", self._number)
        print("Contact mail:", self._mail)
        print("Contact reg:", self._reg)

    @property
    def name(self):
        return self._name

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def reg(self):
        return self._reg