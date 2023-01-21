import requests
from bs4 import BeautifulSoup

url = 'https://stage.raptorsupplies.com/pd/merit/08834154465'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
page_data = soup.find('ul', class_="items breadcrumb")
for data in page_data:
    print(data.text)



