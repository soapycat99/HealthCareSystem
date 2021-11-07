# import ReadData as rd
from Database import CreateData as cd

# def checkInfo(acc, pw):
#     rd.readInfo(acc, pw)

def signUp(firstName, lastName, phoneNumber, username, password):
    cd.createAccount(firstName, lastName, phoneNumber, username, password)