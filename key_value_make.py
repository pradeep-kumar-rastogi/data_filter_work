import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  entity_id,Key_value,id  FROM `chrislynn_12_oct_ts` WHERE attribute_name='Thread size'  ")
myresult = cur.fetchall()

b = []
c = []
prev_value = 'xyz'
for fetch1 in myresult:
    b.append(list(fetch1))
cnt = 0
for fetch in b:
    if prev_value == str(fetch[0]) or prev_value == str('xyz'):
        entity_id = fetch[0]
        key_value = fetch[1]
        cnt += 1
        fetch[1] = str(cnt)
    else:
        cnt = 1
        fetch[1] = '1'
    prev_value = str(fetch[0])
for i in b:
    key1 = i[1]
    id1 = i[2]
    # print(key1,id1)
    sql = ("UPDATE `chrislynn_12_oct_ts` SET Key_value ='" + str(key1) + "' WHERE   id='" + str(
        id1) + "'")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "records successful Done")
