import requests
r = requests.get('http://top.17k.com')
r.encoding = 'utf-8'
print(r.text)