import requests
from bs4 import BeautifulSoup
import os

# url = "https://jahidpqa.wordpress.com/"
url = input("Enter address: ")
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
links = soup.find_all("a")
print("Total Links Found: " + str(len(links)))

content_file = open("contents.txt", 'w')
links_file = open("links.txt", 'w')

urls = []
for link in soup.find_all("a"):
	# print(link)
	# print(link.get("href"))
	content_file.write(f"{link}")
	links_file.write(f'{link.get("href")}\n')
content_file.close()
links_file.close()
