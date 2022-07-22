from urllib import request
import xml.etree.ElementTree as ET

# Open URL
url = 'http://py4e-data.dr-chuck.net/comments_1579942.xml'
print("Retrieving", url)
html = request.urlopen(url)

# Read HTML
data = html.read()
print("Retrieved", len(data), "characters")

# Digging to the section
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount = len(results)

sum = 0

# Find out the expected result
for result in results:
    sum += float(result.find('count').text)

print(icount)
print(sum)
