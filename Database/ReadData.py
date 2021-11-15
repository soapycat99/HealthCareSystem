# import Account.Account as ac
#3,4
import os
import csv

def readInfo(acc, pw):
    with open('Database/Account/AccDB', 'r') as outfile:
        next(outfile)
        for line in outfile:
            info = [x.strip() for x in line.split('|')[3:5]]
            if acc == info[0]:
                if pw == info[1]:
                    print('Yayyy')
                    return True
                else:
                    return False
    return False
def getName(accID):
    with open('Database/Account/AccDB', 'r') as outfile:
        next(outfile)
        for line in outfile:
            info = [x.strip() for x in line.split('|')]
            if accID == info[5]:
                return info[0],info[1]
    return None

def readAppointment(lastName, phoneNumber):
    with open('Database/AppDB.csv', 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for line in csvreader:
            if lastName == line[2]:
                if phoneNumber == line[3]:
                    return line
        return None

def readRecord(fn,ln,recid):
    dir = '/Users/soapycat/PycharmProjects/HealthCareSystem/Database/RecDir'
    info = []
    if recid != None:
        try:
            with open(f'Database/RecDir/{recid}.txt','r') as f:
                try:
                    for line in f:
                        if len(line.split(':'))>1:
                            info.append(line.split(':')[1].strip())
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print('loi o day ne')
                    print(message)
            return info

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('loi o day ne')
            print(message)
            return None


    else:
        for filename in os.listdir(dir):
            try:
                with open(f'Database/RecDir/{filename}', 'r') as f:
                    firstName = f.readline().split(':')[1].strip()
                    lastName = f.readline().split(':')[1].strip()
                    if fn == firstName and ln == lastName:
                        info.append(firstName)
                        info.append(lastName)
                        try:
                            for line in f:
                                if len(line.split(':'))>1:
                                    info.append(line.split(':')[1].strip())
                        except Exception as ex:
                            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                            message = template.format(type(ex).__name__, ex.args)
                            print(message)
                return info

            except:
                print('Failling check ln and fn')

def readInvoice(accID):
    invList = []
    with open('Database/Invoice', 'r') as outfile:
        next(outfile)
        for line in outfile:
            info = [x.strip() for x in line.split('|')]
            if accID == info[0]:
                invList.append(info[1:])
    if len(invList)>0:
        return invList
    return None

def readPayment(refNum,firstName,lastName):
    if refNum == None:
        with open('Database/PaymentInfo.csv', 'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for line in csvreader:
                if firstName == line[1]:
                    if lastName == line[2]:
                        return line
            return None

    else:
        with open('Database/PaymentInfo.csv', 'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for line in csvreader:
                if refNum == line[0]:
                    print(line)
                    return line
            return None