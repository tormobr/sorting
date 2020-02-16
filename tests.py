from bubblesort import Bubble
from quick import Quick
from radix import Radix
from heap import Heap
from insertion import Insertion
import sorting_lib as sl


b = Bubble(200)
r = Radix(200)
q = Quick(200)
h = Heap(200)
i = Insertion(200)
b.sort()
r.sort()
q.sort()
h.sort()
i.sort()
sl.animate(b.arr, b.arrays, "bubble.mp4")
sl.animate(r.arr, r.arrays, "radix.mp4")
sl.animate(q.arr, q.arrays, "quick.mp4")
sl.animate(h.arr, h.arrays, "heap.mp4")
sl.animate(i.arr, i.arrays, "insertion.mp4")
