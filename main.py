import matplotlib.pyplot as plt
import numpy as np
import random

functions = [
    [lambda a: np.sin(a), 2 * np.pi],
    [lambda a: np.cos(a), 2 * np.pi],
    [lambda a: np.power(a, 2), 10],
    [lambda a: np.power(a, 3), 10]
]

for i in range(len(functions)):

    for j in range(10):

        x = np.arange(0, functions[i][1], 0.01)

        a = random.random() * 2

        if (a == 0):
            a = 1
        
        x *= a

        y = functions[i][0](x)

        plt.rcParams['figure.facecolor'] = 'black'

        plt.figure(figsize=(4.1, 4))

        plt.gca().set_axis_off()
        plt.subplots_adjust(top=.9, bottom=.1, right=1, left=0,
                            hspace=0, wspace=0)
        plt.margins(0, 0.1)

        plt.plot(x, y, linewidth=4)

        plt.savefig("graphs/{}.png".format(i * 10 + j), dpi=900)

        plt.close()

