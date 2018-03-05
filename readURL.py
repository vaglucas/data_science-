import urllib.request
import re
from collections import Counter
URL = input("enter the URL:")

try:
    doc = urllib.request.urlopen(URL)
except:
    print("ERROR")
    quit()

html = doc.read().decode().lower()

html = re.findall(r"\w+",html)
print("===========RESULT=============")
print(Counter(html).most_common(50))
