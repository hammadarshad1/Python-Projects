import mysql.connector as mysql
import pandas as pd

def login():
    user = input('Enter your User name: ')
    pas = input('Enter your Password: ')
    mydb = mysql.connect(
        host = 'localhost',
        user = '___', # write username of db
        passwd = '__', # write password of db
        database = '___' # put data base name here!!
    )
    check = pd.read_sql_query("SELECT * from logindb where ____ = '"+ user +"' ____ = '"+pas+"'",mydb) # put columns name in place of ___
    if not check.empty:
        if check.iloc[0]['___'] == user: # column nane
            print('Successfully Loged in!')
        else:
            pass
    else:
        print('Your user name or password incorrect!')
    
