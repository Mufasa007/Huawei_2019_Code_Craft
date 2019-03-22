# 自建优先队列
# data是一个有序数组，d0是一个需要插入的数值
def priority_queue(data, d0):   # 二分查找法的优先队列建立
    if d0 < data[0]:
        data.insert(0, d0)
        return data
    elif d0 > data[-1]:
        data.append(d0)
        return data

    low = 0
    high = len(data) - 1
    while (high - low) > 1:
        mid = low + int((high - low) / 2)
        # print(low, high)
        if data[mid] == d0:
            data.insert(mid, d0)
            return data
        elif data[mid] < d0:
            low = mid
        elif data[mid] > d0:
            high = mid
    data.insert(mid, d0)
    return data


if __name__ == "__main__":
    data = [1, 2, 3, 6, 6, 7]
    # d0 = 4
    d0 = 5
    d1 = priority_queue(data, d0)
    print(d1)
