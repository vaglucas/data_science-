import urllib.request

try:
    URL = "http://networksciencelab.com"
    with urllib.request.urlopen(URL) as doc:
        html = doc.read()
        print(html)
except:
    print("cloud not open")
