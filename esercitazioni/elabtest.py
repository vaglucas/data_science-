from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk import LancasterStemmer
import nltk


print(stopwords.words("italian"))

wn = nltk.corpus.wordnet #
print(wn.synsets("cat"))

x=wn.synsets("cat.n.01")
y=wn.synsets("lybx.n.02")
print(x.path_similarity(y))
