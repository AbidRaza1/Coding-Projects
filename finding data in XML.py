#Importing libraries

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Security Certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = input('Enter...')

#Opening URL
y = urlopen(x, context=ctx).read()

#Parsing Data
y = ET.fromstring(y)

#Finding Comments
y = y.findall('comments/comment')

#Initializing Counter variable
w = 0

#Loop for finding words
for i in y:
        a = int(i.find('count').text)
        w = a + w
print(w)




