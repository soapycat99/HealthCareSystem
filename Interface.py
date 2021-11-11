import HCS

def verifyInfo(acc,pw):
    return HCS.verifyInfo(acc,pw)

def signUp():
    HCS.signUp()

def makeAppointment():
    HCS.makeAppointment()

def checkAppointment():
    return HCS.checkAppointment()

def updateAppointment(appID):
    HCS.updateAppointment(appID)

def cancelAppointment(appID):
    HCS.cancelAppointment(appID)

def createRecord():
    HCS.createRecord()

def checkRecord(fn = None,ln = None ,recid = None):
    return HCS.checkRecord(fn,ln,recid)

def checkInvoice(accID):
    return HCS.checkInvoice(accID)

def updateGeneralRecord(recID):
    HCS.updateGeneralRecord(recID)

def main():
    # info = signUp()
    # for i in info:
    #     print(i)
    # HCS.updateGeneralRecord('R2966')
    # username, password = enterInfo()
    # verifyInfo(username, password)

    # makeAppointment()
    # updateAppointment()
    checkAppointment()
    # cancelAppointment((appID))

    # createRecord()
    # checkRecord(fn='Triet',ln='Le')
    # checkRecord(recid='R2966')
    # checkInvoice('792895')
    # updateGeneralRecord('R2966')

if __name__ == "__main__":
    main()