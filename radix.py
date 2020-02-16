import time
from copy import deepcopy
import random
import sorting_lib as sl

class Radix:
    def __init__(self, n):
        self.n = n
        self.arr = sl.gen_list(self.n)
        self.arrays = []

    def __repr__(self):
        return sl.print_arr(self.arr)
    
    def sort(self):
        loops = 0 
        current_dig = 1
        for _ in range(4):
            buckets = [[] for i in range(10)]
            for x in self.arr:
                index = int((x / current_dig) % 10)
                buckets[index].append(x)
                loops += 1
            j = 0
            for b in buckets:
                for x in b:
                    self.arr[j] = x 
                    j += 1
                    loops += 1
                    self.arrays.append(self.arr.copy())
            current_dig *= 10
        print(loops)


if __name__ == "__main__":
    r = Radix(133)
    s = time.time()
    r.sort()
    print(f"Runtime: {time.time()-s}")
    print(f"is_sorted = {sl.check(r.arr, r.n)}")
    sl.animate(r.arr, r.arrays, "radix.mp4")

