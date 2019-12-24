#!/usr/bin/env python
import numpy as np

def midpoint_dfdt(t, f):
    nts = t.size
    # test = 1
    # if test:
    #     nts = 4
    #     t = t[0:nts]  # overwrite a small block for testing
    #     f = f[0:nts]

    dt_initial = np.array([t[1] - t[0]])
    dt_internal = np.array([t[i+1] - t[i-1] for i in range(1, nts-1)])
    dt_final = np.array([t[-1] - t[-2]])
    dt = np.concatenate((dt_initial, dt_internal, dt_final))

    df_initial = np.array([f[1] - f[0]])
    df_internal = np.array([f[i+1] - f[i-1] for i in range(1, nts-1)])
    df_final = np.array([f[-1] - f[-2]])
    df = np.concatenate((df_initial, df_internal, df_final))

    a = np.divide(df, dt)
    return a

def main():

    import os
    import matplotlib.pyplot as plt

    fact = 4
    coef = 1.0/fact

    t_uniform = np.linspace(0, 4, 5, dtype=float)
    f_uniform = coef * np.multiply(t_uniform, t_uniform)

    t_nonuniform = np.array([0, 0.5, 1, 2, 2.25, 3.5, 3.75, 4], dtype=float)
    f_nonuniform = coef * np.multiply(t_nonuniform, t_nonuniform)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1kwargs = {"marker": "o", "color": "blue", "label": "input data"}
    ax1.plot(t_uniform, f_uniform, **ax1kwargs)
    ax1.legend(loc='upper left')
    function_string = 'function $f(t) = t^2/' + str(fact) + '$'
    ax1.set_title('uniform ' + function_string)
    ax1.set_xlabel('t (uniform $\Delta t$)')
    ax1.set_ylabel('f(t)')
    x0, x1 = -0.25, 4.25
    y0, y1 = -1, 5
    ax1.set(xlim=(x0, x1), ylim=(y0, y1))
    # ax1.set_aspect('equal')
    ax1.grid()

    ax2kwargs = {"marker": "o", "fillstyle": "none", "color": "blue", "label": "input data"}
    # ax2.plot(t_nonuniform, f_nonuniform, marker='o', fillstyle='none', color='blue', label='input data')
    ax2.plot(t_nonuniform, f_nonuniform, **ax2kwargs)
    ax2.legend(loc='upper left')
    ax2.set_title('nonuniform ' + function_string)
    ax2.set_xlabel('t (nonuniform $\Delta t$)')
    ax2.set_ylabel('f(t)')
    ax2.set(xlim=(x0, x1), ylim=(y0, y1))
    # ax2.set_aspect('equal')
    ax2.grid()

    # compute derivatives, with the midpoing definition and with numpy, compare
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.gradient.html
    dfdt_uniform_midpoint = midpoint_dfdt(t_uniform, f_uniform)
    dfdt_uniform_numpy1 = np.gradient(f_uniform, edge_order=1)
    dfdt_uniform_numpy2 = np.gradient(f_uniform, edge_order=2)

    ax3kwargs = {"marker": "o"}
    ax3.plot(t_uniform, dfdt_uniform_midpoint, markersize=6, linewidth=2.0, label='midpoint_dfdt', color='dimgray', **ax3kwargs)
    ax3.plot(t_uniform, dfdt_uniform_numpy1, markersize=4, linewidth=1.5, label='numpy g1', color='red', **ax3kwargs)
    ax3.plot(t_uniform, dfdt_uniform_numpy2, markersize=2, linewidth=1.0, label='numpy g2', color='darkblue', **ax3kwargs)
    ax3.legend(loc='upper left')
    ax3.set_title('uniform derivative $df/dt = t/2$')
    ax3.set_xlabel('t (uniform $\Delta t$)')
    ax3.set_ylabel('df/dt')
    ax3.set(xlim=(x0, x1), ylim=(y0, y1))
    # ax3.set_aspect('equal')
    ax3.grid()

    dfdt_nonuniform_midpoint = midpoint_dfdt(t_nonuniform, f_nonuniform)
    dfdt_nonuniform_numpy1 = np.gradient(f_nonuniform, t_nonuniform, edge_order=1)
    dfdt_nonuniform_numpy2 = np.gradient(f_nonuniform, t_nonuniform, edge_order=2)

    ax4kwargs = {"marker": "o", "fillstyle": "none"}
    ax4.plot(t_nonuniform, dfdt_nonuniform_midpoint, markersize=6, linewidth=2.0, label='midpoint_dfdt', color='dimgray', **ax4kwargs)
    ax4.plot(t_nonuniform, dfdt_nonuniform_numpy1, markersize=4, linewidth=1.5, label='numpy g1', color='red', **ax4kwargs)
    ax4.plot(t_nonuniform, dfdt_nonuniform_numpy2, markersize=2, linewidth=1.0, label='numpy g2', color='darkblue', **ax4kwargs)
    ax4.legend(loc='upper left')
    ax4.set_title('nonuniform derivative $df/dt = t/2$')
    ax4.set_xlabel('t (nonuniform $\Delta t$)')
    ax4.set_ylabel('df/dt')
    ax4.set(xlim=(x0, x1), ylim=(y0, y1))
    # ax4.set_aspect('equal')
    ax4.grid()

    # https://matplotlib.org/3.1.1/tutorials/intermediate/tight_layout_guide.html
    plt.tight_layout()  # attempt to prevent subplot overlap

    plt.show()

    _serialize = 1

    if _serialize:
        file_name = __file__.split('.')[0] + '.png'
        fig.savefig(file_name, dpi=300)
        print('Figure saved to folder: ' + os.getcwd())
        print(f'Figure file name: {file_name}')


if __name__ == '__main__':
    main()
