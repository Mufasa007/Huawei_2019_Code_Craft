# *** 输入图，

def priority_queue(data, d0):  # 自建优先队列格式
    state = 1
    for i in range(len(data)):
        if d0[1] < data[i][1]:
            data.insert(i, d0)
            state = 0
            break
    if state:
        data.append(d0)
    return data


def dijkstra_search(graph, from_index, to_index,data_index=None):
    ## data_index 可以存储节点的名称输出路径也输出节点的名称
    if data_index is None:data_index = list(range(len(graph)))

    parent = {}  # 字典映射，更新前级节点
    queue = []  # 优先队列
    queue_out = [[data_index[from_index], graph[from_index][from_index], 0]]  # 输出队列

    while len(queue_out) < len(data_index):
        root_node = data_index.index(queue_out[-1][0])  # 当前最优节点
        # print(root_node)
        for i in range(len(data_index)):  # 遍历所有的可能性
            if graph[root_node][i] != -1:  # 检查是否可直连，是
                if data_index[i] not in [x[0] for x in queue_out]:
                    queue = priority_queue(queue,
                                           [data_index[i], graph[root_node][i] + queue_out[-1][1], queue_out[-1][0]])
        # print(queue)    # 检查优先队列的情况 [['C', 1], ['B', 5]]

        for i in range(len(queue)):  # 0,1
            # print(queue[i][0])
            if queue[i][0] not in [x[0] for x in queue_out]:
                parent[queue[i][0]] = queue[i][-1]
                queue_out.append(queue[i])
                del queue[i]
                break

    key = to_index
    path_dijstra = [key]
    while key in parent.keys():
        path_dijstra.insert(0, parent[key])
        key = parent[key]
    return path_dijstra


if __name__ == "__main__":
    data_weight = [[0, 5, 1, -1, -1, -1], [5, 0, 2, 1, -1, -1], [1, 2, 0, 4, 8, -1], [-1, 1, 4, 0, 3, 6],
                   [-1, -1, 8, 3, 0, -1], [-1, -1, -1, 6, -1, -1]]
    path = dijkstra_search(data_weight, 0, 5)
    print(path)


