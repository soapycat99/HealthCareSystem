class Account():
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, password: str, username: str, id: str):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.password = password
        self.username = username
        self.id = id

class Patient(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, password: str, username: str, id: str):
        super.__init__(firstName, lastName, phoneNumber, password, username, id)

class Staff(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, password: str, username: str, id: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, password, username, id)
        self.salary = salary

class Doctor(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, password: str, username: str, id: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, password, username, id)
        self.salary = salary

class Nurse(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, password: str, username: str, id: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, password, username, id)
        self.salary = salary

class CEO(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, password: str, username: str, id: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, password, username, id)
        self.salary = salary
