#!/usr/bin/env python
import sys
import numpy as np
from scipy import linalg
import json


def main(argv):

    help_string = "$ python client_experiment.py input_file.json"

    try:
        input_file = argv[0]
        input_file_base = input_file.split(".")[0]
    except IndexError as error:
        print(f"Error: {error}.")
        print("Check script pattern: " + help_string)
        print("Abnormal script termination.")
        sys.exit("No input file specified.")

    with open(input_file) as f:
        model = json.load(f)

    # mass
    m1 = model.get("m1", 1.0)  # kg
    m2 = model.get("m2", 1.0)  # kg

    # stiffness
    k1 = model.get("k1", 1.0)  # N/m
    k2 = model.get("k2", 1.0)  # N/m

    M = np.array([[m1, 0.0], [0.0, m2]])
    K = np.array([[k1 + k2, -k2], [-k2, k2]])

    eigenvalues = linalg.eigvals(K, M)
    frequencies = np.sqrt(eigenvalues)

    print("Initial frequency and period content:")
    for i, freq in enumerate(frequencies, start=1):
        period = 2 * np.pi / np.real(freq)
        print(
            f"  frequency {i}: {freq} radians/second    \n=>   period {i}: {period} seconds."
        )

    # period_max = 2 * np.pi / np.real(np.min(frequencies))  # second

    # initial conditions
    u1_at_0 = model.get("u1_at_0", 0.1)  # m
    u2_at_0 = model.get("u2_at_0", 0.0)  # m

    u1dot_at_0 = model.get("u1dot_at_0", 0.0)  # m/s
    u2dot_at_0 = model.get("u2dot_at_0", 0.0)  # m/s

    # # ODE solver paramters
    # abs_error = model.get("absolute_error", 1.0e-8)
    # rel_error = model.get("relative_error", 1.0e-6)

    # simulation
    t_start = model.get("time_start", 0.0)  # seconds
    # t_stop = model.get("time_stop", 0.5 * period_max)  # seconds
    t_stop = model.get("time_stop", 1.0)  # seconds
    dt = model.get(
        "time_step", 0.1
    )  # seconds, delta_t time step; 10 Hz equivalent default

    if t_stop > t_start:
        nts = int((t_stop - t_start) / dt)
    else:
        print(
            f"Time start and stop error.  Assure t_stop = {t_stop} > t_start = {t_start}"
        )
        sys.exit("Error in time parameters input.")  # early exit

    t = np.linspace(t_start, t_stop, num=nts, endpoint=True)

    # collect parameters and initial conditions
    # parameters = [m1, m2, k1, k2]
    # initial_conditions = [u1_at_0, u2_at_0, u1dot_at_0, u2dot_at_0]

    # solver_odeint = 0

    # if solver_odeint:
    #     # solution = odeint(dudt_rhs, initial_conditions, t, args=(parameters,), atol=abs_error, rtol=rel_error)
    #     # solution = odeint(dudt_rhs, initial_conditions, t, args=(parameters,), atol=abs_error, rtol=rel_error, printmessg=1)
    #     solution = odeint(dudt_rhs, initial_conditions, t, args=(parameters,), printmessg=1)
    #     # unpack displacements
    #     u1 = solution[:, 0]
    #     u2 = solution[:, 1]

    #     # unpack velocities
    #     u1dot = solution[:, 2]
    #     u2dot = solution[:, 3]

    # else:
    #     solution_ivp = solve_ivp(fun=lambda t, y: dudt_rhs_ivp(t, y, m1, m2, k1, k2), t_span=(t[0], t[-1]), y0=initial_conditions, method='RK45', t_eval=t)

    #     t = solution_ivp.t  # overwrite existing times and use from hereon

    #     # unpack displacements
    #     u1 = solution_ivp.y[0, :]
    #     u2 = solution_ivp.y[1, :]

    #     # unpack velocities
    #     u1dot = solution_ivp.y[2, :]
    #     u2dot = solution_ivp.y[3, :]

    # # accelerations
    # u1ddot = np.gradient(u1dot, t, edge_order=2)
    # u2ddot = np.gradient(u2dot, t, edge_order=2)

    use_surrogate_experiment = (
        1  #  0 for real experimental data, 1 for stand-in temporary data
    )

    if use_surrogate_experiment:
        # f1, f2 = 0.9, 2  # frequencies, per interval between t_start and t_stop
        # a1, a2 = 1, 1  # amplitudes, likely in units of Gs
        # p1, p2 = 0, 0.2  # phase shift, positive is in the +t direction
        # b1, b2 = 0, 1  # y-axis shift
        # T = t_stop - t_start

        # u2ddot_exp_f1 = a1 * np.sin(2 * np.pi * f1 * (t - p1) / T) + b1
        # u2ddot_exp_f2 = a2 * np.sin(2 * np.pi * f2 * (t - p2) / T) + b2
        # u2ddot_exp = u2ddot_exp_f1 + u2ddot_exp_f2
        # a = 4

        alpha = ((k1 + k2) * m2 + (k2 * m1)) / (m1 * m2)
        gamma = ((k1 + k2) * k2 - (k2 * k2)) / (m1 * m2)
        omega_squared_mode_1 = 0.5 * alpha - 0.5 * np.sqrt(alpha * alpha - 4.0 * gamma)
        omega_squared_mode_2 = 0.5 * alpha + 0.5 * np.sqrt(alpha * alpha - 4.0 * gamma)

        omega_mode_1 = np.sqrt(omega_squared_mode_1)
        omega_mode_2 = np.sqrt(omega_squared_mode_2)

        frequencies_check = [omega_mode_1, omega_mode_2]

        print("Frequency verification check with Rao 2011:")
        for i, freq in enumerate(frequencies_check, start=1):
            print(f"  frequency {i}: {freq} radians/second.")

        r1 = k2 / (-m2 * omega_squared_mode_1 + k2)  # r1 in Rao 2011 Eq 5.11
        r2 = k2 / (-m2 * omega_squared_mode_2 + k2)  # r2 in Rao 2011 Eq 5.11

        X1_mode_1a = r2 * u1_at_0 - u2_at_0
        X1_mode_1b = (-r2 * u1dot_at_0 + u2dot_at_0) / omega_mode_1

        # X1_mode_1 = 1.0 / (r2 - r1) * np.sqrt( np.power(X1_mode_1a, 2) + np.power(X1_mode_1b, 2) )
        X1_mode_1 = (
            -1.0
            / (r2 - r1)
            * np.sqrt(np.power(X1_mode_1a, 2) + np.power(X1_mode_1b, 2))
        )
        # X1_mode_1 = 1.0 / (r2 - r1) * np.sqrt( np.power(r2 * u1_at_0 - u2_at_0, 2) + np.power(-r2 * u1dot_at_0 - u2dot_at_0, 2) / omega_squared_mode_1 )
        # X1_mode_1 = np.abs( 1.0 / (r2 - r1) * np.sqrt( np.power(r2 * u1_at_0 - u2_at_0, 2) + np.power(-r2 * u1dot_at_0 - u2dot_at_0, 2) / omega_squared_mode_1 ))

        X1_mode_2a = -r1 * u1_at_0 + u2_at_0
        X1_mode_2b = (r1 * u1dot_at_0 - u2dot_at_0) / omega_mode_2

        # X1_mode_2 = 1.0 / (r2 - r1) * np.sqrt( np.power(X1_mode_2a, 2) + np.power(X1_mode_2b, 2) )
        X1_mode_2 = (
            -1.0
            / (r2 - r1)
            * np.sqrt(np.power(X1_mode_2a, 2) + np.power(X1_mode_2b, 2))
        )
        # X1_mode_2 = 1.0 / (r2 - r1) * np.sqrt( np.power(-r1 * u1_at_0 + u2_at_0, 2) + np.power(r1 * u1dot_at_0 - u2dot_at_0, 2) / omega_squared_mode_2 )
        # X1_mode_2 = np.abs(1.0 / (r2 - r1) * np.sqrt( np.power(-r1 * u1_at_0 + u2_at_0, 2) + np.power(r1 * u1dot_at_0 - u2dot_at_0, 2) / omega_squared_mode_2 ))

        phi_1 = np.arctan(X1_mode_1b / X1_mode_1a)
        phi_2 = np.arctan(X1_mode_2b / X1_mode_2a)

        amplitudes_check = [X1_mode_1, X1_mode_2]
        phases_check = [phi_1, phi_2]

        print("Amplitude and phase check with Rao 2011:")
        for i, amp in enumerate(amplitudes_check, start=1):
            print(f"  amplitude {i}: {amp} meters.")
        for i, phase in enumerate(phases_check, start=1):
            print(f"  phase {i}: {phase} radians.")

        # displacements
        u1 = X1_mode_1 * np.cos(omega_mode_1 * t + phi_1) + X1_mode_2 * np.cos(
            omega_mode_2 * t + phi_2
        )
        u2 = r1 * X1_mode_1 * np.cos(
            omega_mode_1 * t + phi_1
        ) + r2 * X1_mode_2 * np.cos(omega_mode_2 * t + phi_2)

    # # energies
    # ke1 = 0.5 * m1 * np.multiply(u1dot, u1dot)  # 1/2 m v^2
    # ke2 = 0.5 * m2 * np.multiply(u2dot, u2dot)
    # ke = ke1 + ke2

    # delta2 = u2 - u1
    # ie1 = 0.5 * k1 * np.multiply(u1, u1)  # u1 is the same as delta1, relative displacement
    # ie2 = 0.5 * k2 * np.multiply(delta2, delta2)
    # ie = ie1 + ie2

    # te = ke + ie   # total energy of the system, no gravity so no potential energy

    # # write solution to a file, write each channel as a separate file
    # channel_strings = ["u1", "u2", "u1dot", "u2dot", "u1ddot", "u2ddot", "ke", "ie", "te"]
    # channel_strings = ["u1_exp", "u2_exp", "u2ddot_exp_f1", "u2ddot_exp_f2", "u2ddot_exp"]
    # channel_strings = ["u1_exp", "u2_exp"]
    channel_strings = ["u1", "u2"]

    for str in channel_strings:
        file_string = input_file_base + "_t_" + str + ".csv"
        np.savetxt(file_string, np.transpose([t, eval(str)]), delimiter=",")
        print(f"Saved file: {file_string}")


if __name__ == "__main__":
    main(sys.argv[1:])
