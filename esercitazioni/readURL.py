import urllib.request
import re
from collections import Counter
URL = "https://e-gov.betha.com.br/transparencia/01035-002/con_comprasdiretas.faces"

try:
    doc = urllib.request.urlopen(URL)
except:
    print("ERROR")
    quit()

html = doc.read()

html = re.findall(r"\w+",html)
print("===========RESULT=============")
print(Counter(html).most_common(50))
