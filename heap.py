import heapq
import time
from copy import deepcopy
import random
import sorting_lib as sl

class Heap:
    def __init__(self, n):
        self.n = n
        self.arr = sl.gen_list(self.n)
        self.arrays = []

    def __repr__(self):
        return sl.print_arr(self.arr)
    
    def sort(self):
        for i in range((self.n // 2)-1, -1, -1):
            self.heapify(self.n, i);
        for i in range(self.n -1, -1, -1):
            sl.swap(self.arr, 0, i);
            self.arrays.append(self.arr.copy())
            self.heapify(i, 0);

    def heapify(self, n, i):
        maxx = i
        l = 2*i +1
        r = 2*i +2
        if l < n and self.arr[l] > self.arr[maxx]:
            maxx = l
        if r < n and self.arr[r] > self.arr[maxx]:
            maxx = r
        if i != maxx:
            sl.swap(self.arr, i, maxx)
            self.arrays.append(self.arr.copy())
            self.heapify(n, maxx)

if __name__ == "__main__":
    h = Heap(100)
    s = time.time()
    h.sort()
    print(f"Runtime: {time.time()-s}")
    print(f"is_sorted = {sl.check(h.arr, h.n)}")
    sl.animate(h.arr, h.arrays, "heap.mp4");

