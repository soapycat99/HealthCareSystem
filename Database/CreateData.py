from Database.Account import Account as ac
from Database import Appointment as app
import random

def createAccount(firstName, lastName, phoneNumber, username, password, category):
    Acc = ac.Account(firstName,lastName,phoneNumber,username,password, category)
    Acc.saveAccount(firstName,lastName,phoneNumber,username,password, Acc.idNum, category)

def createAppointment(firstName, lastName, phoneNumber, doctor):
    App = app.Appointment(firstName, lastName, phoneNumber, doctor)
    App.saveApp(firstName,lastName, phoneNumber, doctor, App.appID)

def createRecord(record):
    recID = random.randint(1000,9999)
    recID = 'R' + str(recID)
    with open(f'Database/RecDir/{recID}.txt','w') as f:
        f.write(f'First Name: {record.pop(0)}\n')
        f.write(f'Last Name: {record.pop(0)}\n')
        f.write(f'Address: {record.pop(0)}\n')
        f.write(f'Phone Number: {record.pop(0)}\n')
        f.write(f'Email: {record.pop(0)}\n')
        f.write(f'SSN: {record.pop(0)}\n')
        f.write(f'Insurance Name: {record.pop(0)}\n')
        f.write('------------------------------\n')

