# 自建优先队列
# data是一个有序数组，d0是一个需要插入的数值
def priority_queue(data, d0):
    index = int(len(data) / 2)
    while 1:
        if data[index] == d0:
            data.insert(index,d0)
            return data
        elif data[index] < d0:

        elif data[index] > d0:


    return data


if __name__ == "__main__":
    data = [1, 2, 3, 5, 6, 7]
    d0 = 4
    d1 = priority_queue(data, d0)
    print(d1)
