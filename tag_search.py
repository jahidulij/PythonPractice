import requests
from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# result = doc.find("option")
result = doc.find_all("option")
print(result)

