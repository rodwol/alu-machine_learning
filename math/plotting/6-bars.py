#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
x_labels = ['Farrah', 'Fred', 'Felicia']
fruit_labels = ['apples', 'bananas', 'oranges', 'peaches' ]
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

x = np.arange(fruit.shape[1])
width = 0.6

fig, ax = plt.subplots()
bottom = np.zeros(fruit.shape[1])

for i in range(fruit.shape[0]):
    ax.bar(x, fruit[i], bottom=bottom, label=fruit_labels[i], color=colors[i])
    bottom += fruit[i]

# Customize chart
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.legend()

plt.show()
