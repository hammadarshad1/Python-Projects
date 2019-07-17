print('------------- Welcome to User Managemenr System---------------')


c = input('Do you have an account (y/n): ')
if c.lower() == 'y':
    import Login
    Login.login()
elif c.lower() == 'n':
    import Signup
    Signup.signup()
else:
    print('Choose the right one')