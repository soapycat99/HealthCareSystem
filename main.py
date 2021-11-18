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

    while True:
        opt = inf.showFunc(user.func)
        if opt == 4:
            sys.exit()

        eval(f'user.{user.actFunc[opt]}')
        # user.checkRecord()
        # TODO: fix make appointment -> auto fill name and phone number
if __name__ == "__main__":
    main()