import Database.DBControl as DB
import sys
import time
import ReceiptOutput.DispenserControl as RD
import datetime
from pwinput import pwinput
from prettytable import PrettyTable


funcList = ['updateGeneralRecord','updateMeasurement','updateTreatment','addPatient']
option = ['Update General Record','Update Measurement','Update Treatment',"Add into doctor's list"]

def login(username = None, password = None):
    if username == None and password == None:
        username = input('ID: ')
        password = pwinput('Passworld: ')
    result = verifyInfo(username,password)
    return result


def verifyInfo(username, password):
    return DB.verifyInfo(username,password)

def signUp():
    firstName,lastName,phoneNumber,username,category = None,None,None,None,None
    while True:
        firstName = input('First name: ')
        lastName = input('Last name: ')
        phoneNumber = input('Phone number: ')
        username = input('Username : ')
        while True:
            password = pwinput('Password: ')
            retypePassword = pwinput('Retype Password: ')
            if password == retypePassword:
                break
            else:
                print("Password retyped doesn't match")

        print('Choose your category')
        categories = ['Patient', 'Staff', 'Nurse', 'Doctor', 'CEO']
        for count, key in enumerate(categories, 1):
            print(f'{count}. {key}')

        while True:
            try:
                opt = 0
                opt = int(input('Select(1-5): '))
                if opt <=0 or opt >5:
                    continue
                else:
                    category = categories[opt-1]
                    break
            except ValueError:
                continue



        try:
            accID,actor = DB.signUp(firstName, lastName, phoneNumber, username, password, category)
            print(accID,actor)
            return accID,actor

        except Exception:
            continue

def makeAppointment(fn, ln):
    info = []
    if fn == None and ln == None:
        info.append(input('First name: '))
        info.append(input('Last name: '))
    else:
        info.append(fn)
        info.append(ln)

    while True:
        number = input('Phone number: ')
        if number.isdigit():
            info.append(number)
            break
    print('Doctor List: ')

    #Select doctor
    docList = ['Anh Nguyen','Quan Huynh','Sheldon Cooper','Howard Wolowitz']
    for count,value in enumerate(docList,1):
        print(f'{count}. {value}')
    while True:
        try:
            opt = int(input('Choose: '))
            if opt <= 1 or opt > 4:
                continue
            info.append(docList[opt-1])
            break
        except Exception:
            continue

    while True:
        today = datetime.datetime.now()
        try:
            month = input('Month(MM): ')
            day = input('Day(DD): ')
            year = input('Year(YYYY): ')
            appDate = f'{day}/{month}/{year} 0:00'
            appDate = datetime.datetime.strptime(appDate, "%d/%m/%Y %H:%M")
            if today < appDate:
                year = year[-2:]
                appDate =  f'{month}/{day}/{year}'
                info.append(appDate)
                break
            else:
                print('No later than current time')
                continue
        except Exception:
            continue

    info.append(input('Time(h:mm p): '))
    DB.makeAppointment(info)
    print('Appointment booked!')

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

def cardPayment(receipt,accID):
    # print('Card number: 123456789')
    # print('PIN: 123')
    invNum,amount,des = receipt
    print(f'Invoice: {invNum}')
    input('Card number: ')
    input('PIN: ')
    timer = 0
    loading = "Loading: [----------]"
    backtrack = '\b' * len(loading)

    while timer < 5:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-", "=", 1)
        time.sleep(0.5)
        timer += 0.5

    time.sleep(0.5)
    sys.stdout.write(backtrack)
    print(loading + " Payment Completed!")
    content,current_time,today = RD.dispenseReceipt(amount,des)
    print(content)

    firstName,lastName = DB.getName(accID)
    payInfo = [firstName,lastName,amount,today,current_time]

    DB.storePayment(payInfo)

    # TODO: delete invoice paid

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

