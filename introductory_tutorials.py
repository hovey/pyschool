# https://matplotlib.org/tutorials/index.html

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.style as mplstyle # see Performance section, below
mplstyle.use('fast')

## Introduction

### Useage Guide

# https://matplotlib.org/tutorials/introductory/usage.html

# Matplotlib is package.
# matplotlib.pyplot is a module in matplotlib.
# matplotlib.pylab is a module in matplotlib.  
# * The pylab module is a convenience module that
#   bulk imports matplotlib.pyplot and numpy in a single namespace.  
# * pylab is deprecated and strongly discouraged because of namespace pollution.  
# * Prefer pyplot instead.

# Top-level, matplotlib.pyplot module acts like a "state-machine", similar to MATLAB, wherein
# lines, images, etc., are added to the current of the current figure.

# State Machine Example

x = np.linspace(0, 2, 100)
# plt.ion() # see Interactive Mode description below
plt.ioff()
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')
plt.legend()
plt.show()

# Figure

# Next, comes the first level of OOP, for figure creation.  
# The figure has one or more child Axes objects, and other 'special' artists, called
# titled, figure legends, etc.  
fig = plt.figure() # an empty figure with no axes
fig.suptitle('No axes on this figure') # add a title to show where it appears on the figure
plt.show()

# Axes

fig, array_axes = plt.subplots(2, 2) # figure with a 2x2 grid of Axes objects
array_axes[0,0].set_xlim(0, 2) # get the first row and first column Axes object, rescale xlimits
plt.show()

# Axis

# A number-line-like object, typically an x-axis and a y-axis will compose a single Axes.
# The Axis object will have ticks and ticklabels.
# The Locator object and Formatter object gives very find control over the 
# tick locations and labels.

# Artists

# Everything seen on a figure is an artist, including the Figure, Axes, and Axis objects.
# Most artists are tied to an Axes object, so an Artist cannot be shared by multiple Axes
# and cannot be moved from one Axes to another.
# All artists are draw on the canvas object.  

# Preferred object-oriented style

# Unlike MATLAB, which relies on a global state machine and a flat namespace, 
# the preferred Python style is with OOP, resulting in wordier but more 
# explicit code.  

x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# Helper Functions

# For repetitive tasks to be applied to two or more Axes, maintain a D.R.Y. (don't repeat
# yourself) coding style with helper functions.
# def my_helper_function(ax, x_data, y_data, param_dict):
#   """
#   A helper function to make a graph
# 
#   Parameters
#   ----------
#   ax : Axes
#       The Axes object to draw to
#
#   x_data : array
#       The x data
#
#   y_data : array
#       The y data
#
#   param_dict : dict
#       Dictionary of kwargs to pass to ax.plot
#
#   Returns
#   -------
#   out : list
#       list of artists added
#   """

def my_helper_function(ax, x_data, y_data, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The Axes object to draw to

    x_data : array
        The x data

    y_data : array
        The y data

    param_dict : dict
        Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        Diection of artists added
    """
    out = ax.plot(x_data, y_data, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_helper_function(ax, data1, data2, {'marker': 'x'})
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
my_helper_function(ax1, data1, data2, {'marker': 'x'})
my_helper_function(ax2, data3, data4, {'marker': 'o'})
plt.show()

# Frontends and Backends

# The Frontend is the user-facing code.  
# The Backend does all the work to make the figure for the specific
# context, e.g., in a Python shell, in a pygtk rich application, etc.
# There are two types of Backends: Interface (also called Interactive) 
# and Hardcopy (also called non-Interface)
# * Interface (Interactive) Backend, for use in pygtk, qt4, macosx, etc.
# * Hardcopy (non-Interactive) Backend, to make image files, e.g., PNG, SVG, PDF, PS, etc.

# There are three (four?) ways to configure the Backend
# 1. The backend parameter in the matplotlibrc file.
# 2. The MPLBACKEND environment variable
# 3. The matplotlib.use() command, which must be called prior to import of matplotlib.pyplot.

# Interactive Mode

# Default is off, turn on via plt.ion(), and turn off with plt.ioff()

# In Interactive mode, plt.draw() will refresh the plot.

# In non-Interactive mode, all drawing is delayed until plt.show() is
# called, which is more efficient than interactive mode, which redraws
# the plot each time a new feature is added to the plot (e.g., this is how
# MATLAB works).

# plt.show() also pauses the script so the user can see the figure.

# Performance

# Plotting data can be a major performance bottleneck.
# The fast style can speed up performance, when speed
# is a higher priority than image quality.
# import matplotlib.style as mplstyle
# mplstyle.use('fast')
