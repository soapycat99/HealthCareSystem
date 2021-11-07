import random

class Account():
    
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, username: str, password: str, category: str):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.password = password
        self.username = username
        self.category = category
        self.idNum = str(random.randint(100001,999999))
        print(self.idNum)
        # self.saveAccount(self.firstName, self.lastName, self.phoneNumber, self.username, self.password, self.idNum, self.category)

    def saveAccount(self, firstName, lastName, phoneNumber, username, password, idNum, category):
        with open('Database/Account/AccDB','a') as outfile:
            outfile.write('\n')
            outfile.write(f'{firstName} | {lastName} | {phoneNumber} | {username} | {password} | {idNum} | {category} | N/A')

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
