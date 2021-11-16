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

def cardPayment():
    pass

def createRecord():
    HCS.createRecord()

def checkRecord(fn = None,ln = None ,recid = None):
    return HCS.checkRecord(fn,ln,recid)

def checkInvoice(accID):
    return HCS.checkInvoice(accID)

def updateGeneralRecord(recID):
    HCS.updateGeneralRecord(recID)

def updateMeasurement(recID):
    HCS.updateMeasurement(recID)

def showRecordOption():
    HCS.showRecordOption('R2966')

def readPayment():
    HCS.readPayment()

def checkDailyList():
    HCS.checkDailyList()

def main():
    # info = signUp()
    # for i in info:
    #     print(i)
    # HCS.updateGeneralRecord('R2966')
    # username, password = enterInfo()
    # verifyInfo(username, password)

    # makeAppointment()
    # updateAppointment()
    # checkAppointment()
    # cancelAppointment((appID))

    # createRecord()
    # checkRecord(fn='Triet',ln='Le')
    checkRecord(recid='R7437')
    # showRecordOption()
    # checkInvoice('792895')
    # updateGeneralRecord('R2966')
    # updateMeasurement('R2966')
    # readPayment()

if __name__ == "__main__":
    main()