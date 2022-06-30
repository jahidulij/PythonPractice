import requests
import re
from bs4 import BeautifulSoup

url = "https://jahidpqa.wordpress.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
links = soup.find_all("a")
print(len(links))

# Find all the urls in the page and put those in a list
urls = []
for link in soup.find_all("a"):
	urls.append(link.get("href"))
print(urls)

new_urls = []
# Remove None from the list
for url in urls:
	if url != None:
		new_urls.append(url)
print(new_urls)

# Find specific urls
u = "https://jahidpqa"

for r in new_urls:
	if u in r:
		print(r)
	else:
		continue







