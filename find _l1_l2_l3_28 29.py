import requests
from bs4 import BeautifulSoup

url = 'https://stage.raptorsupplies.com/pd/merit/08834154465'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
data = soup.find('ul', class_="items breadcrumb").find_all('li')
x = 0

for page_data in data:
    x += 1
    a = page_data.text
    # print(a)
    # print(x)
    if x == 1:
        print(a)
    elif x == 2:
        print("l1 = ", a)
    elif x == 3:
        print("l2 = ", a)
    elif x == 4:
        print('l3 = ', a)
    elif x == 5:
        print("mother = ", a)
    elif x == 6:
        print("mother = ", a)
