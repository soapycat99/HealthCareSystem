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
    # checkAppointment(lastName, phoneNumber)

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

def checkRecord(fn, ln, recid):
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

def updateGeneralRecord(recID):
    category = ['First Name', 'Last Name', 'Address', 'Phone Number','Email','SSN','Insurance Name']
    print('Choose category to be updated:')
    opt = 0
    data = ''
    for count, value in enumerate(category,1):
        print(f'{count}. {value}')
    while True:
        opt = int(input('Input: '))
        if opt>=1 and opt<=len(category):
            data = input(f'Update {category[opt-1]}: ')
            break
    DB.updateGeneralRecord(opt-1,data,recID)