from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())
# tag = doc.title
# tag.string = "Hello" # Change the tag info in main file
# print(tag) # Print out the whole tag info
# print(tag.string) # Print out the tag's string
# tag = doc.find("p") # Find the first tag
# tags = doc.find_all("p")
tags = doc.find_all("p")[0]
print(tags.find_all("b"))
