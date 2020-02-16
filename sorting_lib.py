import random
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

def print_arr(arr):
    return "".join(str(x) + ", " for x in arr)

def swap(arr, i, j):
    tmp = arr[i] 
    arr[i] = arr[j]
    arr[j] = tmp

def gen_list(n):
    ret = [i+1 for i in range(n)]
    random.shuffle(ret)
    return ret

def check(arr, n):
    for i in range(n - 1):
        if arr[i+1] < arr[i]:
            return False
    return True

def ani_iteration(i, rects, data):
    for rect, height in zip(rects, data[i]):
        rect.set_height(height)
    return rects

def animate(arr, data):
    fig = plt.figure()

    x = arr
    plt.style.use("dark_background")
    rects = plt.bar(x, data[0], color="w", edgecolor="g")
    plt.ylim(0, max(arr)+10)

    anim = animation.FuncAnimation(fig, ani_iteration, fargs=(rects, data), frames=len(data), interval=1)
    plt.show()
    #anim.save("plot.mp4")

