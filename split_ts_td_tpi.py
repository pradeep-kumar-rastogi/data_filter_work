
import mysql.connector
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  attribute_name,attribute_value,model_no,entity_id,l3_name,id,a_val,label,brand,type,unit1,l4_name,super_attribute_name,Key_value,remarks  FROM `117_sp_file_18_oct` WHERE remarks='update_on' AND attribute_value LIKE '%-%'  ")
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
    filter_data = fetch[14]

    if "-" in attribute_value:

        s1 = attribute_value.split('-')[0]
        s2 = attribute_value.split('-')[1]
        s3 = s1
        s4 = "rp_" + s2
        z = 'Thread Dia.'
        z1 = 'Thread Per Inch'
        # print(attribute_value)
        # print(z, s3)
        # print(z1, s4)
        # print(key_value)
        # print(id)

        unit2='inch'
        unit3 = ''
        super_attr ='Thread Size'
        sql = ("UPDATE `117_sp_file_18_oct` SET remarks ='Done' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        sql = "INSERT INTO `117_sp_file_18_oct`(attribute_value,attribute_name,entity_id,model_no,a_val,l3_name,label,brand,type,unit1,l4_name,super_attribute_name,Key_value) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (attribute_value, z1, entity_id, model_no, s4, l3_name,label,brand,type,unit3,l4_name,super_attr,key_value)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)
        sql = "INSERT INTO `117_sp_file_18_oct`(attribute_value,attribute_name,entity_id,model_no,a_val,l3_name,label,brand,type,unit1,l4_name,super_attribute_name,Key_value) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (attribute_value, z, entity_id, model_no, s3, l3_name, label, brand, type, unit2, l4_name, super_attr,key_value)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)


