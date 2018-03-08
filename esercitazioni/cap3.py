#esercitazione cap3
import urllib.request
import re
from bs4 import BeautifulSoup



URL = input("enter the URL:")

try:
    doc = urllib.request.urlopen(URL)
except:
    print("ERROR")
    quit()

soup = BeautifulSoup(doc)

links = [(link.string,link["href"])
            for link in soup.findAll("a")
            if link.has_attr("href")]

broken=False
for name, url in links:
    dest = urllib.parse.urljoin(URL,url)
    try:
        doc = urllib.request.urlopen(dest)
        doc.close()
    except:
        broken=True
        print(name,url)
        print("ERROR")
        quit()

if not broken:
    print(links)
