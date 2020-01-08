#!/usr/bin/env python
# Client to create figures for Military Specification journal manuscript.
# To run from command line with Python3:
# [base_directory]: $ python XYFigure.py

import os
# import sys
from abc import ABC
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

#from matplotlib import rc
#rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
#rc('text', usetex=True)

# Figure Service
## Abstract Base Class
class XYBase(ABC):
    """
    Base class to collect all data and methods common to XYBase descendants.
    """
    def __init__(self, **kwargs):
        self._folder = kwargs['folder']
        self._file = kwargs['file']


## Model
class XYModel(XYBase):
    """The data to be plotted in XY format."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # N_SKIP = 1  # skip the first row of the input file
        # self._data = np.genfromtxt(self._file, dtype='float', delimiter=',', skip_header=N_SKIP)
        self._skip_rows = kwargs.get('skip_rows', 0)
        self._data = np.genfromtxt(self._file, dtype='float', delimiter=',', skip_header=self._skip_rows)

        # default value if plot_kwargs not client-supplied
        default = {'linewidth': 2, 'linestyle': '-'}
        self._plot_kwargs = kwargs.get('plot_kwargs', default)

        self._inverted = kwargs.get('inverted', False)
        self._xoffset = kwargs.get('xoffset', 0.0)
        a=4

    @property
    def x(self):
        """Returns the model's x data."""
        return self._data[:, 0]

    @property
    def y(self):
        """Returns the model's y data."""
        return self._data[:, 1]

    @property
    def plot_kwargs(self):
        """Returns kwargs passed to matplotlib.pyplot.plot()."""
        return self._plot_kwargs

    @property
    def is_inverted(self):
        return self._inverted

## View
class XYView(XYBase):
    """Creates a view that sees models."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._models = []
        self._figure = None
        self._folder = kwargs.get('folder', None)
        self._file_base = self._file.split('.')[0]

        # default value if figure_kwargs not client-supplied
        now = datetime.now()
        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        default = self._file_base + ' ' + now_string
        self._title = kwargs.get('title', default)
        self._xlabel = kwargs.get('xlabel', 'default x axis label')
        self._ylabel = kwargs.get('ylabel', 'default y axis label')

        # default = {'scale': 1, 'label': 'ylabel_rhs', 'verification': 0}
        self._yaxis_rhs = kwargs.get('yaxis_rhs', None)

        # default value if figure_kwargs not client-supplied
        default = {'figsize': '(11.0, 8.5)'}  # inches, U.S. paper, landscape
        self._figure_args = kwargs.get('figure_args', default)

        self._display = kwargs.get('display', True)
        self._serialize = kwargs.get('serialize', False)
        self._latex = kwargs.get('latex', False)
        if self._latex:
            from matplotlib import rc
            #rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
            rc('text', usetex=True)
            rc('font', family='serif')

        a=4

    @property
    def models(self):
        return self._models

    @models.setter
    def models(self, value):
        self._models = value

    def figure(self):
        """Create a figure (view) of the registered models to the screen."""
        if self._figure is None:

            # fig, ax = plt.subplots(nrows=1, **self._figure_args)
            # fig, ax = plt.subplots(nrows=1)  # temporary
            # fig, ax = plt.subplots(nrows=1, figsize=figsize_tuple)
            fig, ax = plt.subplots(nrows=1)

            figsize_tuple_str = self._figure_args.get('figsize', None)
            if figsize_tuple_str:
                figsize_tuple = eval(figsize_tuple_str)
                fig.set_size_inches(figsize_tuple)

            #fig.set_size_inches(figsize_tuple)  # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.set_size_inches
            # self._folder = kwargs.get('folder', None)

            for model in self._models:
                if model.is_inverted:
                    ax.plot(model.x + model._xoffset, -1.0 * model.y, **model.plot_kwargs)
                else:
                    ax.plot(model.x + model._xoffset, model.y, **model.plot_kwargs)

            if self._yaxis_rhs:
                rhs_axis_scale = self._yaxis_rhs.get('scale', 1)
                rhs_axis_label = self._yaxis_rhs.get('label', None)

                ax_rhs = fig.add_subplot(111, sharex=ax, frameon=False)
                bottom, top = ax.get_ylim()
                ax_rhs.set_ylim(rhs_axis_scale * bottom, rhs_axis_scale * top)
                ax_rhs.yaxis.tick_right()
                ax_rhs.yaxis.set_label_position('right')
                ax_rhs.set_ylabel(rhs_axis_label)

            xlim_tuple_str = self._figure_args.get('xlim', None)
            if xlim_tuple_str:
                ax.set_xlim(eval(xlim_tuple_str))

            ylim_tuple_str = self._figure_args.get('ylim', None)
            if ylim_tuple_str:
                ax.set_ylim(eval(ylim_tuple_str))

            fig.suptitle(self._title)
            ax.set_xlabel(self._xlabel)
            ax.set_ylabel(self._ylabel)
            ax.grid()
            ax.legend()
            if self._display:
                plt.show()
            if self._serialize:
                folder = self._folder
                if folder:
                    try:
                        os.chdir(folder)
                    except FileNotFoundError:
                        print(f'Folder needed but not available: "{folder}"')
                fig.savefig(self._file, dpi=300)
                print('Figure saved to folder: ' + os.getcwd())
                print(f'Figure filename: {self._file}')

        #return fig, ax  # return so clients to further embellish

## Figure Factory
FACTORY_ITEMS = {
    'model': XYModel,
    'view': XYView
}

class XYFactory:
    """The one and only (singleton) factory for XY items."""
    @staticmethod
    def create(item, **kwargs):
        "Main factory method, returns XY objects."
        instance = FACTORY_ITEMS.get(kwargs['class'], None)
        if instance:
            return instance(**kwargs)

        # If we get here, we did not return an instance, so warn.
        print(f'Warning: {item} requested but not provided by this factory, returning None.')
        return None
