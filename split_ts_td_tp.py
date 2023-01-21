
import mysql.connector
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  attribute_name,attribute_value,model_no,entity_id,l3_name,id,a_val,label,brand,type1,unit1,l4_name,super_attribute_name,Pre_p,Key_value,filter_data  FROM `chrislynn_12_oct_ts` WHERE attribute_name='Thread Size' AND attribute_value LIKE  '%x%' AND attribute_value NOT LIKE '%to%' AND filter_data IS NULL  ")
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
    type1 = fetch[9]
    unit1 = fetch[10]
    l4_name = fetch[11]
    super_attribute_name = fetch[12]
    Pre_p = fetch[13]
    Key_value = fetch[14]
    filter_data = fetch[15]
    if "x" in attribute_value:
        s1 = attribute_value.split(' x ')[0]
        s2 = attribute_value.split(' x ')[1]
        s3 = s1.replace('M','')
        s4 = "rp_" + s2
        z = 'Thread Dia.'
        z1 = 'Thread Pitch'
        # print(attribute_value)
        # print(z, s3)
        # print(z1, s4)
        # print(Key_value)

        unit2 = 'mm'
        unit3 = ''
        pre_p = 'M'
        super_attr = 'Thread Size'
        sql = ("UPDATE `chrislynn_12_oct_ts` SET filter_data ='Done' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        sql = "INSERT INTO `chrislynn_12_oct_ts`(attribute_value,attribute_name,entity_id,model_no,a_val,l3_name,label,brand,type1,unit1,l4_name,super_attribute_name,Pre_p,Key_value) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (attribute_value, z1, entity_id, model_no, s4, l3_name, label, brand, type1, unit3, l4_name, super_attr,Pre_p,Key_value)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)
        sql = "INSERT INTO `chrislynn_12_oct_ts`(attribute_value,attribute_name,entity_id,model_no,a_val,l3_name,label,brand,type1,unit1,l4_name,super_attribute_name,Pre_p,Key_value) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (attribute_value, z, entity_id, model_no, s3, l3_name, label, brand, type1, unit2, l4_name, super_attr,pre_p,Key_value)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)

