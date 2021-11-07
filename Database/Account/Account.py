import random

class Account():
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, username: str, password: str):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.password = password
        self.username = username
        self.idNum = str(random.randint(100001,999999))
        self.saveData(self.firstName, self.lastName, self.phoneNumber, self.username, self.password, self.idNum)

    def saveData(self, firstName, lastName, phoneNumber, username, password, idNum):
        outfile = open('AccDB', 'w')
        outfile.write(f'{firstName} | {lastName} | {phoneNumber} | {username} | {password} | {id} \n')
        outfile.close()

class Patient(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, username: str,password: str):
        super.__init__(firstName, lastName, phoneNumber, username, password)

class Staff(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, username: str, password: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, username, password)
        self.salary = salary

class Doctor(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, username: str, password: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, username, password)
        self.salary = salary

class Nurse(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, username: str, password: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, username, password)
        self.salary = salary

class CEO(Account):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str,  username: str, password: str, salary: float):
        super.__init__(firstName, lastName, phoneNumber, username, password)
        self.salary = salary
