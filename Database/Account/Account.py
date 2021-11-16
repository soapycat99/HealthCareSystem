import random
import Interface

class Account():
    
    def __init__(self, firstName, lastName, phoneNumber, username, password, category):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.password = password
        self.username = username
        self.category = category
        self.idNum = str(random.randint(100001,999999))
        print(self.idNum)

    def saveAccount(self):
        with open('Database/Account/AccDB','a') as outfile:
            outfile.write('\n')
            outfile.write(f'{self.firstName} | {self.lastName} | {self.phoneNumber} | {self.username} | {self.password} | {self.idNum} | {self.category} | N/A')

class Patient(Account):
    def __init__(self, firstName, lastName, phoneNumber, username,password, category):
        Account.__init__(self,firstName, lastName, phoneNumber, username, password,category)

class Staff(Account):
    def __init__(self, firstName, lastName, phoneNumber, username, password, salary):
        Account.__init__(self,firstName, lastName, phoneNumber, username, password)
        self.salary = salary

class Doctor(Account):
    def __init__(self, firstName, lastName, phoneNumber, username, password, salary = None, dailyList = []):
        Account.__init__(self,firstName, lastName, phoneNumber, username, password)
        self.salary = salary
        self.dailyList= dailyList

    def addPatient(self,record):
        self.dailyList.append(record)

    def getList(self):
        return self.dailyList

class Nurse(Account):
    def __init__(self, firstName, lastName, phoneNumber, username, password, salary):
        Account.__init__(self, firstName, lastName, phoneNumber, username, password)
        self.salary = salary

class CEO(Account):
    def __init__(self, firstName, lastName, phoneNumber, username, password, salary):
        Account.__init__(self, firstName, lastName, phoneNumber, username, password)
        self.salary = salary