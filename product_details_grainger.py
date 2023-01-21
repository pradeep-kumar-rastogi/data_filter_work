import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.0.0 Safari/537.36"}

url = 'https://www.123securityproducts.com/catalog/product/view/id/31829/s/rb1224/category/2/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

title = soup.find_all('th', {'class':'label'})
print(title)
title2 = soup.find_all('td', {'class':'data'})
print(len(title2))
print(title2)