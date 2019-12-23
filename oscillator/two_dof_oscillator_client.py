#!/usr/bin/env python
# [base_directory]: $ python two_dof_oscillator_client input_file.json

import sys
import numpy as np
from scipy.integrate import odeint
import json

# ----------------
# input file begin

# parameters
m1 = 1.0  # kg
k1 = 100  # N/m

m2 = 1.0  # kg
k2 = 10  # N/m

# initial conditions
u1_at_0 = 0  # m
u1dot_at_0 = -1  # m/s

u2_at_0 = 0 # m
u2dot_at_0 = -1  # m/s

# ODE solver paramters
abs_error = 1.0e-8
rel_error = 1.0e-6

# simulation
t_start = 0.0  # seconds
t_stop = 2 * np.pi  # seconds
dt = 0.01  # seconds, delta_t time step; 100 Hz equivalent

# input file end
# --------------

if t_stop > t_start:
    nts = int((t_stop - t_start) / dt)
else:
    print(f'Time start and stop error.  Assure t_stop = {t_stop} > t_start = {t_start}')
    sys.exit('Error in time parameters input.')  # early exit 

t = np.linspace(t_start, t_stop, num=nts, endpoint=True)
