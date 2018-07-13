#esercitazione cap3
import urllib.request
import re
from bs4 import BeautifulSoup



URL = 'https://e-gov.betha.com.br/transparencia/01035-002/con_comprasdiretas.faces'#input("enter the URL:")

try:
    doc = urllib.request.urlopen(URL)
except:
    print("ERROR")
    quit()

soup = BeautifulSoup(doc)

print("start for media id")
t = ''
for tag in soup.findAll("table"):
    if 'tr' in str(tag.get('tbody')):
        t = str((tag.get('tr')))


print(t)

print("fine for media id")
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
    print("OK!!!!!!")
    print(links)
