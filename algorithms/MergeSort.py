import random
import time

def merge(list, l, m, r):
  divider = m+1
  lCache = l
  outList = []
  for i in range(r-l+1):
    if l > m:
      outList.append(list[divider])
      divider = divider + 1
    elif divider > r:
      outList.append(list[l])
      l = l+1
    elif list[l] < list[divider]:
      outList.append(list[l])
      l = l+1
    elif list[l] >= list[divider]:
      outList.append(list[divider])
      divider = divider+1
  for i in range(len(outList)):
    list[i + lCache] = outList[i]

def mergeSort(unsortedList, l=0, r=None):
  if r is None:
    r = len(unsortedList)-1

  if l < r:
    m = (l+r-1) // 2
    mergeSort(unsortedList, l, m)
    mergeSort(unsortedList, m+1, r)
    merge(unsortedList, l, m, r)

if __name__ == "__main__":
  l = []
  for i in range(9999):
    l.append(random.randint(0, 999))
  start = time.time()
  mergeSort(l)
  print(l)
  end = time.time()
  for i in range(len(l)-1):
    assert l[i] <= l[i+1]
  print(end-start)