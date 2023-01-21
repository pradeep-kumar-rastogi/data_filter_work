
import requests
from bs4 import BeautifulSoup

url = 'https://www.raptorsupplies.com/l1/abrasives'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
link = soup.find('div', class_="categoryItemsWrap").find_all('a', href=True)
l2 = []
l3 = []
for urls_links in link:
    # name = urls_links.text
    page_url = urls_links['href']
    if 'l2' in page_url:
        urls = page_url
        l2.append(urls)
    else:
        s = page_url
        l3.append(page_url)
for p in l2:
    print(p)
for q in l3:
    print(q)


