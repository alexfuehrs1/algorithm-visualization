import matplotlib.pyplot as plt
import numpy as np
import bubble_sort

lst = np.random.randint(0, 100, 15)
fig, axs = plt.subplots(2, 2, figsize=(10, 5))
bars = []

# generate the Subplots
for i in range(len(axs)):
    for j in range(len(axs)):
        axs[i][j].set_ylim(0, max(lst)*1.2)
        axs[i][j].set_xlim(0, len(lst))
        col = (np.random.random(), np.random.random(), np.random.random())
        bars.append(axs[i][j].bar(np.arange(0, len(lst)), lst, color=col) )

axs[0][0].set_title('Bubblesort')
axs[0][1].set_title('Mergesort')
axs[1][0].set_title('Quicksort')
axs[1][1].set_title('Heapsort')


# update the Subplots
def updateBars(bars, arr):
    for bar, h in zip(bars, arr):
        bar.set_height(h)
    plt.draw()
    plt.pause(0.1)
    

# each algorithm is updated here
def visualize_sorting(sort_algorithm, lst, bars):
    for arr in sort_algorithm(lst.copy()):
        updateBars(bars, arr)


visualize_sorting(bubble_sort.bubble_sort, lst, bars[0])
plt.show()
