# create database and create table  and print information sqlyog to python console

import mysql.connector
obj1 = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="pradeep_work"
    )
# print("created connection")
mycursor = obj1.cursor()  # open cursor to execute file

mycursor.execute("SELECT * FROM student")  # show details in database

result = mycursor.fetchall()  # fetchall all data from database
# print(result)
for info in result:
    tudo = ' '.join(map(str, info))  # convert tuple into string  and join
    print(tudo)




