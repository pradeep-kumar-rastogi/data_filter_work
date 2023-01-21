import requests
from bs4 import BeautifulSoup

url = 'https://www.raptorsupplies.com/l1/abrasives'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find('div', class_="categoryItemsWrap").find_all('a', href=True)
for j in a:
    name = j.text
    page_url = j['href']

    if 'View all' in name:
        s = name.replace('View all', '')
        print(s)
    else:
        print(name)
