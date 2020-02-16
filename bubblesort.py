import random
from matplotlib import pyplot as plt
import sorting_lib as sl

class Bubble:
    def __init__(self, n):
        self.n = n
        self.arr = sl.gen_list(self.n)

    def __repr__(self):
        return sl.print_arr(self.arr)
    
    def sort(self):
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.arr[j] > self.arr[j+1]:
                    sl.swap(arr, j, j+1)


if __name__ == "__main__":
    b = Bubble(10)
    print(b)
    b.sort()
    print(b)
    print(f"is_sorted = {b.check()}")
