import Database.DBControl as DB

def verifyInfo(acc,pw):
    return DB.checkInfo(acc,pw)

def signUp(firstName, lastName, phoneNumber, username, password, category):
    DB.signUp(firstName, lastName, phoneNumber, username, password, category)

def makeAppointment(firstName, lastName, phoneNumber, doctor):
    DB.makeAppointment(firstName, lastName, phoneNumber, doctor)

def checkAppointment(lastName, phoneNumber):
    return DB.checkAppointment(lastName, phoneNumber)

def cancelAppointment(appID):
    DB.cancelAppointment(appID)

def createRecord(record):
    DB.createRecord(record)

def checkRecord(fn,ln,recid):
    return DB.checkRecord(fn,ln,recid)

