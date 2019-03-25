#-*- coding:utf8-*-

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

road_nodes = {'a': 1, 'b': 2, 'c': 3}
# road_nodes = {'a':{1:1}, 'b':{2:2}, 'c':{3:3}}
road_edges = [('a', 'b'), ('b', 'c')]

G.add_nodes_from(road_nodes.items())
G.add_edges_from(road_edges)

nx.draw(G)
plt.savefig("youxiangtu.png")
plt.show()