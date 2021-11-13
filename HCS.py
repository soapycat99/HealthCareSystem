import Database.DBControl as DB

def enterInfo():
    username = input('Enter ID: ')
    password = input('Enter passworld: ')
    verifyInfo(username,password)
    return username, password

def verifyInfo(username, password):
    if(DB.verifyInfo(username,password) == True):
        print('Access granted')
    else:
        print('GG')

def signUp():
    firstName = input('First name: ')
    lastName = input('Last name: ')
    phoneNumber = input('Phone number: ')
    username = input('Username : ')
    password = input('Password: ')
    category = input('Category: ')
    DB.signUp(firstName, lastName, phoneNumber, username, password, category)

    return [firstName, lastName, phoneNumber, username, password, category]

def makeAppointment():
    info = []
    info.append(input('First name: '))
    info.append(input('Last name: '))
    info.append(input('Phone number: '))
    info.append(input('Doctor: '))
    info.append(input('Date: '))
    info.append(input('Time: '))
    DB.makeAppointment(info)

def checkAppointment(lastName = None, phoneNumber = None):
    if lastName == None:
        lastName = input('Last name: ')
        phoneNumber = input('Phone number: ')

    info = DB.checkAppointment(lastName, phoneNumber)
    if info != None:
        key = ['AppID', 'First Name', 'Last Name', 'Phone Number', 'Doctor', 'Date','Time']
        for k,i in zip(key,info):
            print(f'{k}: {i}')
        print('----------------')
        print('1/ Update Appointment')
        print('2/ Cancel Appointment')
        print('3/ X')
        print(f'AppID = {info[0]} and type {type(info[0])}')
        opt = input('Enter: ')
        if int(opt) == 1:
            updateAppointment(info[0])
        elif int(opt) ==2:
            cancelAppointment(info[0])
        else:
            pass
    else:
        print('wtf why doesnt it work, try again')
        checkAppointment()

def cancelAppointment(appID):
    DB.cancelAppointment(appID)
    print('Appointment cancelled successfully!')

def updateAppointment(appID):
    category = ['First Name','Last Name', 'Phone Number', 'Doctor','Date','Time']
    opt = 0
    data = ''
    for count, value in enumerate(category, 1):
        print(f'{count}. {value}')
    while True:
        opt = int(input('Input: '))
        if opt >= 1 and opt <= len(category):
            data = input(f'Update {category[opt - 1]}: ')
            break

    lastName, phoneNumber = DB.updateAppointment(opt,data,appID)
    checkAppointment(lastName, phoneNumber)

def cardPayment(invNum):
    # print('Card number: 123456789')
    # print('PIN: 123')
    print(f'Invoice: {invNum}')

    #Lam chua xong

def createRecord():
    record = []
    record.append(input('First Name: '))
    record.append(input('Last Name: '))
    record.append(input('Address: '))
    record.append(input('Phone Number: '))
    record.append(input('Email: '))
    record.append(input('SSN: '))
    record.append(input('Insurance Name: '))
    DB.createRecord(record)

def checkRecord(fn = None, ln = None, recid = None):
    info = DB.checkRecord(fn,ln,recid)
    print(info)
    info1 = info[:8]
    print(info1)
    info2 = info[8:-1]
    summary = info[-1]
    print(info2)

    key1 = ['First Name', 'Last Name', 'Address', 'Phone', 'Email', 'SSN','Insurance Name', 'RecID']
    key2 = ['Weight','Height','Blood Pressure','Pulse','Radiology','Pathology','Allergy','Prescription']

    for k1,i1,k2,i2 in zip(key1,info1,key2,info2):
        firstVal = f'{k1}: {i1}'
        if k2 != 'Weight':
            print(f'{firstVal:<45} {k2}: {i2:<25} ')
        else:
            print(f'{firstVal:<45} {k2}: {i2:<25} Summary: {summary}')

    print('-'*75,'\n')


    recID = info1[-1]
    showRecordOption(recID)

def showRecordOption(recID):
    print('Select Option')
    for count,key in enumerate(['Update General Record','Update Treatment','Update Measurement','X'],1):
        print(f'{count}. {key}')
    opt = 0
    option = ['updateGeneralRecord','updateTreatment','updateMeasurement']

    while True:
        try:
            opt = int(input('Input: '))
            if opt >= 1 and opt <= 3:
                globals()[option[opt-1]](recID)
                break
            elif opt == 4:
                break
            print('Invalid, try again')
        except ValueError:
            print('Invalid, try again')
            continue


def checkInvoice(accID):
    invList = DB.checkInvoice(accID)
    key = list()
    if invList != None:
        key = ['Invoice Number', 'Amount', 'Description']
        for count, info in enumerate(invList,1):
            print(f'{count}/',end='')
            for k, i in zip(key,info):
                print(f'{k:>20}: {i}')
            print('----------------')
        order = payingAlert(len(invList)+1)
        if order != None:
            invNum = invList[order][0]
            cardPayment(invNum)



def payingAlert(num):
    opt = None
    order = None

    while opt not in ('Y','N'):
        opt = input('Paying invoice(Y/N)?: ')
        if opt not in ('Y','N'):
            print('Please answer by typing Y or N')

    if opt == 'Y':
        while order not in range(1,num):
            order = input('Choose invoice you would like to pay: ')
            if int(order) not in range(num):
                print(f'You must choose a number from 1 to {num-1}, try again')
            else:
                order = int(order)-1
    return order

def readPayment():
    pass

def updateGeneralRecord(recID):
    print('this is updating general record')
    category = ['First Name', 'Last Name', 'Address', 'Phone Number','Email','SSN','Insurance Name']
    print('Choose category to be updated:')
    opt = 0
    data = ''
    for count, value in enumerate(category,1):
        print(f'{count}. {value}')
    while True:
        try:
            opt = int(input('Input: '))
            if opt>=1 and opt<=len(category):
                data = input(f'Update {category[opt-1]}: ')
                break
            print('Invalid, try again')
        except ValueError:
            print('Invalid, try again')
            continue
    DB.updateGeneralRecord(opt-1,data,recID)
    checkRecord(recid=recID)

def updateMeasurement(recID):
    category = ['Weight','Height','Blood Pressure','Pulse']
    print('Select a index needed to be updated: ')
    for count, value in enumerate(category,1):
        print(f'{count}. {value}')
    opt = 0
    data =''
    while True:
        try:
            opt = int(input('Enter :'))
            if opt>0 and opt <=len(category):
                data = input(f'Update {category[opt-1]}: ')
                break
            print('Invalid, try again')

        except ValueError:
            print('Invalid, try again')
            continue
    pos = opt + 8  #line position

    DB.updateMeasurement(pos, data, recID)
    checkRecord(recid=recID)

def updateTreatment(recID):
    category = ['Radiology','Pathology','Allergy','Prescription','Summary']
    print('Select an index needed to be updated: ')
    for count, value in enumerate(category, 1):
        print(f'{count}. {value}')
    opt = 0
    data = ''
    while True:
        try:
            opt = int(input('Enter :'))
            if opt > 0 and opt <= len(category):
                data = input(f'Update {category[opt - 1]}: ')
                break
            print('Invalid, try again')

        except ValueError:
            print('Invalid, try again')
            continue
    pos = opt + 13  # line position

    DB.updateMeasurement(pos, data, recID)
    checkRecord(recid=recID)

