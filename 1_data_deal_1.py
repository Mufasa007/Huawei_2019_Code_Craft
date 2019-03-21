# 先处理road.txt和cross.txt




# 转变成高维度矩阵的数据格式
def map_data(road_path, cross_path):
    pass


def graph_data(road_path):  # 1，读取txt文件；2，根据规则进行数据转换融合
    data_graph = {}
    f = open(road_path)
    txt = f.read().split('\n')
    data = []
    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    for i in data:
        if i[4] not in data_graph.keys():
            data_graph[i[4]] = [i[5]]
        else:
            data_graph[i[4]].append(i[5])
        if i[6]:
            if i[5] not in data_graph.keys():
                data_graph[i[5]] = [i[4]]
            else:
                data_graph[i[5]].append(i[4])
    return data_graph
