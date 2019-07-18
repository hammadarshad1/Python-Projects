import re
import hashpwd

def passwd():
    x=True
    while x:
        password = input('Enter your Password: ')
        if len(password)<6 and len(password)>16:
            break
        elif not re.search("[a-z]",password):
            break
        elif not re.search("[A-Z]",password):
            break
        elif not re.search("[0-9]",password):
            break
        elif not re.search("[A-Z]",password):
            break
        elif not re.search("[@#$%^&*]",password):
            break
        else:
            print('valid Password!!')
            x = False
            pwd = hashpwd.hashPwd(password)
            return pwd
    if x:
        print('Invalid Password!! Try again')
        passwd()