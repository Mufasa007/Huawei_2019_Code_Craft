# version1.0
# 核心功能：①读取txt文件；②转换数据格式；③生成 data_cross/ data_graph/ data_car
# 改进方向：①使用pandas库直接读取txt中的数据，用于节省程序运算时间；②数据格式进行进一步优化；

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

    def graph_data(self, data):  # 生成特定字典
        data_graph = {}
        for i in data:
            if i[4] not in data_graph.keys():
                # 道路id 0、道路长度 1、最高速度 2、车道数目 3、 连接节点id 4
                data_graph[i[4]] = [i[0], i[1], i[2], i[3], i[5]]
            else:
                data_graph[i[4]].extend([i[0], i[1], i[2], i[3], i[5]])
            if i[6]:
                if i[5] not in data_graph.keys():
                    data_graph[i[5]] = [i[0], i[1], i[2], i[3], i[4]]
                else:
                    data_graph[i[5]].extend([i[0], i[1], i[2], i[3], i[4]])
        for key in data_graph:
            data_graph[key].append(int(len(data_graph[key]) / 5))
        return data_graph

    def dict_data(self, cross):
        road_direction = {}
        for i in cross:
            road_direction[i[0]] = i[1:]
        return road_direction

    def main(self):
        road = self.read_txt(self.path_road)
        cross = self.read_txt(self.path_cross)
        car = self.read_txt(self.path_car)

        data_road = self.graph_data(road)
        data_cross = self.dict_data(cross)
        data_car = self.dict_data(car)
        return data_road, data_cross, data_car


if __name__ == '__main__':
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'
    car_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\car.txt'

    dip = data_input(road_path, cross_path, car_path)
    data_road, data_cross, data_car = dip.main()
    # print(data_road)
    # print(data_cross)
    print(data_car)
