import requests
from bs4 import BeautifulSoup

url = 'https://www.raptorsupplies.com/pd/morse-drum/85-5'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
name = soup.find('div', class_="product-description",).find_all("li")
for element in name:
    print(element.text)
