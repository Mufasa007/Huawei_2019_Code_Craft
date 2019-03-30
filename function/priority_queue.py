# 2019.03.25    Mufasa
# version2.0    使用二分查找插入，时间复杂度O(1*logn) 空间复杂度O（1）
# 相较于之前的从头开始遍历进行插入效果更好，之前的时间复杂度O(n),空间复杂度O（1）


def priority_queue(data, d0):  # 二分查找法的优先队列建立
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
    d0 = -1
    # d0 = 0
    # d0 = 1
    # d0 = 3
    # d0 = 4
    # d0 = 6
    # d0 = 8
    d1 = priority_queue(data, d0)
    print(d1)
