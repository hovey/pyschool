"""This module shown an incrementally growing sine curve, as a Matplotlib animation.
https://matplotlib.org/stable/api/animation_api.html
"""
from typing import Tuple

import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xmin, xmax = 0, 2 * np.pi
ymin, ymax = -2, 2

# frames=np.linspace(0, 2 * np.pi, 128),
xs = np.linspace(xmin, xmax, num=128)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

xdata, ydata = [], []
(line,) = plt.plot([], [], "bo")


# def func_init():
#     # ax.set_xlim(0, 2 * np.pi)
#     # ax.set_ylim(-2, 2)
#     ax.set_xlabel("x")
#     ax.set_xlim(xmin, xmax)
#     ax.set_ylim(ymin, ymax)
#     return (line,)


def func_update(frame: int, *fargs) -> Tuple[Line2D]:
    # # history trail is shown
    # xdata.append(frame)
    # ydata.append(np.sin(frame))

    # history trail is not shown
    xdata = frame
    ydata = np.sin(frame)

    line.set_data(xdata, ydata)
    return (line,)


ani = FuncAnimation(
    fig,
    func_update,
    frames=xs,
    init_func=None,
    fargs=None,
    interval=5,
    blit=True,
)
plt.show()
