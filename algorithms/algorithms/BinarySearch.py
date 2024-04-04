def binarySearch(sortedList, item):
    first = 0
    last = len(sortedList) - 1
    found = False
    i = -1
    while (found != True and first <= last):
        mid = (first + last) // 2
        if sortedList[mid] == item:
            found = True
            return mid
        else:
            if item > sortedList[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found


if __name__ == "__main__":
    l = [1, 2, 4, 8, 9, 42, 1337, 1338, 5600, 13370]
    print(binarySearch(l, 42))
