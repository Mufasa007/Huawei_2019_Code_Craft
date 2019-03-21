def map_data(road,cross):
    length = len(cross)









if __name__=="__main__":
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    cross_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\cross.txt'
    import read_txt,graph_data
    road = read_txt.read_txt(road_path)
    cross = read_txt.read_txt(cross_path)
    data_graph = graph_data.graph_data(road)
    data_map = map_data(road,cross)
    # print(road)
    # print(cross)
    # print(data_graph)
    # print(data_map)