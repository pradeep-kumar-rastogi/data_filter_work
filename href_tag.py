# find href tag in webpage


import requests
from bs4 import BeautifulSoup

url = 'https://www.raptorsupplies.com/l1/abrasives'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
data = soup.find('section', class_="ourBlock categoryListWrap sectionGap").find_all('a', href=True)

for name in data:
    j = name.text
    page = name['href']
    print(name)
    if 'View all' in name:
        s = name.replace('View all', '')
        print(s)
    else:
        print(j)
