import random
import time

def insertionSort(unsortedList):
    sortedList = []
    while len(unsortedList) > 0:
        smallest = unsortedList[0]
        smallestIndex = 0
        for index, elem in enumerate(unsortedList):
            if elem < smallest:
                smallest = elem
                smallestIndex = index
        unsortedList.pop(smallestIndex)
        sortedList.append(smallest)
    return sortedList

if __name__ == "__main__":
    # Liste mit Zuffalszahlen erzeugen
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    start = time.time()
    print(insertionSort(l))
    end = time.time()
    print(end - start)