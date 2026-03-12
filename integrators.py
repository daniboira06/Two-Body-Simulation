import numpy as np
from two_body import compute_acceleration

def euler_step(r1, r2, v1, v2, m1, m2, dt):
    a1, a2 = compute_acceleration(r1, r2, m1, m2)
    r1_new = r1 + v1 * dt
    r2_new = r2 + v2 * dt
    v1_new = v1 + a1 * dt
    v2_new = v2 + a2 * dt
    return r1_new, r2_new, v1_new, v2_new

def verlet_step(r1, r2, v1, v2, m1, m2, dt):
    a1, a2 = compute_acceleration(r1, r2, m1, m2)
    r1_new = r1 + v1 * dt + 0.5 * a1 * dt**2
    r2_new = r2 + v2 * dt + 0.5 * a2 * dt**2
    a1_new, a2_new = compute_acceleration(r1_new, r2_new, m1, m2)
    v1_new = v1 + 0.5 * (a1 + a1_new) * dt
    v2_new = v2 + 0.5 * (a2 + a2_new) * dt
    return r1_new, r2_new, v1_new, v2_new

def rk4_step(r1, r2, v1, v2, m1, m2, dt):
    # k1
    a1_1, a2_1 = compute_acceleration(r1, r2, m1, m2)
    # k2
    a1_2, a2_2 = compute_acceleration(r1 + 0.5*v1*dt, r2 + 0.5*v2*dt, m1, m2)
    # k3
    a1_3, a2_3 = compute_acceleration(r1 + 0.5*v1*dt, r2 + 0.5*v2*dt, m1, m2)
    # k4
    a1_4, a2_4 = compute_acceleration(r1 + v1*dt, r2 + v2*dt, m1, m2)

    r1_new = r1 + v1 * dt
    r2_new = r2 + v2 * dt
    v1_new = v1 + (dt/6) * (a1_1 + 2*a1_2 + 2*a1_3 + a1_4)
    v2_new = v2 + (dt/6) * (a2_1 + 2*a2_2 + 2*a2_3 + a2_4)
    return r1_new, r2_new, v1_new, v2_new