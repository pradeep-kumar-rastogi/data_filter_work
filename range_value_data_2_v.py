
import mysql.connector
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  attribute_name,attribute_value,model_no,entity_id,l3_name,id,a_val,label,brand,type1,unit1,l4_name,super_attribute_name,Pre_p,Key_value,filter_data  FROM `chrislynn_12_oct_ts` WHERE  attribute_name='Thread Size' AND attribute_value LIKE '%,%' AND attribute_value NOT LIKE '%to%'  ")
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

    if ',' in attribute_value:
        a = attribute_value.count(',')
        if a == 2:
            b = attribute_value.replace('rp_', '')
            i = b.split(', ')[0]
            i1 = b.split(', ')[1]
            i2 = b.split(', ')[2]
            # i3 = b.split(', ')[3]
            # i4 = b.split(', ')[4]

            i = 'rp_' + i
            i1 = 'rp_' + i1
            i2 = 'rp_' + i2
            # i3 = 'rp_' + i3
            # i4 = 'rp_' + i4
            print(attribute_value)
            print(i, i1, i2)
            j = 1
            j1 = 2
            j2 = 3
            # j3 = 4
            # j4 = 5
            # attribute_name='Thread Size'
            sql = ("UPDATE `chrislynn_12_oct_ts` SET attribute_value ='" + str(i) + "',Key_value ='" + str(
                j) + "',attribute_name='"+str(attribute_name)+"' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            sql = "INSERT INTO `chrislynn_12_oct_ts` (attribute_value,attribute_name,entity_id,model_no," \
                  "l3_name,brand,type1,Key_value,label) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s) "
            val = (i1, attribute_name, entity_id, model_no, l3_name, brand, type1, j1, label)
            cur.execute(sql, val)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
            print(id)
            sql = "INSERT INTO `chrislynn_12_oct_ts` (attribute_value,attribute_name,entity_id,model_no,l3_name,brand,type1,Key_value,label) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s)"
            val = (i2, attribute_name, entity_id, model_no, l3_name, brand, type1, j2, label)
            cur.execute(sql, val)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
            print(id)
            # sql = "INSERT INTO `chrislynn_12_oct_ts` (attribute_value,attribute_name,entity_id,model_no,l3_name,brand,type1,Key_value,label) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s,%s)"
            # val = (i3, attribute_name, entity_id, model_no, l3_name, brand, type1, j3, label)
            # cur.execute(sql, val)
            # mydb.commit()
            # print(cur.rowcount, "record(s) affected")
            # print(id)

