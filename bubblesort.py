import time
from copy import deepcopy
import random
import sorting_lib as sl

class Bubble:
    def __init__(self, n):
        self.n = n
        self.arr = sl.gen_list(self.n)
        self.arrays = []

    def __repr__(self):
        return sl.print_arr(self.arr)
    
    def sort(self):
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.arr[j] > self.arr[j+1]:
                    sl.swap(self.arr, j, j+1)
                self.arrays.append(deepcopy(self.arr))


if __name__ == "__main__":
    b = Bubble(20)
    print(b)
    s = time.time()
    b.sort()
    print(f"Runtime: {time.time()-s}")
    print(b)
    print(f"is_sorted = {sl.check(b.arr, b.n)}")
    sl.animate(b.arr, b.arrays, "bubble.mp4")

