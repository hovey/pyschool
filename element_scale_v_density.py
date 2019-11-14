# 2019-01-25 Plot of theoretical element size versus 
# element density for a flat CTH mesh with Bob.  Overlay
# similar data from other researchers, based on Table 1
# of Giudice 2018.

# import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
# from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
import os
from decimal import Decimal

# constants or globals
PRINT_TO_PDF = 1
LIMIT_LINE_COLOR = 'mediumblue'
GRID_LINE_COLOR = 'dimgray'
FIG_NUM = 1
FILE_BASE = os.path.basename(__file__).split('.')[0]

# colors
# https://matplotlib.org/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py

# helper functions
def text_elements(x, y, text):
    ax.text(x, y, text, backgroundcolor="none",
        ha='left', va='center', weight='normal', color=GRID_LINE_COLOR)

def text_elements_rotated(x, y, text):
    ax.text(x, y, text, backgroundcolor="none",
        ha='right', va='top', weight='normal', color=GRID_LINE_COLOR, 
        rotation=90)

# turn interactive mode to on
# plt.ion()

# turn interactive mode to off
plt.ioff()

# update default font to Helvetica
# Ref: https://matplotlib.org/users/dflt_style_changes.html#normal-text
# https://matplotlib.org/users/customizing.html 
# https://stackoverflow.com/questions/21321670/how-to-change-fonts-in-matplotlib-python 
# http://jonathansoma.com/lede/data-studio/matplotlib/changing-fonts-in-matplotlib/
# http://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/ 


# mpl.rcParams['font.sans-serif'] = "Comic Sans MS" # cool, but no
# mpl.rcParams['font.family'] = "sans-serif"

mpl.rcParams['font.sans-serif'] = "Calibri"
mpl.rcParams['font.family'] = "sans-serif"

# mpl.rcParams['font.serif'] = "Georgia"
# mpl.rcParams['font.family'] = "serif"

# Assume a domain (20, 20, 20) cm, with a flat uniform mesh, 
# with length scale of cm, half-cm, double-mm, mm, half-mm, and quarter-mm

DOMAIN_VOLUME = 0.20 * 0.20 * 0.20 # m^3
# length_scales = [0.01, 0.005, 0.002, 0.001, 0.0005, 0.00025]
# length_scales = [0.00025, 0.0005, 0.001, 0.002, 0.005, 0.01]
length_scales = [0.001, 0.002, 0.005, 0.01] # don't do less than 1-mm
num_elements = [DOMAIN_VOLUME * 1/(i**3) for i in length_scales]
# This should produce elements of 
# 8 thousand
# 64 thousand
# 1 million
# 8 million
# 64 million
# 512 million

# fig, ax = plt.subplots()
fig = plt.figure(figsize=(8, 8)) # 8 inch wide, 8 inch tall
ax = fig.add_subplot(1, 1, 1, aspect=1)

marker_style = dict(color=LIMIT_LINE_COLOR, linestyle=':', marker='s', markersize=5)
ax.plot(length_scales, num_elements, **marker_style)

# annotation for each data point
# https://matplotlib.org/gallery/lines_bars_and_markers/timeline.html#sphx-glr-gallery-lines-bars-and-markers-timeline-py 
# https://docs.python.org/3.3/library/string.html#formatspec
for ii, (x_data, y_data) in enumerate(zip(length_scales, num_elements)):
    x_data_str = '{:.1e}'.format(Decimal(str(x_data)))
    y_data_str = '{:.1e}'.format(Decimal(str(y_data))) 
    the_string = '  (' + x_data_str + ', ' + y_data_str + ')'
    ax.text(x_data, y_data, the_string, ha='left', va='center', 
    color=LIMIT_LINE_COLOR)



