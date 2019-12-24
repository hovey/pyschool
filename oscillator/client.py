#!/usr/bin/env python
import sys
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy import linalg
import json

def dudt_rhs(state_variables, time, parameters=[1, 1, 1, 1]):
    """ Returns the right-hand-side (RHS) vector for the system of 
    first-order ordinary differential equations describing the two
    degree of freedom (DOF) spring mass system.

    No gravity.

    m1 u1'' + (k1 + k2) u1 - k2 u2 = 0
    m2 u2''       - k2  u1 + k2 u2 = 0

    Let
        u3 = u1'  # velocity of u1
        u4 = u2'  # velocity of u2

    Then

        LHS = RHS
        LHS = [u1', u2', u3', u4'] = dydt
        
        RHS = 
            [ u3,
              u4,
              ( (k1 + k2) u1 - k2 u2 ) / (-m1),
              ( -k2 u1 + k2 u2 ) / (-m2)
            ]
    """
    u1, u2, u3, u4 = state_variables
    m1, m2, k1, k2 = parameters


    rhs = [u3,
           u4,
           ( (k1 + k2) * u1 - k2 * u2) / (-1.0 * m1),
           ( -k2 * u1 + k2 * u2 ) / (-1.0 * m2)]
    return rhs

    
def dudt_rhs_ivp(t, y, m1, m2, k1, k2):
    """ Returns the right-hand-side (RHS) vector for the system of 
    first-order ordinary differential equations describing the two
    degree of freedom (DOF) spring mass system.

    No gravity.

    m1 u1'' + (k1 + k2) u1 - k2 u2 = 0
    m2 u2''       - k2  u1 + k2 u2 = 0

    Let
        u3 = u1'  # velocity of u1
        u4 = u2'  # velocity of u2

    Then

        LHS = RHS
        LHS = [u1', u2', u3', u4'] = dydt
        
        RHS = 
            [ u3,
              u4,
              ( (k1 + k2) u1 - k2 u2 ) / (-m1),
              ( -k2 u1 + k2 u2 ) / (-m2)
            ]
    """
    # u1, u2, u3, u4 = state_variables
    u1, u2, u3, u4 = y
    # m1, m2, k1, k2 = parameters


    rhs = [u3,
           u4,
           ( (k1 + k2) * u1 - k2 * u2) / (-1.0 * m1),
           ( -k2 * u1 + k2 * u2 ) / (-1.0 * m2)]
    return rhs

def dvdt(t, v):
    nts = t.size
    # test = 1
    # if test:
    #     nts = 4
    #     t = t[0:nts]  # overwrite a small block for testing
    #     v = v[0:nts]

    dt_initial = np.array([t[1] - t[0]])
    dt_internal = np.array([t[i+1] - t[i-1] for i in range(1, nts-1)])
    dt_final = np.array([t[-1] - t[-2]])
    dt = np.concatenate((dt_initial, dt_internal, dt_final))

    dv_initial = np.array([v[1] - v[0]])
    dv_internal = np.array([v[i+1] - v[i-1] for i in range(1, nts-1)])
    dv_final = np.array([v[-1] - v[-2]])
    dv = np.concatenate((dv_initial, dv_internal, dv_final))

    a = np.divide(dv, dt)
    return a

