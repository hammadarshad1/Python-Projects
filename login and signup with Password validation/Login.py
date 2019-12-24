import mysql.connector as mysql
import pandas as pd
import hashpwd

def login():
    user = input('Enter your User name: ')
    pas = input('Enter your Password: ')
    pwd = hashpwd.hashPwd(pas)
    mydb = mysql.connect(
        host = 'localhost',
        user = 'write username of db', 
        passwd = 'write password of db', 
        database = 'put database name here!!' 
    )
    check = pd.read_sql_query("SELECT * from logindb where user_name = '"+ user +"' and password = '"+ pwd +"'",mydb) # put columns name in place of ___
    if not check.empty:
        if check.iloc[0]['user_name'] == user: # column name
            print('Successfully Loged in!')
        else:
            pass
    else:
        print('Your user name or password incorrect!')
    
