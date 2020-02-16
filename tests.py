from bubblesort import Bubble
from quick import Quick
from radix import Radix
from heap import Heap
from insertion import Insertion
import sorting_lib as sl


b = Bubble(100)
r = Radix(255)
q = Quick(255)
h = Heap(255)
i = Insertion(100)
print("bubble")
b.sort()
print("radix")
r.sort()
print("quick")
q.sort()
print("heap")
h.sort()
print("insert")
i.sort()
sl.animate(b.arr, b.arrays, "bubble.mp4")
sl.animate(r.arr, r.arrays, "radix.mp4")
sl.animate(q.arr, q.arrays, "quick.mp4")
sl.animate(h.arr, h.arrays, "heap.mp4")
sl.animate(i.arr, i.arrays, "insertion.mp4")
