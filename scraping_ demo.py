# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
url = "https://www.raptorsupplies.com/l1/abrasives"
links = []
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a'):
    links.append(link.get('href'))
for link in links:
    print(link)
