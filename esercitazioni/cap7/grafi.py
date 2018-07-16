import networkx as nx
import pandas as pd

borders = nx.Graph()
not_borders1 = nx.DiGraph() #solo per riferimento
not_borders2 = nx.MultiDiGraph() #Solo per riferimento

borders.add_node("Italia")

borders.add_nodes_from(["Francia","Croacia","Svizera","Austria","Malta"])
borders.remove_node("Francia")
borders.add_edge("Croacia","Grecia",dist=9)
borders.add_edges_from([("Croacia","Polonia"),("Croacia","Francia"),("Germania","Olanda"),("Germania","Spain")],dist=11)
borders.add_edge("Italia","Francia",dist=8)
borders.add_edge("Italia","Croacia",dist=7)
borders.add_edge("Italia","Svizera",dist=6)
borders.add_edge("Italia","Austria",dist=5)
borders.add_edge("Italia","Malta",dist=4)
print(len(borders))
print(borders.nodes(data=True))
print(borders.node)
print(borders.edges())
print(borders["Italia"])
print(borders.degree())

degrees = pd.DataFrame(list(borders.degree()),columns=("country","degree")).set_index("country")
#degrees.sort_index("degree")
degrees2 = degrees.sort_values(by=["degree"]).tail(5)
print(degrees2)


print(list(nx.connected_components(borders)))
print(nx.eigenvector_centrality_numpy(borders))
print(nx.closeness_centrality(borders))