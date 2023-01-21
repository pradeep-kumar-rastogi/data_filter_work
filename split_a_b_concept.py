
import mysql.connector
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  attribute_name,attribute_value,model_no,entity_id,l3_name,id,a_val,label,brand,type1,unit1,l4_name,super_attribute_name,Key_value,check_mark  FROM `29_l3_14_oct`   WHERE type1='Dimension' AND check_mark !='Done' AND attribute_value LIKE '%x%' ")
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
    label = fetch[7]
    brand = fetch[8]
    type = fetch[9]
    unit1 = fetch[10]
    l4_name = fetch[11]
    super_attribute_name = fetch[12]
    key_value = fetch[13]
    check_mark = fetch[14]

    if "x" in attribute_value:

        s1 = attribute_value.split(' x ')[0]
        s2 = attribute_value.split(' x ')[1]
        s3 = s1
        s4 = "rp_" + s2
        z = 'A'
        z1 = 'B'
        # print(attribute_value)
        # print(z, s3)
        # print(z1, s4)
        # print(key_value)
        # print(id)
        k = 1
        k1 = 2
        unit2=''
        unit3 = ''
        super_attr = attribute_name
        sql = ("UPDATE `29_l3_14_oct` SET check_mark ='delete Done' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

        sql = "INSERT INTO `29_l3_14_oct`(attribute_value,attribute_name,entity_id,model_no,a_val,l3_name,label,brand,type1,unit1,l4_name,super_attribute_name,Key_value) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (attribute_value, z, entity_id, model_no, s3, l3_name, label, brand, type, unit2, l4_name, super_attr,k)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)
        sql = "INSERT INTO `29_l3_14_oct`(attribute_value,attribute_name,entity_id,model_no,a_val,l3_name,label,brand,type1,unit1,l4_name,super_attribute_name,Key_value) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (attribute_value, z1, entity_id, model_no, s4, l3_name,label,brand,type,unit3,l4_name,super_attr,k1)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)



