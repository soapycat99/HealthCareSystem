import random

class Appointment():
    def __init__(self, firstName: str, lastName: str,
                 phoneNumber: str, doctor: str):
        self.firstName = firstName
        self.lastName = lastName
        self.appID = str(random.randint(100001,999999))
        self.phoneNumber = phoneNumber
        self.doctor = doctor
        # self.time = time

    def saveApp(self,firstName,lastName, phoneNumber, doctor, appID):
        with open('Database/AppDB','a') as outfile:
            outfile.write('\n')
            outfile.write(f'{firstName} | {lastName} | {phoneNumber} | {doctor} | {appID}')


    def checkApp(self):
        return self.firstName, self.lastName, self.phoneNumber, self.doctor

    def updateApp(self):
        pass