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

def checkAppointment():
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

    else:
        print('wtf why doesnt it work')

def cancelAppointment(appID):
    DB.cancelAppointment(appID)

def updateAppointment():
    pass

def cardPayment():
    print('Card number: 123456789')
    print('PIN: 123')
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

def checkRecord(fn=None, ln=None, recid=None):
    info = DB.checkRecord(fn,ln,recid)
    key = ['First Name', 'Last Name', 'Address', 'Phone', 'Email', 'SSN','Insurance Name', 'RecID']
    for k, i in zip(key,info):
        print(f'{k} : {i}')

def checkInvoice(accID):
    invList = DB.checkInvoice(accID)
    if invList != None:
        key = ['Invoice Number', 'Amount', 'Description']

    for info in invList:
        for k, i in zip(key,info):
            print(f'{k}: {i}')
        print('----------------')

def readPayment():
    pass

def updateGeneralRecord():
    category = ['First Name', 'Last Name', 'Address', 'Phone Number','Email','SSN','Insurance Name']
    print('Choose category to be updated:')
    opt = 0
    for count, value in enumerate(category,1):
        print(f'{count}: {value}')
    while True:
        opt = int(input('Input: '))
        if opt>=1 and opt<=len(category):
            break
    DB.updateGeneralRecord(opt)