
import mysql.connector
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  attribute_name,attribute_value,model_no,entity_id,l3_name,id,a_val,label,brand,type1,unit1,l4_name,super_attribute_name,Key_value,check_mark  FROM `29_l3_14_oct`  WHERE type1='range1' AND check_mark !='Done' AND attribute_value LIKE '%to%' AND attribute_value LIKE '%rp_+%' ")
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

    if "to" in attribute_value:

        s1 = attribute_value.split(' to ')[0]
        s2 = attribute_value.split(' to ')[1]
        s3 = s1
        s4 = "rp_" + s2

        # print(attribute_value)
        # print(s3)
        # print(s4)

        sql = ("UPDATE `29_l3_14_oct` SET check_mark ='Done',a_val='"+str(s4)+"',a_val2='"+str(s3)+"' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

