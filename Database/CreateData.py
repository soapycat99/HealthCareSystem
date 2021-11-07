from Database.Account import Account as ac
from Database import Appointment as app

def createAccount(firstName, lastName, phoneNumber, username, password, category):
    Acc = ac.Account(firstName,lastName,phoneNumber,username,password, category)
    Acc.saveAccount(firstName,lastName,phoneNumber,username,password, Acc.idNum, category)

def createAppointment(firstName, lastName, phoneNumber, doctor):
    App = app.Appointment(firstName, lastName, phoneNumber, doctor)
    App.saveApp(firstName,lastName, phoneNumber, doctor, App.appID)



