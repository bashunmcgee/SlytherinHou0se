import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import ssl

#ByPasses Security errors 3 lines SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum = 0

url = input('Enter -')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1634299.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:

    sum = sum + int(tag.contents[0])
print(sum)
