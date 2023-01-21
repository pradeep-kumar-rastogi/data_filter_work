# get price in product page
import requests
from bs4 import BeautifulSoup
urls = "https://www.raptorsupplies.com/pd/helicoil/a1084-2-5en038"
r = requests.get(urls)
soup = BeautifulSoup(r.content, "html.parser")
price = soup.find("span", class_="actual-price")
for i in price:
    b = i.text.replace('$', '').split(' ')[0].replace('/pack', '')
    get = b
    print(get, end='')
