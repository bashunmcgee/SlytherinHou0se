import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
num = 0

url = input('Enter File Name')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1634301.xml'
html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html.decode())
list = tree.findall('comments/comment')
print("Comment Count : ", len(list))

for item in list:
    print("Name : ", item.find('name').text)
    print("Count : ", item.find('count').text)
    sum = sum + int(item.find('count').text)
print("Sum : ", sum)
