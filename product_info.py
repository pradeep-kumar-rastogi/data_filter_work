import requests
response = requests.get('https://www.raptorsupplies.com/pd/zurn/qh7')
print(response)
print("Status code", response.status_code)
print("Page Length", len(response.content))
# print(response.content)
# print(response.headers)
# print(response.text)



    # print(heading.name + ' ' + heading.text.strip())

