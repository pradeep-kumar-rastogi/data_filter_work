import requests
from bs4 import BeautifulSoup
import mysql.connector
obj1 = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="pradeep_work"
)
# database
mycursor = obj1.cursor()  # open cursor to execute file
mycursor.execute("SELECT l3_name, parent_name, product_url FROM real_tits_dba63")
data = mycursor.fetchall()  # fetchall all data from database
for result in data:
    l3_name = result[0]
    parent_name = result[1]
    product_url = result[2]
    # print(product_url)
    r = requests.get(product_url)
    soup = BeautifulSoup(r.content, "html.parser")
    page_urls = soup.find("ul", class_="items breadcrumb")
    bread_crumb = page_urls
    # for x in bread_crumb:
    #     print(x.text)
    x = 0
    for data in bread_crumb:
        x += 1
        a = data.text
        if x == 4:
            # print('l3_name = ', a)
            if a.strip() == l3_name:
                yy = "Match Data Found"
                print(yy)
                data_up_2 = "UPDATE real_tits_dba63 SET l3_name_test = '" + str(yy) + "' WHERE product_url='" + str(
                    product_url) + "'"
                mycursor.execute(data_up_2)
                obj1.commit()
                print(mycursor.rowcount, "record(s) affected")

            else:
                yy_1 = "No Match Data Found"
                print(yy_1)
                data_up_3 = "UPDATE real_tits_dba63 SET l3_name_test = '" + str(yy_1) + "' WHERE product_url='" + str(
                    product_url) + "'"
                mycursor.execute(data_up_3)
                obj1.commit()
                print(mycursor.rowcount, "record(s) affected")

        elif x == 6:
            # print("parent_name= ", a)
            if a == parent_name:
                xx = "Match Data Found"
                print(xx)
                data_up = "UPDATE real_tits_dba63 SET parent_name_test = '" + str(xx) + "' WHERE product_url='" + str(
                    product_url) + "'"
                mycursor.execute(data_up)
                obj1.commit()
                print(mycursor.rowcount, "record(s) affected")

            else:
                xx_1 = "No Match Data Found"
                print(xx_1)
                data_up_1 = "UPDATE real_tits_dba63 SET parent_name_test = '" + str(xx_1) + "' WHERE product_url='" + str(product_url) + "'"
                mycursor.execute(data_up_1)
                obj1.commit()
                print(mycursor.rowcount, "record(s) affected")
