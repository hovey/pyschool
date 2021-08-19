#!/usr/bin/env python
import os

# import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


class DistributionPlotter:
    def __init__(self, file):
        self.home = os.getcwd()
        self.file = file
        self.base = self.file.split(".")[0]
        self.months_to_years = (
            1.0 / 12.0
        )  # convert months to years, dataset is in months, want plot in years
        self.data_x = None
        self.data_y = None

    def check_file_schema(self):
        print(f"Searching for input file: {self.file}")
        if os.path.isfile(self.file):
            print("Success: file exists.")
        else:
            print("Error: file does not exist.")
            return  # early return because file does not exist
            # sys.exit()  # early return because file does not exist

    def file_io(self, x_column=1, y_columns=[2]):
        n_header_rows = 1  # number of header rows to be skipping when reading input
        d = os.path.join(self.home, self.file)
        data = np.genfromtxt(d, dtype="float", delimiter=",", skip_header=n_header_rows)

        self.data_x = data[:, x_column] * self.months_to_years  # years, age
        self.data_y = data[:, y_columns]  # cm, stature

        # print('Input data x values:')
        # print(self.data_x)
        # print('Input data y values:')
        # print(self.data_y)

    def plot(
        self, label_x="x", label_y="y", t="title", show_plot=1, save_to_file=0, **kwargs
    ):
        p05 = 0  # 5th percentile
        p10 = 1  # 10th percentile
        p25 = 2  # etc
        p50 = 3
        p75 = 4
        p90 = 5
        p95 = 6
        x_lim = kwargs.get("x_limits", [self.data_x[0], self.data_x[-1]])
        y_lim = kwargs.get(
            "y_limits", [np.min(self.data_y[0, p05]), np.min(self.data_y[-1, p95])]
        )
        #
        fig, ax = plt.subplots(nrows=1, figsize=(11, 8.5))
        #
        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)
        ax.xaxis.set_major_locator(MultipleLocator(1.0))  # every year
        ax.yaxis.set_major_locator(MultipleLocator(10.0))  # every 10 cm
        ax.grid(linestyle="--", linewidth=0.5)
        #
        # ax.plot(self.data_x, self.data_y, 'b')  # plot all curves the same color
        #
        color_str = "#3399ff"  # blue rgb(0, 51, 102) at 60 percent
        ax.fill_between(
            self.data_x, self.data_y[:, p05], self.data_y[:, p95], facecolor=color_str
        )
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p05],
            "5",
            va="top",
            ha="right",
            color=color_str,
        )  # 5th percentile
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p95],
            "95",
            va="bottom",
            ha="right",
            color=color_str,
        )  # 95th percentile
        #
        color_str = "#0066cc"  # blue rgb(0, 51, 102) at 40 percent
        ax.fill_between(
            self.data_x, self.data_y[:, p10], self.data_y[:, p90], facecolor=color_str
        )
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p10],
            "10",
            va="top",
            ha="right",
            color=color_str,
        )  # 10th percentile
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p90],
            "90",
            va="bottom",
            ha="right",
            color=color_str,
        )  # 90th percentile
        #
        color_str = "#003366"  # blue rgb(0, 51, 102) at 20 percent
        ax.fill_between(
            self.data_x, self.data_y[:, p25], self.data_y[:, p75], facecolor=color_str
        )
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p25],
            "25",
            va="top",
            ha="right",
            color=color_str,
        )  # 25th percentile
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p75],
            "75",
            va="bottom",
            ha="right",
            color=color_str,
        )  # 75th percentile
        #
        # color_str = '#000000'  # black
        # color_str = '#ffffff'  # white
        color_str = "#ffff00"  # yellow
        ax.plot(
            self.data_x, self.data_y[:, p50], linewidth=2, color=color_str
        )  # 50th percentile
        ax.text(
            self.data_x[-1],
            self.data_y[-1, p50],
            "50",
            va="bottom",
            ha="right",
            color=color_str,
        )  # 50th percentile
        #
        ax.set_title(t)
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        if show_plot:
            plt.show()
        if save_to_file:
            fig.savefig(self.base + ".svg", bbox_inches="tight", dpi=600)


if __name__ == "__main__":
    # globals
    file_index = 0
    title_index = 1
    x_index = 1  # column 2, account for zero index
    y_index = list(range(6, 13))  # columns of distributions 5% to 95%
    show_figure = 1
    save_figure = 1
    title_base = "stature-for-age:"
    title_age_range = "2 to 20 years"

    population = [
        ("statage_male.csv", title_base + " males " + title_age_range),
        ("statage_female.csv", title_base + " females " + title_age_range),
    ]

    for item in population:
        h = DistributionPlotter(item[file_index])
        h.check_file_schema()
        h.file_io(x_index, y_index)
        x_label = "age (years)"
        y_label = "stature (cm)"
        h.plot(
            x_label,
            y_label,
            item[title_index],
            show_figure,
            save_figure,
            x_limits=[1, 21],
            y_limits=[70, 200],
        )
