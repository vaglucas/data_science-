import networkx as nx
import pandas as pd

sc = nx.read_adjlist(open("soc-Epinions1.txt","rb"))
print(sc.edges())

pd_sc = pd.DataFrame(list(sc.edges()))
print(pd_sc.describe())