# from
# https://matplotlib.org/stable/gallery/event_handling/timers.html

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def update_title(axes):
    now = datetime.now()
    now_string = now.strftime("%Y-%m-%d %H:%M:%S")
    # axes.set_title(datetime.now())
    axes.set_title(now_string)
    axes.figure.canvas.draw()


fig, ax = plt.subplots()

x = np.linspace(-3, 3)
ax.plot(x, x ** 2)

# Create a new timer object. Set the interval to 1000 milliseconds
# (1000 is default) and tell the timer what function should be called.
time_interval = 1000  # millisecond

# https://matplotlib.org/stable/api/backend_bases_api.html?highlight=new_timer#matplotlib.backend_bases.FigureCanvasBase.new_timer
# new_timer(self, interval=None, callbacks=None)

timer = fig.canvas.new_timer(interval=time_interval)
timer.add_callback(update_title, ax)
timer.start()

# Or could start the timer on first figure draw
# def start_timer(event):
#    timer.start()
#    fig.canvas.mpl_disconnect(drawid)
# drawid = fig.canvas.mpl_connect('draw_event', start_timer)

plt.show()
