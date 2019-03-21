import numpy as np

def map_data(road_path, cross_path): # 1，读取txt文件；2，根据规则进行数据转换融合
    f = open(road_path)
    txt = f.read().split('\n')
    # print(txt)
    data = []
    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    # print(data)
    data1 = np.array(data)
    print(data1.shape)
    print(data1)

    f = open(cross_path)
    txt = f.read().split('\n')
    # print(txt)
    data = []
    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    data1 = np.array(data)
    # print(data1.shape)
    # print(data1)

def car_data(car_path): # 1，读取txt文件；2，生成有顺序数组
    f = open(car_path)
    txt = f.read().split('\n')
    data = []
    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    data1 = np.array(data)
    # print(data1.shape)
    # print(data1)



if __name__ == '__main__':
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'
    car_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\car.txt'

    data_map = map_data(road_path, cross_path)
    data_car = car_data(car_path)