import time
from copy import deepcopy
import random
import sorting_lib as sl

class Insertion:
    def __init__(self, n):
        self.n = n
        self.arr = sl.gen_list(self.n)
        self.arrays = []

    def __repr__(self):
        return sl.print_arr(self.arr)
    
    def sort(self):
        key = 0
        for i in range(1, self.n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j+1] = self.arr[j]
                self.arrays.append(self.arr.copy())
                j -= 1
            self.arr[j+1] = key
            self.arrays.append(self.arr.copy())

if __name__ == "__main__":
    i = Insertion(50)
    s = time.time()
    i.sort()
    print(f"Runtime: {time.time()-s}")
    print(f"is_sorted = {sl.check(i.arr, i.n)}")
    sl.animate(i.arr, i.arrays, "insertion.mp4")

