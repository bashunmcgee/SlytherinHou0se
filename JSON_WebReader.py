import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Url Here - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1634302.json'

    data = urllib.request.urlopen(url).read()

sum = 0
count = 0
info = json.loads(data)

#print('User Count :', len(info))

for item in info['comments']:
    sum = sum +  int(item['count'])
    count = count + 1
print('Sum : ', sum)
print('Count : ', count)
