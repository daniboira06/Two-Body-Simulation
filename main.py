import numpy as np
from two_body import compute_acceleration, compute_energy
from integrators import euler_step, verlet_step, rk4_step
import matplotlib.pyplot as plt

# ── Parámetros iniciales ──────────────────────────────────────────
m1, m2 = 1.0, 1.0
r1 = np.array([1.0, 0.0])
r2 = np.array([-1.0, 0.0])
v1 = np.array([0.0, 0.8])
v2 = np.array([0.0, -0.8])

dt = 0.01       # paso de tiempo
N  = 1000       # número de pasos
integrador = verlet_step   # prueba cambiando a euler_step o rk4_step

# ── Listas para guardar resultados ───────────────────────────────
r1_list = [r1.copy()]
r2_list = [r2.copy()]
v1_list = [v1.copy()]
v2_list = [v2.copy()]

E_list = [compute_energy(r1, r2, v1, v2, m1, m2)]

# ── Bucle de simulación ───────────────────────────────────────────
for i in range(N):
    r1, r2, v1, v2 = integrador(r1, r2, v1, v2, m1, m2, dt)
    r1_list.append(r1.copy())
    r2_list.append(r2.copy())
    v1_list.append(v1.copy())
    v2_list.append(v2.copy())
    E_list.append(compute_energy(r1, r2, v1, v2, m1, m2))

# ── Convertir a arrays ────────────────────────────────────────────
r1_list = np.array(r1_list)
r2_list = np.array(r2_list)

print("Simulación completada!")
print(f"Pasos: {N} | dt: {dt} | Integrador: {integrador.__name__}")
print(f"Posición final cuerpo 1: {r1}")
print(f"Posición final cuerpo 2: {r2}")

from plots import plot_trajectory, plot_energy, animate_trajectory

plot_trajectory(r1_list, r2_list, title=f"Trayectoria - {integrador.__name__}")
plot_energy(E_list, title=f"Energía - {integrador.__name__}")
ani = animate_trajectory(r1_list, r2_list, title=f"Animación - {integrador.__name__}")
plt.show()