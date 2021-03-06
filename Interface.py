import HCS

def welcomeInf():
    print('1. Sign up\n'
          '2. Login\n'
          '3. Quit')
    while True:
        opt = 0
        try:
            opt = int(input('Select(1-3): '))
            if opt != 1 and opt != 2 and opt != 3:
                continue
            else:
                return opt
        except ValueError:
            continue



def login():
    return HCS.login()

def signUp():
    return HCS.signUp()

def makeAppointment(fn=None,ln=None):
    HCS.makeAppointment(fn,ln)

def checkAppointment():
    HCS.checkAppointment()

def createRecord():
    HCS.createRecord()


def checkRecord(actor=None,fn = None,ln = None ,recid = None):

    actList = ['Patient','Staff','Nurse','Doctor','CEO']

    #showing option board searching by name or by record id
    if actor != actList[0]:
        opt = 0
        while True:
            print('Searching by:\n'
                  '1. Record ID\n'
                  '2. First name, Last name')
            try:
                opt = int(input('Choose: '))
                if opt != 1 and opt != 2:
                    continue
                else:
                    break
            except Exception:
                continue

        if opt == 1:
            recid = input('Record ID: ')
        else:
            fn = input('First Name: ')
            ln = input('Last Name: ')
    try:
        recid = HCS.checkRecord(fn,ln,recid)

        if actor == actList[1]:
            HCS.showStaffOption(recid)
        elif actor == actList[2]:
            HCS.showNurseOption(recid)
        elif actor == actList[3]:
            HCS.showDoctorOption(recid)

    except Exception:
        print('Unavailable')

def checkInvoice(accID):
    HCS.checkInvoice(accID)


def updateGeneralRecord(recID):
    HCS.updateGeneralRecord(recID)

def updateMeasurement(recID):
    HCS.updateMeasurement(recID)

def readPayment():
    HCS.readPayment()

def checkDailyList(*args):
    HCS.checkDailyList(*args)

def readSalaryList():
    HCS.readSalaryList()

def updateSalary():
    HCS.updateSalary()

def showFunc(func):
    opt = None
    for count,key in enumerate(func,1):
        print(f'{count}. {key}')

    while True:
        try:
            opt = int(input('Enter: '))
            if opt <= 0 or opt > len(func):
                continue
        except ValueError:
            continue

        break

    return opt-1

def main():
    # pass
    signUp()

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