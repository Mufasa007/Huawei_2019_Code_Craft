# version1.0
# 使用dijstra最优路径算法
# 处理的核心是cross节点，其他数据都是配角
import time


import data_input
import numpy as np


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


def graph_tuning(road, dict_cross, cross_num, the_car):  # 通过二维数组表示图,权重直接转换成消耗时间
    graph = np.ones((cross_num, cross_num))  # 原始图
    graph *= -1
    graph += np.eye(cross_num)
    speed = the_car[3]  # the_car的功能完结
    
    for key in road:  # 还是需要重新修改成为字典
        if road[key][1] > speed:
            graph[dict_cross[road[key][3]]][dict_cross[road[key][4]]] = road[key][0] / speed
            if road[key][-1] == 1:
                graph[dict_cross[road[key][4]]][dict_cross[road[key][3]]] = road[key][0] / speed
        else:
            graph[dict_cross[road[key][3]]][dict_cross[road[key][4]]] = road[key][0] / road[key][1]
            if road[key][-1] == 1:
                graph[dict_cross[road[key][4]]][dict_cross[road[key][3]]] = road[key][0] / road[key][1]
    return graph


def dijkstra_search(data, data_index, start):
    index = data_index.index(start)
    parent = {}  # 字典映射，更新前级节点
    queue = []  # 优先队列
    queue_out = [[data_index[index], data[index][index], 0]]  # 输出队列

    while len(queue_out) < len(data_index):
        root_node = data_index.index(queue_out[-1][0])  # 当前最优节点
        for i in range(len(data_index)):  # 遍历所有的可能性
            if data[root_node][i] != -1:  # 检查是否可直连，是
                if data_index[i] not in [x[0] for x in queue_out]:
                    queue = priority_queue(queue,
                                           [data_index[i], data[root_node][i] + queue_out[-1][1], queue_out[-1][0]])

        for i in range(len(queue)):  # 0,1
            if queue[i][0] not in [x[0] for x in queue_out]:
                parent[queue[i][0]] = queue[i][-1]
                queue_out.append(queue[i])
                del queue[i]
                break

    return queue_out, parent


def dijstra_path(road, cross, dict, end):
    key = end
    path = []
    while key in dict.keys():
        ## TODO(这里的数据还需继续优化，现在的数据形式太乱了)
        node = dict[key]  # 前一个节点
        for i in cross[key - 1][1:]:
            if i != -1:
                if node in road[i][3:5]:
                    path.insert(0, i)
                    break
        key = node
    return path

def write_txt(data,path): # 按照特定格式写入txt文件
    file = open(path, 'w')
    for i in data:
        file.write('(' + str(i)[1:-1] + ')\n')
    file.close()

def main(road, cross, dict_cross, car):
    answer_data = []
    for the_car in car:
        graph = graph_tuning(road, dict_cross, len(cross), the_car)
        cross_name = list(range(1, len(cross) + 1))
        d0, d1 = dijkstra_search(graph, cross_name, the_car[1])
        path = dijstra_path(road, cross, d1, the_car[2])
        path.insert(0,the_car[0])
        answer_data.append(path)
        # print('车辆编号%s的最优路径是：'%(the_car[0]),path)

    write_txt(answer_data, 'answer.txt')
    # return answer_data



if __name__ == "__main__":
    time_start = time.time()
    road, cross, dict_cross, car = data_input.default()
    answer_data = main(road, cross, dict_cross, car)

    time_end = time.time()
    print('time cost', time_end - time_start, 's')

    # print(road)
    # print(cross)
    # graph = graph_tuning(road, dict_cross, len(cross), car[0])  # 运行正常
    # print(graph)

    # cross_name = list(range(1, len(cross) + 1))
    # print(cross_name)

    # d0, d1 = dijkstra_search(graph, cross_name, car[0][1])  # d0 包含消耗的时间和上一个节点
    # print(d0)
    # print(d1)

    # path = dijstra_path(road, cross, d1, car[0][2])
    # print('最优路线为：', path)

    # print(road)             # [5000, 15, 6, 2, 1, 2, 1]
    # print(cross)          # [1, 5000, 5007, -1, -1]
    # print(dict_cross)     # 1: 0
    # print(car)            # [10000, 18, 50, 8, 3]
