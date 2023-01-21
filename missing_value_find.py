import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  *  FROM `header_data_missing_28_nov` WHERE child_product_mpn='FFSSGC-1N' ")
myresult = cur.fetchall()
lis = []
for fetch in myresult:
    li = []
    model_no = fetch[6]
    child_product_dyn_1 = fetch[7]
    child_product_dyn_2 = fetch[8]
    child_product_dyn_3 = fetch[9]
    child_product_dyn_4 = fetch[10]
    child_product_dyn_5 = fetch[11]
    child_product_dyn_6 = fetch[12]
    child_product_dyn_7 = fetch[13]
    child_product_dyn_8 = fetch[14]
    no_h = int(fetch[15])
    header = fetch[16]

    li.append(fetch[1])
    li.append(fetch[2])
    li.append(fetch[3])
    li.append(fetch[4])
    li.append(fetch[5])
    li.append(model_no)
    # li.append(fetch[6])
    # a_val = header.split('|')
    if '|' in header:
        a_val = header.split('|')
        if child_product_dyn_1 == None and no_h >= 1:
            li.append(a_val[0])
            li.append('1')

        if child_product_dyn_2 == None and no_h >= 2:
            li.append(a_val[1])
            li.append('2')
        if child_product_dyn_3 == None and no_h >= 3:
            li.append(a_val[2])
            li.append('3')
        if child_product_dyn_4 == None and no_h >= 4:
            li.append(a_val[3])
            li.append('4')
        if child_product_dyn_5 == None and no_h >= 5:
            li.append(a_val[4])
            li.append('5')
        if child_product_dyn_6 == None and no_h >= 6:
            li.append(a_val[5])
            li.append('6')
        if child_product_dyn_7 == None and no_h >= 7:
            li.append(a_val[6])
            li.append('7')
        if child_product_dyn_8 == None and no_h >= 8:
            li.append(a_val[7])
            li.append('8')
    else:
        if child_product_dyn_1 == None:
            li.append(header)
            li.append('1')

    lis.append(li)
    # print(lis)
# print(lis)
for x in lis:
    if x[8]:
        b = x[0:8]
        a = '|'.join(x[8:])

        # a.split()
        print(b,a)

    # header1 = '|'.join(h)
    #     print(x)
    # sql = "INSERT INTO `missing_data_header_28_nov` (model_no,header_name) VALUES (%s,%s) "
    # val = (mpn,header1)
    # cur.execute(sql, val)
    # mydb.commit()
    # print(cur.rowcount, "record(s) affected")
