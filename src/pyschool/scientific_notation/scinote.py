#!/usr/bin/env python

# References:
# https://stackoverflow.com/questions/28371674/prevent-scientific-notation-in-matplotlib-pyplot

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1000, 1001, 100)
y = np.linspace(1e-9, 1e9, 100)


fig, ax = plt.subplots()
# ax.plot(range(2003, 2012, 1), range(200300, 201200, 100))
# ax.ticklabel_format(axis='x', style='scientific')
# ax.ticklabel_format(axis='y', style='scientific')

ax.ticklabel_format(axis="y", style="scientific", scilimits=(0, 0))
# ax.ticklabel_format(useOffset=False, style='plain')
ax.plot(x, y)

ax2 = fig.add_subplot(111, sharex=ax, frameon=False)
bottom, top = ax.get_ylim()
# print(f'The (bottom, top) y limits are {bottom, top}')

scale = 10
ax2.set_ylim(scale * bottom, scale * top)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

plt.show()
