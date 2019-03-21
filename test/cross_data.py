# 功能：获取道路的方向
def cross_data(cross):
    road_direction = {}
    for i in cross:
        if i[1] not in road_direction.keys():
            road_direction[i[1]] = 1
        if i[2] not in road_direction.keys():
            road_direction[i[2]] = 0
        if i[3] not in road_direction.keys():
            road_direction[i[3]] = 1
        if i[4] not in road_direction.keys():
            road_direction[i[4]] = 0
        # print(road_direction)
    return road_direction


if __name__ == "__main__":
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'

    import read_txt,graph_data
    road = read_txt.read_txt(road_path)
    cross = read_txt.read_txt(cross_path)
    road_direction = cross_data(cross)
    print(road_direction)