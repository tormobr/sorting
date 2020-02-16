import random
from matplotlib import pyplot as plt

class Bubble:
    def __init__(self, n):
        self.n = n
        self.arr = self.gen_list()
    
    def __repr__(self):
        return "".join(str(x) + ", " for x in self.arr)

    def sort(self):
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.swap(j, j+1)

    def swap(self, i, j):
        tmp = self.arr[i] 
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp

    def gen_list(self):
        return [random.randrange(self.n) for i in range(self.n)]

    def check(self):
        for i in range(self.n - 1):
            if self.arr[i+1] < self.arr[i]:
                return False
        return True


if __name__ == "__main__":
    b = Bubble(10)
    print(b)
    b.sort()
    print(b)
    print(f"is_sorted = {b.check()}")
