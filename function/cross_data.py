# 功能：获取道路的方向
def cross_data(cross):
    road_direction = {}
    for i in cross:
        road_direction[i[0]] = i[1:]
    return road_direction


if __name__ == "__main__":
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'

    import read_txt,graph_data
    road = read_txt.read_txt(road_path)
    cross = read_txt.read_txt(cross_path)
    data_cross = cross_data(cross)
    print(data_cross)