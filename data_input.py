# version1.0    2019.03.21
# 核心功能：①读取txt文件；②转换数据格式；③生成 data_cross/ data_graph/ data_car
# 改进方向：①使用pandas库直接读取txt中的数据，用于节省程序运算时间；②数据格式进行进一步优化；

# version2.0    2019.03.22
# 修改：
# ① 将cross当做数据的核心，其他数据是对cross数据的辅助；
# ② 考虑后续的二维节点图的构建
# ③ 简化数据，不要花里胡哨的数据格式，简洁

import os


class data_input:
    os.chdir(os.getcwd())  # 设置相对路径

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


def default():  # 直接输出所有数据
    road_path = u'road.txt'
    cross_path = u'cross.txt'
    car_path = u'car.txt'

    dip = data_input(road_path, cross_path, car_path)
    data_road, data_cross, dict_cross, data_car = dip.main()
    return data_road, data_cross, dict_cross, data_car


if __name__ == '__main__':
    # road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    # cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'
    # car_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\car.txt'

    road_path = u'road.txt'
    cross_path = u'cross.txt'
    car_path = u'car.txt'

    dip = data_input(road_path, cross_path, car_path)
    data_road, data_cross, dict_cross, data_car = dip.main()

    print(data_road)
    # print(data_cross)
    # print(data_car)
    # print(dict_cross)
    # print(data_car[10000])




