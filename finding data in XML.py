import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = input('Enter...')
y = urlopen(x, context=ctx).read()
y = ET.fromstring(y)
y = y.findall('comments/comment')
w = 0
for i in y:
        a = int(i.find('count').text)
        w = a + w
print(w)




