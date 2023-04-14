def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    # 遍历items 列表 从第一个数开始， 依次选择
    for i in range(len(items) - 1):
        min_index = i
        # 在第一个数确定的情况下，遍历它之后的所有数，两个数之间进行大小排序
        for j in range(i + 1, len(items)):
            # 如果第一个数小于遍历中的数就进行序号交换，在for 循环结束后进行位置交换
            if comp(items[j], items[min_index]):
                min_index = j
        # if 语句成立，交换匹配到的两个数 （小的排前面，大的排后面）
        items[i], items[min_index] = items[min_index], items[i]
    return items


def main():
    list1 = [1, 3, 4, 4, 3, 52, 3423, 5234, 3523, 52, 5, 1, 65]
    print(select_sort(list1))


if __name__ == "__main__":
    main()
