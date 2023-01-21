# get price in product page
import requests
from bs4 import BeautifulSoup
urls = "https://www.raptorsupplies.com/pd/helicoil/a1084-2-5en038"
r = requests.get(urls)
soup = BeautifulSoup(r.content, "html.parser")
price = soup.find("span", class_="actual-price")
# print(type(price.text))
for price_list in price:
    if "$166.64" in price_list:
        # a = price_list.split(' ')[0]
        b = price_list.replace('$', '')
        print("Price:--", b)

