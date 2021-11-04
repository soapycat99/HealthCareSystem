class Appointment():
    def __init__(self, firstName: str, lastName: str, appID: str, phoneNumber: str, doctor: str, time , timeStamp):
        self.firstName = firstName
        self.lastName = lastName
        self.appID = appID
        self.phoneNumber = phoneNumber
        self.doctor = doctor
        self.time = time
        self.timeStamp = timeStamp


    def checkApp(self):
        return self.firstName, self.lastName, self.phoneNumber, self.doctor

    def updateApp(self):
        pass