from matplotlib import pyplot as plt

class Bubble:
    def __init__(self, n):
        self.n = n
        self.arr = get_list(self.n)
    
    def __repr__(self):
        return "".join(self.arr)

    

    def gen_list(self, n):
        return [random.randrange(i) for i in range(n)]

if __name__ == "__main__":
    pass
