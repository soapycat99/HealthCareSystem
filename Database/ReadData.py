# import Account.Account as ac
#3,4
import os
import csv

def readInfo(acc, pw):
    with open('Database/Account/AccDB', 'r') as outfile:
        next(outfile)
        for line in outfile:
            info = [x.strip() for x in line.split('|')]
            if acc == info[3]:
                if pw == info[4]:
                    return info[-3],info[-2]
                else:
                    return None
    return None

def getName(accID):
    with open('Database/Account/AccDB', 'r') as outfile:
        next(outfile)
        for line in outfile:
            info = [x.strip() for x in line.split('|')]
            if accID == info[5]:
                return info[0],info[1]
    return None

def readAppointment(lastName, phoneNumber):
    print(lastName,phoneNumber)
    with open('Database/App.csv', 'r') as f:
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
            with open(f'Database/RecDir/{recid}.txt', 'r') as f:
                try:
                    for line in f:
                        if len(line.split(':')) > 1:
                            info.append(line.split(':')[1].strip())

                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
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
                            return info
                        except Exception as ex:
                            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                            message = template.format(type(ex).__name__, ex.args)
                            print(message)


            except:
                print('Failling check ln and fn')
        return None

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
def getDailyList(accID):

    with open(f'Database/DailyList', 'r') as out:
        # try:
        lines = out.readlines()
        for line in lines[1:]:
            info = line.strip().split(',')
            if info[0] == str(accID):
                return tuple(info[1:])
        return None
