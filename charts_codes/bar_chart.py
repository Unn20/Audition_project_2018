#this code creates a bar chart comparing ratio of values_2 to values_1

import matplotlib.pyplot as plt
import numpy as np

def bar_chart(names,values_1,values_2, title):
    N = len(names)
    values_1 = tuple(values_1)
    values_2 = tuple(values_2)
    std=[]
    ind = np.arange(N)
    width = 0.35
    fig, ax = plt.subplots()
    for i, j in zip(values_1, values_2):
        std.append((j/i)*100)
    rects1 = ax.bar(ind, tuple(std), width, color='lawngreen',edgecolor="red",linewidth=0.2)
    ax.set_ylabel('Percentage')
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    autolabel(rects1, ax)
    
    plt.show()
    return 0

def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                '{0}%'.format(int(height)),
                ha='center', va='bottom')