import HCS

def enterInfo():
    username = input('Enter ID: ')
    password = input('Enter passworld: ')
    return username, password

def verifyInfo(username, password):
    if(HCS.verifyInfo(username,password) == True):
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
    HCS.signUp(firstName, lastName, phoneNumber, username, password, category)
    return [firstName, lastName, phoneNumber, username, password, category]

def makeAppointment():
    firstName = input('First name: ')
    lastName = input('Last name: ')
    phoneNumber = input('Phone number: ')
    doctor = input('Doctor: ')
    HCS.makeAppointment(firstName, lastName, phoneNumber, doctor)

def checkAppointment():
    lastName = input('Last name: ')
    phoneNumber = input('Phone number: ')
    info = HCS.checkAppointment(lastName, phoneNumber)
    if info != None:
        print(f'Appoinment ID: {info[4]}')
        print(f'Doctor: {info[3]}')
    else:
        print('Not available')
    # return info[4]

def cancelAppointment(appID):
    HCS.cancelAppointment(appID)

def updateAppointment():
    pass

def cardPayment():
    pass

def createRecord():
    record = []
    record.append(input('First Name: '))
    record.append(input('Last Name: '))
    record.append(input('Address: '))
    record.append(input('Phone Number: '))
    record.append(input('Email: '))
    record.append(input('SSN: '))
    record.append(input('Insurance Name: '))
    HCS.createRecord(record)
def checkRecord():
    pass

def main():
    # info = signUp()
    # for i in info:
    #     print(i)

    # username, password = enterInfo()
    # verifyInfo(username, password)

    # makeAppointment()

    # checkAppointment()
    # cancelAppointment((appID))

    createRecord()

if __name__ == "__main__":
    main()