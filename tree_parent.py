import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# print(trs[0].parent.name)
print(list(trs[0].children)) # descendants/ children/ contents all are same
