import matplotlib.pyplot as plt

def pie_chart(labels,sizes):
    # Data to plot
    labels = labels
    sizes = sizes
    colors = ['crimson', 'orange', 'gold', 'green','deepskyblue', 'lightgreen', 'lightcoral', 'peru','darkgray']
    # Plot
    patches, texts, costam = plt.pie(sizes, labels=labels, colors=colors,
         shadow=True, startangle=140, autopct='%1.1f%%', pctdistance=0.9)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.show()
    return 0