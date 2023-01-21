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
cur.execute("SELECT  *  FROM `header_missing_29_nov`  WHERE header_missing1 != ''  ")
myresult = cur.fetchall()

for fetch in myresult:
    id = fetch[6]
    header_m = fetch[9]
    c = fetch[10]
    # print(header_m)
    # print(c)
    rs1=''
    rs2=''
    sql = "INSERT INTO `header_missing_29_nov` (mp_id,mp_name,mother_url,child_product_id,child_product_url,child_product_mpn,header_missing,no_of_header) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
    val = (fetch[1],fetch[2],fetch[3],fetch[4],fetch[5],fetch[6],header_m,c)
    cur.execute(sql, val)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")
    sql = ("UPDATE `header_missing_29_nov`  SET header_missing1 ='" + str(
        rs1) + "',no_of_header1 ='" + str(
        rs2) + "'  WHERE   child_product_mpn='" + str(id) + "'")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "records successful Done")

