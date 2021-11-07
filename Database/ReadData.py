# import Account.Account as ac
#3,4
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

def readAppointment(lastName, phoneNumber):
    with open('Database/AppDB', 'r') as outfile:
        next(outfile)
        for line in outfile:
            info = [x.strip() for x in line.split('|')]
            if lastName == info[1]:
                if phoneNumber == info[2]:
                    return info

        return None