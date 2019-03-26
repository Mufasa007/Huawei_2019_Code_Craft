# 2019.03.25    Mufasa
# version3.0    增加道路的宽度因素参与决策

# version4.0
# 优化方向：①使用pandas读写文件加快速度；②找到一个优化的损失函数；
import os
import time
import numpy as np


# *** 数据读写 *** #
class data_wr:  # 数据读写
    def __init__(self, car_path, cross_path, road_path):
        self.car_path = car_path
        self.cross_path = cross_path
        self.road_path = road_path

    def write_txt(self, data, path):  # 写入txt文件，无返回值
        os.chdir(os.getcwd())
        file = open(path, 'w')
        for i in data:
            file.write('(' + str(i)[1:-1] + ')\n')
        file.close()

    def read_txt(self, path):  # 读取txt文件，返回二维数组
        os.chdir(os.getcwd())  # 设置相对路径
        file = open(path, 'r')
        txt = file.read().split('\n')  # 自带分行符
        data = []
        if txt[0][0] == '#':  # 增强程序的鲁棒性（1，跳过文件说明；2，防止数据遗漏）
            txt = txt[1:]
        for i in txt:
            data_mid = []
            for j in i[1:-1].split(','):
                data_mid.append(int(j))
            data.append(data_mid)
        file.close()
        return data

    def dict_trans(self, data):  # 将原始的数据转换成字典，key为数据id，value为其值
        dict = {}
        for i in data:
            dict[i[0]] = i[1:]
        return dict

    def line_cross(self, data):  # 将cross的信息转换特定格式
        dict = {}  # key=id，value=index
        for i in range(len(data)):
            dict[data[i][0]] = i
        return dict

    def line_cross(self, data):  # 将cross的信息转换特定格式
        line = []
        for i in data:
            line.append(i[0])
        return line

    def data_out(self):
        car = self.read_txt(self.car_path)
        cross = self.read_txt(self.cross_path)
        road = self.read_txt(self.road_path)  # 这个需要进行字典转换

        road_dict = self.dict_trans(road)  # road 暂时不做处理
        cross_line = self.line_cross(cross)

        return car, cross, cross_line, road_dict


# *** 单个车辆的dijstra路径规划 *** #
class dijstra_path:
    def __init__(self, car, cross, line_cross, road):
        self.car = car
        self.cross = cross
        self.line_cross = line_cross
        self.road = road

    def priority_queue(self, data, d0):  # 自建优先队列格式,冒泡类型
        state = 1
        for i in range(len(data)):
            if d0[1] < data[i][1]:
                data.insert(i, d0)
                state = 0
                break
        if state:
            data.append(d0)
        return data

    def graph_tuning(self, road, line_cross, the_car):  # 通过二维数组表示图,权重直接转换成消耗时间
        graph = np.ones((len(self.line_cross), len(self.line_cross)))  # 原始图
        graph *= -1
        graph += np.eye(len(self.line_cross))
        speed = the_car[3]  # the_car的功能完结

        for key in road:  # 还是需要重新修改成为字典
            [road_length, road_speed, road_channel, from_id, to_id] = road[key][0:5]
            if road_speed > speed:
                graph[line_cross.index(from_id)][line_cross.index(to_id)] = road_length / (speed * road_channel)
                if road[key][-1] == 1:
                    graph[line_cross.index(to_id)][line_cross.index(from_id)] = road_length / (speed * road_channel)
            else:
                graph[line_cross.index(from_id)][line_cross.index(to_id)] = road_length / (road_speed * road_channel)
                if road[key][-1] == 1:
                    graph[line_cross.index(to_id)][line_cross.index(from_id)] = road_length / (
                            road_speed * road_channel)
        return graph

    def dijkstra_search(self, data, data_index, start):
        index = data_index.index(start)
        parent = {}  # 字典映射，更新前级节点
        queue = []  # 优先队列
        queue_out = [[data_index[index], data[index][index], 0]]  # 输出队列
        while len(queue_out) < len(data_index):
            root_node = data_index.index(queue_out[-1][0])  # 当前最优节点
            for i in range(len(data_index)):  # 遍历所有的可能性
                if data[root_node][i] != -1:  # 检查是否可直连，是
                    if data_index[i] not in [x[0] for x in queue_out]:
                        queue = self.priority_queue(queue,
                                                    [data_index[i], data[root_node][i] + queue_out[-1][1],
                                                     queue_out[-1][0]])
            for i in range(len(queue)):  # 0,1
                if queue[i][0] not in [x[0] for x in queue_out]:
                    parent[queue[i][0]] = queue[i][-1]
                    queue_out.append(queue[i])
                    del queue[i]
                    break
        return queue_out, parent

    def road_path(self, from_id, to_id, parent):
        path = []
        now_id = to_id  # 当前路口id
        next_id = parent[now_id]  # 下个路口id
        while now_id != from_id:
            index = self.line_cross.index(now_id)  # index位置
            for i in self.cross[index][1:]:  # 遍历这个路口的道路id
                if i != -1:
                    # print(self.road[i][3:5])
                    if next_id in self.road[i][3:5]:
                        path.insert(0, i)
                        now_id, next_id = next_id, parent[now_id]
                        break
        return path


if __name__ == '__main__':
    time_start = time.time()

    # **** 原始数据的读取**** #
    car_path = u'car.txt'
    cross_path = u'cross.txt'
    road_path = u'road.txt'
    data_wr = data_wr(car_path, cross_path, road_path)
    car, cross, cross_line, road = data_wr.data_out()

    # **** 数据处理获得所有车辆的路径 **** #
    dijstra_path = dijstra_path(car, cross, cross_line, road)
    path_all = []
    for the_car in car:  # 对每辆车进行遍历
        graph = dijstra_path.graph_tuning(road, cross_line, the_car)
        queue_out, parent = dijstra_path.dijkstra_search(graph, cross_line, the_car[1])
        path = dijstra_path.road_path(the_car[1], the_car[2], parent)
        path.insert(0,the_car[0])
        path_all.append(path)

    # **** 数据写入answer.txt文件 **** #
    data_wr.write_txt(path_all, u'answer.txt')