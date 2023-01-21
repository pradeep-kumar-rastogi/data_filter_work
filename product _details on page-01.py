import requests
from bs4 import BeautifulSoup
urls = "https://www.raptorsupplies.com/pd/morse-drum/86"
r = requests.get(urls)
soup = BeautifulSoup(r.content, "html.parser")
product = soup.find("div", class_="product-description",).find("p")
product_page = product.text
print(product_page,  "\n")
