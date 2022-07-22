import requests
import re
from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all(["p", "div", "li"])
# tags = doc.find_all(text=re.compile("\$.*")) # Find all the data
tags = doc.find_all(text=re.compile("\$.*"), limit=1) # Limiting the data


for tag in tags:
    print(tag.strip())

