from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.raptorsupplies.com/pd/zurn/qh7')
bsh = BeautifulSoup(html.read(), 'html.parser')

# print(bsh.h2)
# print(bsh.h1)
# print(len(bsh.h1,))
r = bsh.get(html)
soup = BeautifulSoup(r.text, 'html.parser')
for heading in soup.find_all("h1"):
    print(heading.name + ' ' + heading.text.strip())
