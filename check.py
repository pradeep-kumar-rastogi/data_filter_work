# Find The Product Specifications
import requests
from bs4 import BeautifulSoup

urls = "https://stage.raptorsupplies.com/pd/merit/08834154465"
r = requests.get(urls)
soup = BeautifulSoup(r.content, 'html.parser')
product_info = soup.find('table', class_="table").find_all("tr")
for data in product_info:
    d = data.text
    print(d)