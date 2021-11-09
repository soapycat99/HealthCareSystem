from Database import ReadData as rd
from Database import CreateData as cd
from Database import DeleteData as dd

def checkInfo(acc, pw):
    return rd.readInfo(acc, pw)

def signUp(firstName, lastName, phoneNumber, username, password, category):
    cd.createAccount(firstName, lastName, phoneNumber, username, password, category)

def makeAppointment(firstName, lastName, phoneNumber, doctor):
    cd.createAppointment(firstName, lastName, phoneNumber, doctor)

def checkAppointment(lastName, phoneNumber):
    return rd.readAppointment(lastName, phoneNumber)

def cancelAppointment(appID):
    dd.deleteApp(appID)

def createRecord(record):
    cd.createRecord(record)