# show 3:1 slope of line
# http://pbpython.com/effective-matplotlib.html
# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hlines.html#matplotlib.axes.Axes.hlines
x0 = length_scales[-2]
x1 = length_scales[-1]
y0 = num_elements[-1]
y1 = num_elements[-2]
ax.hlines(0.8*y1, 1.2*x0, 0.8*x1, colors=LIMIT_LINE_COLOR, linewidth=0.5)
ax.vlines(0.8*x1, 2.2*1.2*y0, 0.8*y1, colors=LIMIT_LINE_COLOR, linewidth=0.5)
ax.text(0.85*x1, 0.45*(y0+y1), '3', ha='left', va='baseline', color=LIMIT_LINE_COLOR)

ax.set_xlabel("Element Characteristic Length (m)")
ax.set_ylabel("Number of Elements (J>0)")
# ax.set_title("Number of Elements versus Element Resolution")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-4, 1e-1)
#ax.set_ylim(1e3,1e9)
ax.set_ylim(1e3,1e7)
#ax.set_aspect(1.0)
ax.grid()

LABEL_ELEMENT_X = 0.12 # x coordinate for the element number labels

text_elements(LABEL_ELEMENT_X, 10000, '10 thousand')
text_elements(LABEL_ELEMENT_X, 100000, '100 thousand')
text_elements(LABEL_ELEMENT_X, 1000000, '1 million')
text_elements(LABEL_ELEMENT_X, 10000000, '10 million')

LABEL_ELEMENT_Y = 5e3 # y coordinate for the element length labels

text_elements_rotated(1e-3, LABEL_ELEMENT_Y, 'millimeter')
text_elements_rotated(1e-2, LABEL_ELEMENT_Y, 'centimeter')
text_elements_rotated(1e-1, LABEL_ELEMENT_Y, 'decimeter')

if PRINT_TO_PDF:
    # fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.pdf')
    fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.svg', dpi=300, bbox_inches='tight')
    FIG_NUM += 1

length_scales_others = [1.80E-03, 3.90E-03, 3.60E-03, 3.80E-03, 
4.60E-03, 3.20E-03, 1.00E-03, 2.40E-03, 2.50E-03, 1.60E-03, 
3.30E-03, 1.00E-03, 1.80E-03, 3.00E-03]

num_elements_others = [3.14E+05, 2.10E+04, 2.80E+04, 5.00E+04, 
1.30E+04, 4.60E+04, 2.00E+06, 9.80E+04, 2.70E+05, 1.17E+06, 
1.15E+05, 2.10E+06, 1.25E+06, 6.20E+04]

marker_style_others = dict(linestyle='none', marker='o', markersize=8, 
        markerfacecolor='magenta', markeredgecolor='black')
ax.plot(length_scales_others, num_elements_others, **marker_style_others)

if PRINT_TO_PDF:
    # fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.pdf')
    fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.svg', dpi=300, bbox_inches='tight')
    FIG_NUM += 1

length_scales_panzer = [2.07e-3, 1.07e-3, 1.69e-3, 0.99e-3, 0.84e-3, 4.0e-3, 2.0e-3, 1.0e-3]
num_elements_panzer = [45877, 345244, 250484, 990860, 1984051, 30228, 207514, 1526144] 

marker_style_panzer = dict(linestyle='none', marker='o', markersize=8, 
        markerfacecolor='orange', markeredgecolor='black')
ax.plot(length_scales_panzer, num_elements_panzer, **marker_style_panzer)

if PRINT_TO_PDF:
    # fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.pdf')
    fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.svg', dpi=300, bbox_inches='tight')
    FIG_NUM += 1

SANDIA_MARKER_SIZE = 12
ax.plot(2.0e-3, 735033, marker='v', markersize=SANDIA_MARKER_SIZE, markerfacecolor='cyan', 
        markeredgecolor='black') # Sandia coarse model at 2-mm edge length

ax.plot(1.0e-3, 5654227, marker='^', markersize=SANDIA_MARKER_SIZE, markerfacecolor='red', 
        markeredgecolor='black') # Sandia fine model at 1-mm edge length

if PRINT_TO_PDF:
    # fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.pdf')
    fig.savefig(FILE_BASE + '_' + str(FIG_NUM) + '.svg', dpi=300, bbox_inches='tight')
    FIG_NUM += 1

if (PRINT_TO_PDF == 0):
    plt.show()

