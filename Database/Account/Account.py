import Interface as inf


class Patient():
    def __init__(self,recordID=None):
        self.recordID = recordID

    def makeAppointment(self):
        inf.makeAppointment()

    def checkAppointment(self):
        inf.checkAppointment()


class Staff():
    def __init__(self, salary):
        self.salary = salary

class Doctor():
    def __init__(self,salary = None, dailyList = None):
        self.salary = salary
        self.dailyList= dailyList

    def addPatient(self,record):
        self.dailyList.append(record)

    def getList(self):
        return self.dailyList

class Nurse():
    def __init__(self,salary):
        self.salary = salary

class CEO():
    def __init__(self, salary):
        self.salary = salary