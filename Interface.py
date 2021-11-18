import HCS

def logIn():
    return HCS.enterInfo()

def signUp():
    HCS.signUp()

def makeAppointment():
    HCS.makeAppointment()

def checkAppointment():
    return HCS.checkAppointment()

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

def showFunc(func):
    opt = None
    for count,key in enumerate(func,1):
        print(f'{count}. {key}')

    while True:
        try:
            opt = int(input('Enter: '))
            if opt <= 0 or opt > 5:
                continue
        except ValueError:
            continue

        break

    return opt-1

def main():
    pass
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
    # checkRecord(fn='Nam',ln='Dang')
    # checkRecord(recid='R7437')
    # showRecordOption()
    # checkInvoice4('792895')
    # updateGeneralRecord('R2966')
    # updateMeasurem4ent('R2966')
    # readPayment()

if __name__ == "__main__":
    main()