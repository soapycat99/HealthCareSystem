import Interface as inf
import HCS
import Database.ReadData as rd
import Database.DBControl as DB

class Patient():
    def __init__(self,accID):

        self.accID = str(accID)
        self.firstName,self.lastName = rd.getName(self.accID)

        try:
            self.recordID = DB.checkRecord(fn=self.firstName,ln=self.lastName)[7]
        except Exception:
            self.recordID = None
        self.func = ['Make Appointment','Check Appointment','Check Record','Check Invoice','X']
        self.actFunc = ['makeAppointment()','checkAppointment()','checkRecord()','checkInvoice()']


    def makeAppointment(self):
        inf.makeAppointment(self.firstName,self.lastName)

    def checkAppointment(self):
        inf.checkAppointment()

    def checkRecord(self):
        if self.recordID == None:
            print("Patient haven't created a record")
        else:
            actor = self.__class__.__name__
            inf.checkRecord(actor= actor,recid=self.recordID)

    def checkInvoice(self):
        inf.checkInvoice(self.accID)



class Staff():
    def __init__(self, accID):
        self.accID = accID

class Doctor():
    def __init__(self,accID):
        self.accID = accID
        self.dailyList= rd.getDailyList(self.accID)
        self.func = ['Read Payment Information','Check Daily List','Check Record',  'X']
        self.actFunc = ['readPayment()', 'checkDailyList()', 'checkRecord()']

    def addPatient(self,record):
        self.dailyList.append(record)

    def checkDailyList(self):
        inf.checkDailyList(*self.dailyList)

    def readPayment(self):
        inf.readPayment()

    def checkRecord(self):
        actor = self.__class__.__name__
        inf.checkRecord(actor=actor)





class Nurse():
    def __init__(self,salary):
        self.salary = salary

class CEO():
    def __init__(self, salary):
        self.salary = salary