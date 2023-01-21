# compare two different values in database and webpage

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
mycursor.execute("SELECT product_title, product_url, model_no FROM real_tits_dba63")  # show details in database
result = mycursor.fetchall()  # fetchall all data from database
for j in result:  # extract value one by one in database
    product_title = j[0]
    product_url = j[1]
    model_no = j[2]
    # print(product_title)
    r = requests.get(product_url)
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("div", class_="productInfoRight half-collomn", ).find("h1")  # found a product_title in webpage
    title_page = title.text  # use text remove h1 tag in webpage
    # print(title)
    # print(product_title)
    add_content = "REAL-TITE PLUGS"
    add_name = add_content + model_no + " " + product_title  # add string and values in product title
    # print(a)
    if add_name == title_page:
        var1 = "Same values Found in databases"
        print(var1)
        ps = "UPDATE real_tits_dba63 SET product_title_test = '" + str(var1) + "' WHERE product_url='" + str(product_url) + "'"
        mycursor.execute(ps)
        obj1.commit()
        print(mycursor.rowcount, "record(s) affected")
    else:
        var2 = "Different values Found in Databases"
        print(var2)
        sqlyog = "UPDATE real_tits_dba63 SET product_title_test = '" + str(var2) + "' WHERE product_url='" + str(product_url) + "'"
        mycursor.execute(sqlyog)
        obj1.commit()
        print(mycursor.rowcount, "record(s) affected")

        # print(add_name)
        # print(title_page)
        # print("Different values Found in Database")
