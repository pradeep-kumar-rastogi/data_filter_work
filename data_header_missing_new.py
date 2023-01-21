import pandas as pd
import mysql.connector
import csv
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  *  FROM `missing_data_header_28_nov` ")
myresult = cur.fetchall()
lis = []
for fetch in myresult:
    li = []
    model_no = fetch[1]
    header = fetch[2]

    if '|' in header:
        print(model_no)


# print(lis)
# with open("C:/Users/hp/Downloads/missing_data_header2.csv", "w", newline="") as filexport:
#     writer = csv.writer(filexport)
#     writer.writerows(lis)
# filexport.close()

