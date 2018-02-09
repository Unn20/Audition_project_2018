#code that creates a bar chart from set of values

import matplotlib.pyplot as plt
import numpy as np

def bar_chart(names,values_1, title):
    N = len(names)
    values_1 = tuple(values_1)
    #values_2 = tuple(values_2)
    #std=[]
    ind = np.arange(N)
    width = 0.35
    fig, ax = plt.subplots()
    #for i, j in zip(values_1, values_2):
    #    std.append((j/i)*100)
    rects1 = ax.bar(ind,values_1, width, color='lawngreen',edgecolor="red",linewidth=0.2)
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
                '{0}%'.format(float(height)),
                ha='center', va='bottom')