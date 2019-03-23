
def read_txt(path): # 读取txt文件，返回二维数组
    f = open(path)

    txt = f.read().split('\n')  # 自带分行符
    # print(txt[0])
    data = []

    for i in txt[1:]:
        data_mid = []
        for j in i[1:-1].split(','):
            data_mid.append(int(j))
        data.append(data_mid)
    return data

if __name__ == "__main__":
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\config\\car.txt'
    data = read_txt(road_path)
    print(data)