def main(argv):

    help_string = '$ python client.py input_file.json'

    try:
        input_file = argv[0]
        input_file_base = input_file.split('.')[0]
    except IndexError as error:
        print(f'Error: {error}.')
        print('Check script pattern: ' + help_string)
        print('Abnormal script termination.')
        sys.exit('No input file specified.')

    with open(input_file) as f:
        model = json.load(f)

    # mass
    m1 = model.get("m1", 1.0)  # kg
    m2 = model.get("m2", 1.0)  # kg

    # stiffness
    k1 = model.get("k1", 1.0)  # N/m
    k2 = model.get("k2", 1.0)  # N/m

    # initial conditions
    u1_at_0 = model.get("u1_at_0", 0.1)  # m
    u2_at_0 = model.get("u2_at_0", 0.0)  # m

    u1dot_at_0 = model.get("u1dot_at_0", 0.0)  # m/s
    u2dot_at_0 = model.get("u2dot_at_0", 0.0)  # m/s

    # ODE solver paramters
    abs_error = model.get("absolute_error", 1.0e-8)
    rel_error = model.get("relative_error", 1.0e-6)

    # simulation
    t_start = model.get("time_start", 0.0)  # seconds
    t_stop = model.get("time_stop", 1.0)  # seconds
    dt = model.get("time_step", 0.1)  # seconds, delta_t time step; 10 Hz equivalent default

    if t_stop > t_start:
        nts = int((t_stop - t_start) / dt)
    else:
        print(f'Time start and stop error.  Assure t_stop = {t_stop} > t_start = {t_start}')
        sys.exit('Error in time parameters input.')  # early exit 
    
    t = np.linspace(t_start, t_stop, num=nts, endpoint=True)

    # collect parameters and initial conditions
    parameters = [m1, m2, k1, k2]
    initial_conditions = [u1_at_0, u2_at_0, u1dot_at_0, u2dot_at_0]

    M = np.array([[m1, 0.0], [0.0, m2]])
    K = np.array([[k1 + k2, -k2], [-k2, k2]])

    eigenvalues = linalg.eigvals(K, M)
    frequencies = np.sqrt(eigenvalues)

    print('Initial frequency and period content:')
    for i, freq in enumerate(frequencies, start=1):
        period = 2 * np.pi / freq
        print(f'  frequency {i}: {freq} radians/second    =>    period {i}: {period} seconds.')

    solver_odeint = 0
    
    if solver_odeint:
        # solution = odeint(dudt_rhs, initial_conditions, t, args=(parameters,), atol=abs_error, rtol=rel_error)
        # solution = odeint(dudt_rhs, initial_conditions, t, args=(parameters,), atol=abs_error, rtol=rel_error, printmessg=1)
        solution = odeint(dudt_rhs, initial_conditions, t, args=(parameters,), printmessg=1)
        # unpack displacements
        u1 = solution[:, 0]
        u2 = solution[:, 1]

        # unpack velocities
        u1dot = solution[:, 2]
        u2dot = solution[:, 3]

    else:
        solution_ivp = solve_ivp(fun=lambda t, y: dudt_rhs_ivp(t, y, m1, m2, k1, k2), t_span=(t[0], t[-1]), y0=initial_conditions, method='RK45', t_eval=t)

        t = solution_ivp.t  # overwrite existing times and use from hereon

        # unpack displacements
        u1 = solution_ivp.y[0, :]
        u2 = solution_ivp.y[1, :]
    
        # unpack velocities
        u1dot = solution_ivp.y[2, :]
        u2dot = solution_ivp.y[3, :]

    # accelerations
    u1ddot = dvdt(t, u1dot)
    u2ddot = dvdt(t, u2dot)

    # energies
    ke1 = 0.5 * m1 * np.multiply(u1dot, u1dot)  # 1/2 m v^2
    ke2 = 0.5 * m2 * np.multiply(u2dot, u2dot)
    ke = ke1 + ke2

    delta2 = u2 - u1
    ie1 = 0.5 * k1 * np.multiply(u1, u1)  # u1 is the same as delta1, relative displacement
    ie2 = 0.5 * k2 * np.multiply(delta2, delta2)
    ie = ie1 + ie2

    te = ke + ie   # total energy of the system, no gravity so no potential energy

    # write solution to a file, write each channel as a separate file
    channel_strings = ["u1", "u2", "u1dot", "u2dot", "u1ddot", "u2ddot", "ke", "ie", "te"]

    for str in channel_strings:
        file_string = input_file_base + '_t_' + str + '.csv'
        np.savetxt(file_string, np.transpose([t, eval(str)]), delimiter=',')
        print(f'Saved file: {file_string}')



if __name__ == '__main__':
    main(sys.argv[1:])
