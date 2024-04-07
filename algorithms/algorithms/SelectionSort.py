import random
import time

#Funktion Selection Sort Algorithmus

def selectionSort(unsortedList):
  for index in range(len(unsortedList)):
    minimumIndex = index
    for i in range(minimumIndex+1, len(unsortedList)):
      if unsortedList[minimumIndex] > unsortedList[i]:
        minimumIndex = i

    # Elemente tauschen
    unsortedList[index], unsortedList[minimumIndex] = unsortedList[minimumIndex], unsortedList[index]

  return unsortedList

if __name__ == "__main__":
  l = []
  for i in range(9999):
    l.append(random.randint(0, 999))
  start = time.time()
  l = selectionSort(l)
  print(l)
  end = time.time()
  for i in range(len(l)-1):
    assert l[i] <= l[i+1]
  print(end-start)