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
    with open(f'Database/RecDir/{recID}.txt','x') as f:
        f.write(f'First Name: {record.pop(0)}\n')
        f.write(f'Last Name: {record.pop(0)}\n')
        f.write(f'Address: {record.pop(0)}\n')
        f.write(f'Phone Number: {record.pop(0)}\n')
        f.write(f'Email: {record.pop(0)}\n')
        f.write(f'SSN: {record.pop(0)}\n')
        f.write(f'Insurance Name: {record.pop(0)}\n')
        f.write(f'Record ID: {recID}\n')
        f.write('------------------------------\n')

