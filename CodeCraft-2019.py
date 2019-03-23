import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    filename='../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


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


def write_txt(data, path):  # 按照特定格式写入txt文件
    file = open(path, 'w')
    for i in data:
        file.write('(' + str(i)[1:-1] + ')\n')
    file.close()


class data_input:
    def __init__(self, path_road, path_cross, path_car):
        self.path_road = path_road
        self.path_cross = path_cross
        self.path_car = path_car

    def read_txt(self, path):  # txt文件读取
        f = open(path)
        txt = f.read().split('\n')
        data = []
        for i in txt[1:]:
            data_mid = []
            for j in i[1:-1].split(','):
                data_mid.append(int(j))
            data.append(data_mid)
        return data

    def dict_trans(self, data):  # 将原始的数据转换成字典，key为数据id，value为其值
        dict = {}
        for i in data:
            dict[i[0]] = i[1:]
        return dict

    def dict_cross(self, data):
        dict = {}  # key=id，value=index
        for i in range(len(data)):
            dict[data[i][0]] = i
        return dict

    def main(self):
        road = self.read_txt(self.path_road)  # 不需要，转成字典
        cross = self.read_txt(self.path_cross)  # 需要额外转换一个字典（key=id，value=index）
        car = self.read_txt(self.path_car)  # 不需要，转成字典
        road = self.dict_trans(road)
        cross_dict = self.dict_cross(cross)
        return road, cross, cross_dict, car


def main():  # 主程序
    if len(sys.argv) != 5:
        logging.info('please input args: car_path, road_path, cross_path, answerPath')
        exit(1)

    car_path = sys.argv[1]
    road_path = sys.argv[2]
    cross_path = sys.argv[3]
    answer_path = sys.argv[4]

    logging.info("car_path is %s" % (car_path))
    logging.info("road_path is %s" % (road_path))
    logging.info("cross_path is %s" % (cross_path))
    logging.info("answer_path is %s" % (answer_path))

    # to read input file
    dip = data_input(road_path, cross_path, car_path)
    road, cross, dict_cross, car = dip.main()    # 应该可以运行出结果

    # to write output file
    answer_data = []
    for the_car in car:
        graph = graph_tuning(road, dict_cross, len(cross), the_car)
        cross_name = list(range(1, len(cross) + 1))
        d0, d1 = dijkstra_search(graph, cross_name, the_car[1])
        path = dijstra_path(road, cross, d1, the_car[2])
        path.insert(0,the_car[0])
        answer_data.append(path)
        # print('车辆编号%s的最优路径是：'%(the_car[0]),path)

    write_txt(answer_data, answer_path)

if __name__ == "__main__":
    main()
