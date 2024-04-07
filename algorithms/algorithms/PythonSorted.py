import random
import time

if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    start = time.time()
    l = sorted(l)
    print(l)
    end = time.time()
    print(end-start)