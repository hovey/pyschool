import time

import numpy as np
import matplotlib.pyplot as plt


def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()


plt.clf()
plt.setp(plt.gca(), autoscale_on=False)

tellme("You will define a triangle, click to begin")

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme("Select 3 corners with mouse")
        # ginput is a blocking call to allow user to click n times on the figure
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme("Too few points, starting over")
            time.sleep(1)  # Wait a second

    ph = plt.fill(pts[:, 0], pts[:, 1], "r", lw=2)

    tellme("Happy? Key click for yes, mouse click for no")

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    for p in ph:
        p.remove()
