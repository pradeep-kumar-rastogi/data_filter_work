# connection creation in database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Mysql@#1234")

# print(mydb_1.connection_id)
create = mydb.cursor()
create.execute("CREATE DATABASE USERS1")