def getRecord(fn = None, ln = None, recid = None):

    info = DB.checkRecord(fn, ln, recid)
    info1 = info[:8]
    info2 = info[8:-1]
    summary = info[-1]

    key1 = ['First Name', 'Last Name', 'Address', 'Phone', 'Email', 'SSN', 'Insurance Name', 'RecID']
    key2 = ['Weight', 'Height', 'Blood Pressure', 'Pulse', 'Radiology', 'Pathology', 'Allergy', 'Prescription']

    for k1, i1, k2, i2 in zip(key1, info1, key2, info2):
        firstVal = f'{k1}: {i1}'
        if k2 != 'Weight':
            print(f'{firstVal:<45} {k2}: {i2:<25} ')
        else:
            print(f'{firstVal:<45} {k2}: {i2:<25} Summary: {summary}')
    print('-' * 75, '\n')

    recID = info1[-1]
    return recID

def checkRecord(fn = None, ln = None, recid = None):
    return getRecord(fn,ln,recid)
    # showRecordOption(recID)

def showStaffOption(recID):
    '''Show options for staff actor after checking record, and implement the selected function'''
    actOpt = [option[0],option[-1],'X']
    actFunc= [funcList[0],funcList[-1]]
    for count,key in enumerate(actOpt,1):
        print(f'{count}. {key}')

    call_function(recID,actFunc)


def showNurseOption(recID):
    for count,key in enumerate([option[1],'X'],1):
        print(f'{count}. {key}')
    call_function(recID,[funcList[1]])


def showDoctorOption(recID):
    for count,key in enumerate([option[2],'X'],1):
        print(f'{count}. {key}')
    call_function(recID,[funcList[2]])


def call_function(recID,actFunc:list):
    opt = 0
    l = len(actFunc)
    print(type(actFunc),actFunc,l)
    while True:
        try:
            opt = int(input('Input: '))
            if opt >= 1 and opt <= l:
                globals()[actFunc[opt - 1]](recID)
                break
            elif opt == l+1:
                break
            print('Invalid, try again')
        except ValueError:
            print('Invalid, try again')
            continue

    if opt != l+1:
        checkRecord(recid=recID)

def showRecordOption(recID):
    # TODO: Delete this function after done testing
    print('Select Option')
    for count,key in enumerate(['Update General Record','Update Measurement',
                                'Update Treatment',"Add into doctor's list",'X'],1):
        print(f'{count}. {key}')
    opt = 0
    option = ['updateGeneralRecord','updateMeasurement','updateTreatment','addPatient']


    while True:
        try:
            opt = int(input('Input: '))
            if opt >= 1 and opt <=4:
                globals()[option[opt-1]](recID)
                break
            elif opt == 5:
                break
            print('Invalid, try again')
        except ValueError:
            print('Invalid, try again')
            continue

    if opt != 5:
        checkRecord(recid=recID)

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
            receipt = tuple(invList[order])
            cardPayment(receipt,accID)

def payingAlert(num):
    opt = None
    order = None

    while opt not in ('Y','N'):
        opt = input('Paying invoice(Y/N)?: ').upper()
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
    opt = 0
    print('1. Reference number')
    print('2. Name')
    while True:
        try:
            opt = int(input('Search by: '))
        except:
            continue
        if opt in (1,2):
            break

    refNum,lastName,firstName = None,None,None
    info = []
    if opt == 1:
        refNum = input('Reference Number: ')
        info = DB.readPayment(refNum)
    else:
        firstName = input('First Name: ')
        lastName = input('Last Name: ')
        info = DB.readPayment(lastName = lastName,firstName = firstName)

    if info != None:
        key = ['Reference Number','First Name','Last Name','Amount','Date','Time']
        for k,i in zip(key,info):
            print(f'{k:>16}: {i:}')
    else:
        print('Wrong input!')

def checkDailyList(*args):
    for arg in args:
        getRecord(recid=arg)

def addPatient(recID):
    print('1. Anh Nguyen\n'
          '2. Quan Huynh\n'
          '3. Sheldon Cooper\n'
          '4. Howard Wolowitz\n')

    opt = int(input('Choose doctor: '))
    DB.addPatient(recID,opt)


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

def readSalaryList():
    salaryList = DB.readSalaryList()
    salTable = PrettyTable()
    salTable.field_names = ['First Name','Last Name','ID','Position','Salary']
    salTable.add_rows(salaryList)
    # for info in salaryList:
    #     salTable.add_row(info)

    print(salTable)