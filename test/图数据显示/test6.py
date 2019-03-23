#!-*- coding:utf8-*-

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # 建立一个空的无向图G
G.add_edge(2, 3)  # 添加一条边2-3（隐含着添加了两个节点2、3）
G.add_weighted_edges_from([(3, 4, 3.5), (3, 5, 7.0)])  # 对于无向图，边3-2与边2-3被认为是一条边

# print
# G.get_edge_data(2, 3)
# print
# G.get_edge_data(3, 4)
# print
# G.get_edge_data(3, 5)

nx.draw(G)
plt.savefig("wuxiangtu.png")
plt.show()