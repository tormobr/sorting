import time
from copy import deepcopy
import random
import sorting_lib as sl

class Quick:
    def __init__(self, n):
        self.n = n
        self.arr = sl.gen_list(self.n)
        self.arrays = []

    def __repr__(self):
        return sl.print_arr(self.arr)
    
    def sort(self):
        self.quicksort(0, self.n-1)

    def quicksort(self, left, right):
        l, r = left, right
        pivot = self.arr[(r+l)//2]
        while l <= r:
            while self.arr[l] < pivot:
                l += 1
            while self.arr[r] > pivot:
                r -= 1

            if l <= r:
                sl.swap(self.arr, l, r)
                l += 1
                r -= 1
            self.arrays.append(deepcopy(self.arr))
        if left < r:
            self.quicksort(left, r)
        if l < right:
            self.quicksort(l, right)

            
        
        

if __name__ == "__main__":
    q = Quick(100)
    s = time.time()
    q.sort()
    print(f"Runtime: {time.time()-s}")
    print(f"is_sorted = {sl.check(q.arr, q.n)}")
    sl.animate(q.arr, q.arrays, "quick.mp4")

