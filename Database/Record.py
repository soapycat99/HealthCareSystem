class Record():
    def __init__(self, firstName: str, lastName: str, address:str, phoneNumber: str, email: str, ssn: str, insuranceName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.ssn = ssn
        self.insuranceName = insuranceName


class Measurement():
    def __init__(self, weight: int, height: int, bloodPressure: int, pulse: int):
        self.weight = weight
        self.height = height
        self.bloodPressure = bloodPressure
        self.pulse = pulse

class Treatment():
    def __init__(self,  labResult: str, radiology: str, pathology: str, allergy: str, prescription: str, summary: str = None):
        self.labResult = labResult
        self.radiology = radiology
        self.pathology = pathology
        self.allergy = allergy
        self.prescription = prescription
        self.summary = summary