import requests
from bs4 import BeautifulSoup
url = 'https://stage.raptorsupplies.com/pd/merit/08834154465'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
product = soup.find_all()
