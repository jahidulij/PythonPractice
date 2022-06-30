import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
# print(trs[0].next_sibling)
# print(trs[0].next_siblings)
# print(trs[1].previous_sibling)
print(list(trs[0].next_siblings))
