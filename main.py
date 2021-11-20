import Interface as inf
import os
import sys
import Database.Account.Account as ac



def main():
    while True:
        accID = None
        actor = None
        opt = inf.welcomeInf()

        if opt == 1:
            while True:
                result = inf.signUp()
                if result != None:
                    accID, actor = result
                    break
                else:
                    print('Unvailable username, please select another one')
        elif opt == 2:
            while True:
                result = inf.login()
                if result !=None:
                    accID,actor= result
                    break
                else:
                    print('Wrong id/password. Please type again')
        else:
            print('SYSTEM EXIT')
            sys.exit()

        obj = f'ac.{actor}({accID})'
        user = eval(obj)

        while True:
            opt = inf.showFunc(user.func)

            if opt == len(user.func) - 2:
                break
            elif opt == len(user.func) - 1:
                print('SYSTEM EXIT')
                sys.exit()
            eval(f'user.{user.actFunc[opt]}')
            print('-'*75)

if __name__ == "__main__":
    main()