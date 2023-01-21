
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
mycursor.execute("SELECT product_title product_title, product_url, model_no FROM real_tits_dba63")
results = mycursor.fetchall()  # fetchall all data from database
for result in results:
    product_title = result[0]
    product_url = result[1]
    model_no = result[2]
    # print(product_title)

    r = requests.get(product_url)
    soup = BeautifulSoup(r.content, "html.parser")
    product_page_urls = soup.find("div", class_="productInfoRight half-collomn",).find("h1")
    page_title = product_page_urls.text
    # print(page_title)
    add_content = "REAL-TITE PLUGS"
    add_name = add_content + model_no + " " + product_title
    if add_name == product_page_urls:
        print("same value")
    else:
        print("different")
        print(product_title)

