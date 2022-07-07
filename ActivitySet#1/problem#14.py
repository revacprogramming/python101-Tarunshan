#Network programming 2
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

content = []
total = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    content.append(tag.contents[0])
    
for i in range(len(content)):
    total = total + int(content[i])
print("Sum:",total)
