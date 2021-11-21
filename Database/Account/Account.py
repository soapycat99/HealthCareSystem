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
        self.func = ['Make Appointment','Check Appointment','Check Record','Check Invoice','Log Out','Quit']
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
        self.func = ['Make Appointment','Check Appointment','Read Payment Information','Create Record','Check Record','Log Out','Quit']
        self.actFunc = ['makeAppointment()','checkAppointment()','readPayment()','createRecord()','checkRecord()']
    def makeAppointment(self):
        inf.makeAppointment()

    def checkAppointment(self):
        inf.checkAppointment()

    def readPayment(self):
        inf.readPayment()

    def checkRecord(self):
        actor = self.__class__.__name__
        inf.checkRecord(actor=actor)

    def createRecord(self):
        inf.createRecord()

class Doctor():
    def __init__(self,accID):
        self.accID = accID
        self.dailyList= rd.getDailyList(self.accID)
        self.func = ['Read Payment Information','Check Daily List','Check Record', 'Log Out','Quit']
        self.actFunc = ['readPayment()', 'checkDailyList()', 'checkRecord()']


    def checkDailyList(self):
        inf.checkDailyList(*self.dailyList)

    def readPayment(self):
        inf.readPayment()

    def checkRecord(self):
        actor = self.__class__.__name__
        inf.checkRecord(actor=actor)







class Nurse():
    def __init__(self, accID):
        self.accID = accID
        self.func = ['Read Payment Information','Check Record','Log Out','Quit']
        self.actFunc = ['readPayment()','checkRecord()']

    def checkRecord(self):
        actor = self.__class__.__name__
        inf.checkRecord(actor=actor)

    def readPayment(self):
        inf.readPayment()


class CEO():
    def __init__(self, accID):
        self.accID = accID

    def readSalaryList(self):
        inf.readSalaryList()