"""This module shows random walks in 3D animation.

Adapted from 'Animated 3D random walk'
https://matplotlib.org/stable/gallery/animation/random_walk.html
"""
from typing import Tuple

import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Line3D
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    nsd = 3  # number of space dimensions, 2 for 2D, 3 for 3D
    start_pos = np.random.random(nsd)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, nsd))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk


# def update_lines(num, walks, lines):
#    for line, walk in zip(lines, walks):
#        # NOTE: there is no .set_data() for 3 dim data...
#        line.set_data(walk[:num, :2].T)
#        line.set_3d_properties(walk[:num, 2])
#    return lines


def update_lines(frame: int, walks, lines) -> Tuple[Line3D]:
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:frame, :2].T)
        line.set_3d_properties(walk[:frame, 2])
    return lines


# Data: 40 random walks as (num_steps, 3) arrays
# num_particles = 40
num_particles: int = 2
# num_steps = 30
num_steps: int = 10
walks = [random_walk(num_steps) for index in range(num_particles)]

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel="x")
ax.set(ylim3d=(0, 1), ylabel="y")
ax.set(zlim3d=(0, 1), zlabel="z")

# Creating the Animation object
# ani = animation.FuncAnimation(
#     fig, update_lines, num_steps, fargs=(walks, lines), interval=100
# )
ani = animation.FuncAnimation(
    fig, update_lines, frames=num_steps, fargs=(walks, lines), interval=100
)

plt.show()
