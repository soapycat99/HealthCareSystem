import HCS

def enterInfo():
    username = input('Enter ID: ')
    password = input('Enter passworld: ')
    return username, password

def verifyInfo(username, password):
    HCS.verifyInfo(username,password)

def signUp():
    firstName = input('First name: ')
    lastName = input('Last name: ')
    phoneNumber = input('Phone number: ')
    username = input('Username : ')
    password = input('Password: ')
    HCS.signUp(firstName, lastName, phoneNumber, username, password)
    return [firstName, lastName, phoneNumber, username, password]

def main():
    info = signUp()
    for i in info:
        print(i)

if __name__ == "__main__":
    main()