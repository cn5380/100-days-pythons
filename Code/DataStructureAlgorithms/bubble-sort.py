def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def main():
    list1 = [9, 3, 4, 7, 16, 52, 323, 5234, 3523, 52, 5, 1, 65]
    print(bubble_sort(list1))


if __name__ == "__main__":
    main()
