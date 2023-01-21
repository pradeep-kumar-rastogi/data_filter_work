# get price in product page
import requests
from bs4 import BeautifulSoup
urls = "https://www.raptorsupplies.com/pd/helicoil/a1084-2-5en038"
r = requests.get(urls)
soup = BeautifulSoup(r.content, "html.parser")
price = soup.find("div", class_="priceInnerwrap").find_all('span')
for i in price:
    a = i.text.split(' ')[0].replace('$', '')
    print(a)
