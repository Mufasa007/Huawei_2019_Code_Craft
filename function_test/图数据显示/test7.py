# -*- coding: cp936 -*-
import networkx as nx
import matplotlib.pyplot as plt

# 计算1：求无向图的任意两点间的最短路径
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (4, 5), (4, 6), (5, 6)])
# nx.draw(G)
# plt.show()
#
# path = nx.all_pairs_shortest_path(G)
#
# print(path[1:2])

# G = nx.path_graph(5)
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (4, 5), (4, 6), (5, 6)])
# nx.draw(G)
# plt.show()

# path = nx.single_source_shortest_path(G, 1)
# for key in path:
#     print(key,path[key])

paths={}
for n in G:
    paths[n]=nx.single_source_shortest_path(G,n,cutoff=None)
print(paths)
print(paths[1][6])

# print(path[4])
# path1=nx.all_pairs_shortest_path(G)
# print(path1[1][4])

# all_pairs_shortest_path(G,cutoff=None) 返回字典
# 使用函数 single_source_shortest_path

# single_source_shortest_path(G,source,cutoff=None)
