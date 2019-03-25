# 2019.03.25    Mufasa
# version2.0    增强程序鲁棒性
import os


def read_txt(path):  # 读取txt文件，返回二维数组
    os.chdir(os.getcwd())  # 设置相对路径
    f = open(path)
    txt = f.read().split('\n')  # 自带分行符
    data = []
    if txt[0][0] == '#':  # 增强程序的鲁棒性（1，跳过文件说明；2，防止数据遗漏）
        txt = txt[1:]

    for i in txt:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    return data


if __name__ == "__main__":
    road_path = 'answer.txt'
    data = read_txt(road_path)
    print(data)
