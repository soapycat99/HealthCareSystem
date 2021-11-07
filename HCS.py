import Database.DBControl as DB

def verifyInfo(acc,pw):
    return DB.checkInfo(acc,pw)

def signUp(firstName, lastName, phoneNumber, username, password):
    DB.signUp(firstName, lastName, phoneNumber, username, password)
