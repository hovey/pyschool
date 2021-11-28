"""This module shown a translating sine curve, as a simple Matplotlib animation.
The animation stops when the user closes the Matplotlib figure window.
Adapted from 'Animated Line Plot',
https://matplotlib.org/stable/gallery/animation/simple_anim.html
"""

from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D

fig, ax = plt.subplots()

t0, tfinal = 0.0, 2.0 * np.pi
dt = 0.1
t = np.arange(t0, tfinal, dt)

ax.set_xlabel("t")
ax.set_ylabel("f(t)")
ax.set_xlim(t0, tfinal)
ax.set_ylim(-1.2, 1.2)

# (line,) = ax.plot(t, np.sin(t))
(line,) = ax.plot([], [])

# def animate(i): in the example has become 'update' here


# def func_init():
#     line.set_ydata(np.sin(t))  # initialize the y-data
#     return (line,)


def func_update(frame: int, *fargs) -> Tuple[Line2D]:
    line.set_xdata(t)
    line.set_ydata(np.sin(t + frame / 50))  # update the y-data
    return (line,)


# https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html

# class matplotlib.animation.FuncAnimation(fig, func, frames=None, init_func=None, fargs=None, save_count=None, *, cache_frame_data=True, **kwargs)

# Note: The created Animation object must be stored in a variable that lives as long as
# the animation should run. Otherwise, the Animation object will be garbage-collected
# and the animation will stop.

# ani = animation.FuncAnimation(
#     fig,
#     func_update,
#     frames=None,
#     init_func=None,
#     fargs=None,
#     save_count=50,
#     interval=20,
#     blit=True,
# )
ani = animation.FuncAnimation(fig, func_update, interval=20, blit=True, save_count=50)
"""
    Parameters:
        fig (Figure): The figure object used to get needed events, such as draw or resize.
        func (callable): The function to call at each frame, with the signature:
                def func(frame, *fargs) -> iterable_of_artists
            The first argument will be the next value in 'frames'.  Any additional
                positional arguments use the 'fargs' parameter.  The required signature:
            If blit == True, then func must return an iterable of artists that were
                created or modified.  This information is used by the blitting algorithm
                to determine which parts must be updated.  The return value is not used
                if blit == False, and may be omitted in this False case.
        frames (iterable, int, generator, or None):  Optional.
        init_func (callable): Optional.  A function used to draw a clear frame with the
            signature:
                def init_func() -> iterable_of_artists
            If not given, the results of drawing from the first item in the frames
            sequence is used.  This function is called once before the first frame.
        interval (int):  Time delay between frames in milliseconds. Defaults to 200.
        save_count (int):  Fallback for the number of values from `frames` to cache.
            This is only used if the number of `frames` cannot be inferred from `frames`,
            i.e., when it is an iterator without length or a generator.
            Defaults to 100.
        blit (bool): Whether blitting is used to optimize drawing.  When blitting is
            used, any animated artist will be drawn according to their zorder; however,
            they will be drawn on top of any previous artist, regardless of their zorder.
            Defaults to False.
"""

# To save the animation, use e.g.,
# ani.save("test_movie.mp4")

plt.show()
