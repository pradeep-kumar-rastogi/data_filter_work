import mysql.connector
from fractions import Fraction
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute(
    "SELECT  attribute_name,attribute_value,model_no,entity_id,l3_name,id,a_val  FROM `29_l3_14_oct` WHERE type1='Dimension' AND a_val LIKE '%/%' AND polarity1 IS NULL  ")
myresult = cur.fetchall()
# print(myresult)
for fetch in myresult:

    attribute_name = fetch[0]
    attribute_value = fetch[1]
    model_no = fetch[2]
    entity_id = fetch[3]
    l3_name = fetch[4]
    id = fetch[5]
    a_val = fetch[6]
    print(a_val)
    if '/' in a_val and ' ' not in a_val :
        a = a_val.strip('rp_').strip('RP_')
        b = a.strip('"')
        a2 = float(Fraction(b))
        rs = round(a2, 3)
        rs1 = "rp_" + str(rs)
        # print(rs1)
        print(id)

        ra = 'inch'
        sql = ("UPDATE`29_l3_14_oct`  SET a_val ='" + str(
            rs1) + "'  WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(id)
    if '/' in a_val and ' ' in a_val :
        a = a_val.strip('rp_').strip('RP_')
        b = a.strip('"')
        c = b.split(' ')[1]
        d = float(b.split(' ')[0])
        # print(d)
        a2 = float(Fraction(c))
        a3 = d + a2
        rs = round(a3, 3)

        rs1 = "rp_" + str(rs)
        # print(rs1)
        print(id)

        ra = 'inch'
        sql = ("UPDATE `29_l3_14_oct`      SET a_val ='" + str(
            rs1) + "'  WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(id)
