#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arrange(0, 11)

plt.plot(x,y, 'r-') # 'r-' means solid red line
plt.show()
