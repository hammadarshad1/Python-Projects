import password as pas
import mysql.connector as mysql
import pandas as pd
import Login

def signup():
    user = input('Enter your User name: ')
    password = pas.passwd()
    mydb = mysql.connect(
        host = 'localhost',
        user = '___', #Write user of db
        passwd = '___', # Write Password of db
        database = '___'
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO logindb (____, ___) VALUES ('"+user+"' , '"+password+"')") # column name in place of ____
    mydb.commit()
    print('Account Successfully Created')
    n = input('Do you wish to login (y/n): ')
    if n.lower() == 'y':
        Login.login()
    elif n.lower() == 'n':
        print('GoOd ByE!!!')
    else:
        print('Wrong input!')
