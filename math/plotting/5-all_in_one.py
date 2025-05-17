#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(constrained_layout=True, figsize=(12, 10))
gs = fig.add_gridspec(3, 2)

# figure 1
ax1 = fig.add_subplot(gs[0,0])
ax1.plot(y0, 'r-')

# figure 2
ax2 = fig.add_subplot(gs[0,1])
ax2.scatter(x1,y1, color='magenta')
ax2.set_xlabel("Height(in)")
ax2.set_ylabel("Weight(lbs)")
ax2.set_title("Men’s Height vs Weight")

# figure 3
ax3 = fig.add_subplot(gs[1,0])
ax3.plot(x2,y2, color='blue')
ax3.set_yscale('log')
ax3.set_xlabel("Time(years)")
ax3.set_ylabel("Fraction remaining")
ax3.set_title("Exponential Decay of C-14")

# figure 4
ax4 = fig.add_subplot(gs[1,1])
ax4.plot(x3,y31, color='Red', linestyle='--')
ax4.plot(x3,y32, color='green')
ax4.set_xlabel("Time (years)")
ax4.set_ylabel("Fraction Remaining")
ax4.set_title("Exponential Decay of Radioactive Elements")
ax4.legend(["C-14", "Ra-226"], loc="upper right")

# figure 5
ax5 = fig.add_subplot(gs[2, :])
ax5.hist(student_grades, edgecolor='black')
ax5.set_xticks(np.arange(0, 110, 10))
ax5.set_yticks(np.arange(0, 35, 5))
ax5.set_xlabel("Grades")
ax5.set_ylabel("Number of Students")
ax5.set_title("Project A")

fig.suptitle("All in One", fontsize= 16)
plt.show()
