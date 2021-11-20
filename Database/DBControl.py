from Database import ReadData as rd
from Database import CreateData as cd
from Database import DeleteData as dd
from Database import UpdateData as ud

def verifyInfo(acc, pw):
    return rd.readInfo(acc, pw)

def signUp(firstName, lastName, phoneNumber, username, password, category):
    return cd.createAccount(firstName, lastName, phoneNumber, username, password, category)

def makeAppointment(info):
    cd.createAppointment(info)

def checkAppointment(lastName, phoneNumber):
    return rd.readAppointment(lastName, phoneNumber)

def updateAppointment(opt,data,appID):
    return ud.updateAppointment(opt,data,appID)

def cancelAppointment(appID):
    dd.deleteApp(appID)

def createRecord(record):
    cd.createRecord(record)

def checkRecord(fn = None ,ln = None ,recid = None):
    return rd.readRecord(fn,ln,recid)

def checkInvoice(accID):
    return rd.readInvoice(accID)

def updateGeneralRecord(opt,data,recID):
    ud.updateGeneralRecord(opt,data,recID)

def updateMeasurement(pos, data, recID):
    ud.updateMeasurement(pos,data, recID)

def getName(accID):
    return rd.getName(accID)

def storePayment(payInfo):
    cd.createPayment(payInfo)

def readPayment(refNum=None,firstName=None,lastName=None):
    info =  rd.readPayment(refNum,firstName,lastName)
    return info

def addPatient(recID,opt):
    ud.addPatient(recID,opt)
