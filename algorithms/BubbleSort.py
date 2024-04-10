import random
import time

def bubbleSort(unsortedList):
  for i in range(len(unsortedList)):
    for j in range(0, len(unsortedList)-1-i):
      if unsortedList[j] > unsortedList[j+1]:

        #Elemente tauschen
        unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]

  return unsortedList

if __name__ == "__main__":
  l = []
  for i in range(9999):
    l.append(random.randint(0, 999))
  start = time.time()
  l = bubbleSort(l)
  print(l)
  end = time.time()
  for i in range(len(l)-1):
    assert l[i] <= l[i+1]
  print(end-start)