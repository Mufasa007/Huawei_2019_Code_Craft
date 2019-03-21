# 先处理road.txt和cross.txt

# 读取原始数据，图的字典格式
def map_data(road_path, cross_path):    # 1，读取txt文件；2，根据规则进行数据转换融合
    data_map = {}
    f = open(road_path)
    txt = f.read().split('\n')
    data = []
    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    for i in data:
        if i[4] not in data_map.keys():
            data_map[i[4]] = [i[5]]
        else:
            data_map[i[4]].append(i[5])
        if i[6]:
            if i[5] not in data_map.keys():
                data_map[i[5]] = [i[4]]
            else:
                data_map[i[5]].append(i[4])
    return data_map


if __name__ == '__main__':
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'

    data_map = map_data(road_path, cross_path)
    print(data_map)

'''
{1: [2, 7], 2: [1, 3, 8], 3: [2, 4, 9], 4: [3, 5, 10], 5: [4, 6, 11], 6: [5, 12], 7: [1, 8, 13], 8: [2, 7, 9, 14], 
9: [3, 8, 10, 15], 10: [4, 9, 11, 16], 11: [5, 10, 12, 17], 12: [6, 11, 18], 13: [7, 14, 19], 14: [8, 13, 15, 20], 
15: [9, 14, 16, 21], 16: [10, 15, 17, 22], 17: [11, 16, 18, 23], 18: [12, 17, 24], 19: [13, 20, 25], 20: [14, 19, 21, 
26], 21: [15, 20, 22, 27], 22: [16, 21, 23, 28], 23: [17, 22, 24, 29], 24: [18, 23, 30], 25: [19, 26, 31], 26: [20, 
25, 27, 32], 27: [21, 26, 28, 33], 28: [22, 27, 29, 34], 29: [23, 28, 30, 35], 30: [24, 29, 36], 31: [25, 32], 
32: [26, 31, 33], 33: [27, 32, 34], 34: [28, 33, 35], 35: [29, 34, 36], 36: [30, 35]} 
'''
