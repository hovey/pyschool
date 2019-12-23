from scipy import linalg


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
    m1, k1, m2, k2 = parameters

    M = np.array([[m1, 0.0], [0.0, m2]])
    K = np.array([[k1 + k2, -k2], [-k2, k2]])

    eigenvalues = linalg.eigvals(M, K)

    rhs = [u3,
            u4,
            ( (k1 + k2) * u1 - k2 * u2) / (-1.0 * m1),
            ( -k2 * u1 + k2 * u2 / (-1.0 * m2))]
    return rhs
