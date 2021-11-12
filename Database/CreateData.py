from Database.Account import Account as ac
import random
import csv

def createAccount(firstName, lastName, phoneNumber, username, password, category):
    Acc = ac.Account(firstName,lastName,phoneNumber,username,password, category)
    Acc.saveAccount(firstName,lastName,phoneNumber,username,password, Acc.idNum, category)


def createAppointment(info):
    appID = str(random.randint(100001, 999999))
    info.insert(0,appID)

    with open('Database/AppDB.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(info)



def createRecord(record):
    recID = random.randint(1000,9999)
    recID = 'R' + str(recID)
    record.append(recID)

    with open(f'Database/RecDir/{recID}.txt','x') as f:
        category = ['First Name', 'Last Name', 'Address','Phone Number', 'Email','SSN','Insurance Name','Record ID']
        for key,value in zip(category,record):
            f.write(f'{key}: {value}\n')
        f.write('------------------------------\n')

        category = iter(('Weight','Height','Blood Pressure','Pulse'))
        for key in category:
            f.write(f'{key}: N/A\n')
        f.write('------------------------------\n')

        category = iter(('Radiology','Pathology','Allergy','Prescription','Summary'))
        for key in category:
            f.write(f'{key}: N/A\n')
        f.write('------------------------------\n')



        # f.write(f'First Name: {record.pop(0)}\n')
        # f.write(f'Last Name: {record.pop(0)}\n')
        # f.write(f'Address: {record.pop(0)}\n')
        # f.write(f'Phone Number: {record.pop(0)}\n')
        # f.write(f'Email: {record.pop(0)}\n')
        # f.write(f'SSN: {record.pop(0)}\n')
        # f.write(f'Insurance Name: {record.pop(0)}\n')
        # f.write(f'Record ID: {recID}\n')


