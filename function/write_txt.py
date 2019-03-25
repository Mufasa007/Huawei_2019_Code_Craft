# 2019.03.25    Mufasa
# version2.0    使用相对路径

import os


def write_txt(data, path):  # 读取txt文件，返回二维数组
    os.chdir(os.getcwd())  # 设置相对路径
    file = open(path, 'w')
    for i in data:
        file.write('(' + str(i)[1:-1] + ')\n')
    file.close()


if __name__ == "__main__":
    road_path = u'write_test.txt'
    data = [[1001, 1, 2, 3, 4, 5], [1002, 1, 2, 3, 4, 5]]
    write_txt(data, road_path)
    # print(data)
