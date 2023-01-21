# Find The Product Specifications
import requests
from bs4 import BeautifulSoup

urls = "https://stage.raptorsupplies.com/pd/merit/08834154465"
r = requests.get(urls)
soup = BeautifulSoup(r.content, 'html.parser')
product_info = soup.find('table', class_="table").find_all("td")
# print(product_info)
a = 0
for index in product_info:
    a += 1
    z = index.text
    # print(z)
    # print(a)
    if a == 1:
        print(z, end=" = ")
    elif a == 2:
        print(z)
    elif a == 3:
        print(z, end=" = ")
    elif a == 4:
        print(z)
    elif a == 5:
        print(z, end=" = ")
    elif a == 6:
        print(z)
    elif a == 7:
        print(z, end=" = ")
    elif a == 8:
        print(z)
