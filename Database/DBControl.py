from Database import ReadData as rd
from Database import CreateData as cd
from Database import DeleteData as dd

def checkInfo(acc, pw):
    return rd.readInfo(acc, pw)

def signUp(firstName, lastName, phoneNumber, username, password, category):
    cd.createAccount(firstName, lastName, phoneNumber, username, password, category)

def makeAppointment(info):
    cd.createAppointment(info)

def checkAppointment(lastName, phoneNumber):
    return rd.readAppointment(lastName, phoneNumber)

def cancelAppointment(appID):
    dd.deleteApp(appID)

def createRecord(record):
    cd.createRecord(record)

def checkRecord(fn,ln,recid):
    return rd.readRecord(fn,ln,recid)

def checkInvoice(accID):
    return rd.readInvoice(accID)
