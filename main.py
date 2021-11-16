import Interface as inf
import os
import sys
import Database.Account.Account as ac

def main():
    while True:
        if(inf.logIn()):
            break
    print('Granted access')
    sys.exit()

if __name__ == "__main__":
    main()