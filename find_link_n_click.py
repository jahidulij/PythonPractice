import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# url = "https://jahidpqa.wordpress.com/"
url = input("Enter the url: ")
driver.maximize_window()
driver.get(url)
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
refine_urls = []
for r in new_urls:
    if u in r:
        refine_urls.append(r)
    else:
        continue

print(refine_urls)
for i in refine_urls:
    print(i)
    time.sleep(2)
    driver.get(i)
time.sleep(2)
