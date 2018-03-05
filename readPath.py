import urllib.request
import re
import os
from os.path import join, getsize
from collections import Counter
import numpy
import pandas
#path = input("enter the path:")
path = "D://test/"
result =[]
for root, path, files in os.walk(path):
    for name in files:
        with open(join(root,name), mode='r') as f:
            print(f.readline())
            result.append(f.name)



dizionario ={"aloha":result}

print(dizionario)
