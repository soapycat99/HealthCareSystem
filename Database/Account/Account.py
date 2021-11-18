import Interface as inf
import HCS
import Database.ReadData as rd
import Database.DBControl as DB

class Patient():
    def __init__(self,accID):
        # TODO: Return accID to retrieve other info
        # TODO: retrieve record ID by accID
        self.accID = str(accID)
        self.firstName,self.lastName = rd.getName(self.accID)

        try:
            self.recordID = DB.checkRecord(fn=self.firstName,ln=self.lastName)[7]
        except Exception:
            self.recordID = None
        self.func = ['Make Appointment','Check Appointment','Check Record','Check Invoice','X']
        self.actFunc = ['makeAppointment()','checkAppointment()','checkRecord()','checkInvoice()']


    def makeAppointment(self):
        inf.makeAppointment()

    def checkAppointment(self):
        inf.checkAppointment()

    def checkRecord(self):
        if self.recordID == None:
            print("Patient haven't created a record")
        else:
            inf.checkRecord(recid=self.recordID)

    def checkInvoice(self):
        inf.checkInvoice(self.accID)



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