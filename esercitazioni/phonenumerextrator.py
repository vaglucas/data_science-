import urllib.request
import re
from collections import Counter


test = "3284107661 adasdjas 328-4107661 jasdk asdij n +39 328 410 7661  +393284107661"
print(re.findall(r"((\+?)((\d{2,3})|(\d{2,3}\-?\n?)(\s?\-?))((\d{2,3})((\s+\-*)?)(\d{3,8})))",test))


URL = input("enter the URL:")

try:
    doc = urllib.request.urlopen(URL)
except:
    print("ERROR")
    quit()

html = doc.read().decode().lower()

print("===========RESULT=============")
html = re.findall(r"((\+?)((\d{2,3})|(\d{2,3}\-?\n?)(\s?\-?))((\d{2,3})((\s+\-*)?)(\d{3,8})))",html)
print(html)
