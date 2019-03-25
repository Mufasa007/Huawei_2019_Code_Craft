# -*- coding:utf8-*-

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node(1)
G.add_node(2)  # 加点
G.add_nodes_from([3, 4, 5, 6])  # 加点集合
G.add_cycle([1, 2, 3, 4])  # 加环
G.add_edge(1, 3)
G.add_edges_from([(3, 5), (3, 6), (6, 7)])  # 加边集合
nx.draw(G)
plt.savefig("youxiangtu.png")
plt.show()