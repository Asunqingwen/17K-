import requests
from lxml import etree

r = requests.get('http://top.17k.com')
r.encoding = 'utf-8'
html = etree.parse(r.text)
result = html.xpath("//@class='TABBOX'")
print(result)