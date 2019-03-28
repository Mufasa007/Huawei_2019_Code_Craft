
import sys

import numpy as np


# 生成邻接矩阵的时候路口的范围从0-N-1
def getAdj(roads,crosses):
    size=len(crosses)
    adjacency_matrix=np.zeros((size,size))
    for road in roads:
        # (id,length,speed,channel,from,to,isDuplex)
        #todo 速度调整
        adjacency_matrix[road[4]-1][road[5]-1]=road[1]/road[2]
        if road[-1]:
            adjacency_matrix[road[5]-1][road[4]-1]=road[1]/road[2]
    for i in range(size):
        for j in range(size):
            if i!=j and adjacency_matrix[i][j]==0:
                adjacency_matrix[i][j]= 10000000

    # print(adjacency_matrix)
    return adjacency_matrix

def floyed_search(D):
    N=len(adjacency_matrix)
    path_matrix = np.ones((N, N))
    path_matrix*=-1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if((D[i][k]+D[k][j])<D[i][j]):
                    D[i][j]=D[i][k]+D[k][j]
                    path_matrix[i][j]=k
    # print(path_matrix)
    return path_matrix


# path_matrix范围是路口0-路口N-1；
# from，to的范围是路口1到路口N；
def find_paths(path_matrix,car_path):
    paths=[]
    # (id,from,to,speed,planTime)
    for car in cars:
        start = int(car[1]) - 1
        dest = int(car[2]) - 1
        stack = []
        k = dest
        stack.append(k+1)
        find(start,dest,path_matrix,stack)
        stack.append(start+1)
        paths.append(stack)
    return paths

def find(start,dest,path_maxtrix,stack):
    k=int(path_matrix[start][dest])
    if k==-1 :
        return
    else:
        find(k,dest,path_matrix,stack)
        stack.append(k + 1)
        find(start, k, path_matrix, stack)




def convert_to_roadpath(paths,crosses):
    roadpaths=[]
    for path in paths:
        roadpath=[]
        for i in range(len(path)-1,0,-1):
            if(i>0):
                for roadid in crosses[path[i]-1][1:] :
                    if roadid in crosses[path[i-1]-1][1:]and roadid!=-1:
                        roadpath.append(roadid)
        roadpaths.append(roadpath)
    return roadpaths


def read_txt( path):  # txt文件读取
        f = open(path)
        txt = f.read().split('\n')
        data = []
        for i in txt[1:]:
            data_mid = []
            for j in i[1:-1].split(','):
                data_mid.append(int(j))
            data.append(data_mid)
        return data

def write_txt(data,cars,path):  # 按照特定格式写入txt文件
    file = open(path, 'w')
    file.write('#(carId,StartTime,RoadId...)')
    for i in range(len(data)):
        #todo 出发时间调整
        file.write('\n('+str(cars[i][0])+","+str(cars[i][-1])+","+ str(data[i])[1:-1] + ')')
    file.close()
def adjust_plantime(car):
    pass

if __name__ == '__main__':
    car_path = sys.argv[1]
    road_path = sys.argv[2]
    cross_path = sys.argv[3]
    answer_path = sys.argv[4]
    roads = read_txt(road_path)
    crosses = read_txt(cross_path)
    cars = read_txt(car_path)
    adjacency_matrix = getAdj(roads, crosses)
    path_matrix = floyed_search(adjacency_matrix)
    paths = find_paths(path_matrix, cars)
    roadpaths = convert_to_roadpath(paths, crosses)
    write_txt(roadpaths,cars, answer_path)

