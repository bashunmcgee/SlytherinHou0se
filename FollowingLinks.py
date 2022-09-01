import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Selasi.html'
#Counting or iterating through Sequence
counting = int(input('Enter count '))
#Position to deal with
position = int(input('Enter position '))

#Opens Connection
html = urllib.request.urlopen(url, context=ctx).read()
#BeautifulSoup Library begin parsing
soup = BeautifulSoup(html, "html.parser")
#Searches for Tags
tags = soup('a')
#Counter
count = 0
#Begin within Counting
#count = count + 1
for tag in tags:
    print(tag.get('href', None))
