# get data in product page
import requests
from bs4 import BeautifulSoup

urls = "https://www.raptorsupplies.com/pd/morse-drum/86"
r = requests.get(urls)
soup = BeautifulSoup(r.content, "html.parser")

page = soup.find("div", class_="productDetailsRight half-collomn").find_all('h2')
for x in page:
    a = x.text
    if a == 'Uses:':
        print("Uses:--\n", x.find_next().text)
    elif a == 'Features:':
        print("Features:---\n ", x.find_next().text)
    elif a == 'Compatible Accessories:':
        print("Compatible Accessories:---\n ", x.find_next().text)
    elif a == 'Standards and Approvals:':
        print("Standards and Approvals:---\n ", x.find_next().text)
    elif a == 'Installation:':
        print("Installation:---\n ", x.find_next().text)
    elif a == 'Frequently Asked Questions:':
        print("Frequently Asked Questions:---\n ", x.find_next().text)
