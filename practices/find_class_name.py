import requests
from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all(["p", "div", "li"])
tags = doc.find_all(class_="btn-item")
print(tags)

