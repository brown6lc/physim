import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def compute_g_force(m1, m2, r1, r2, G=6.67408e-11):

    r_vec = r1 - r2
    r_mag = np.linalg.norm(r_vec)
    r_hat = r_vec / r_mag
    F = G * m1 * m2 / r_mag**2 * r_hat

    return F

def compute_acceleration(m_self, pos_self, other_bodies):

    F_net = np.zeros(2)
    for m_other, pos_other in other_bodies:
        F_net += compute_g_force(m_self, m_other, pos_self, pos_other)
    a = F_net / m_self

    return a

def initial_conditions(m, r, v):
    # need n amt of m, r, v
    return 0
