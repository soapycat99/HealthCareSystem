import Interface as inf
import os
import sys
import Database.Account.Account as ac



def main():
    accID = None
    actor = None
    while True:
        result = inf.logIn()
        if result !=None:
            accID,actor= result
            break
        else:
            print('Wrong id/password. Please type again')


    obj = f'ac.{actor}({accID})'
    user = eval(obj)
    # print(user.dailyList)
    # user.readPayment()

    while True:
        opt = inf.showFunc(user.func)
        if opt == len(user.func) - 1:
            print('SYSTEM EXIT')
            sys.exit()
        eval(f'user.{user.actFunc[opt]}')
        print('-'*75)
        # user.checkRecord()
if __name__ == "__main__":
    main()