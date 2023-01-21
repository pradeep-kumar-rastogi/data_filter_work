import requests
from bs4 import BeautifulSoup

url = 'https://stage.raptorsupplies.com/pd/merit/08834154465'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
page_data = soup.find('ul', class_="items breadcrumb")
for data in page_data:
    print(data.text)

#















# if page_data[1].text:
#     print("l1 = "+page_data[1].text)
# if page_data[2].text:
#     print("l2 = "+page_data[2].text)
# if page_data[3].text:
#     print("l3 = "+page_data[3].text)
# if page_data[4].text:
#     print("mother = "+page_data[4].text)
# if page_data[5].text:
#     print("mother = "+page_data[5].text)
