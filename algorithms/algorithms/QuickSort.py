import random
import time

def part(list, low, high):
  pivot = list[high]
  lowCache = low
  highCache = high

  while low < high:
    while high > lowCache and list[high] >= pivot:
      high = high -1
    while low < highCache and list[low] < pivot:
      low = low + 1
    if low < high:
      #Elemente tauschen
      list[low], list[high] = list[high], list[low]
    else:
      break
  if list[low] > pivot:
    list[highCache], list[low] = list[low], list[highCache]
  return low

def quickSort(unsortedList, low=0, high=None):
  if high is None:
    high = len(unsortedList) - 1

  if low < high:
    pivot = part(unsortedList, low, high)
    quickSort(unsortedList, low, pivot - 1)
    quickSort(unsortedList, pivot + 1, high)

if __name__ == "__main__":
  l = []
  for i in range(9999):
    l.append(random.randint(0, 999))
  start = time.time()
  quickSort(l)
  print(l)
  end = time.time()
  for i in range(len(l)-1):
    assert l[i] <= l[i+1]
  print(end-start)