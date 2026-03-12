import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def plot_trajectory(r1_list, r2_list, title="Trayectoria (m)"):
    plt.figure(figsize=(6, 6))
    plt.plot(r1_list[:, 0], r1_list[:, 1], label="Cuerpo 1")
    plt.plot(r2_list[:, 0], r2_list[:, 1], label="Cuerpo 2")
    plt.scatter(r1_list[0, 0], r1_list[0, 1], marker="o", color="blue")
    plt.scatter(r2_list[0, 0], r2_list[0, 1], marker="o", color="orange")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    plt.axis("equal")
    plt.grid(True)

def plot_energy(E_list, title="Energía total (J)"):
    plt.figure(figsize=(8, 4))
    plt.plot(E_list, color="green")
    plt.xlabel("Paso")
    plt.ylabel("Energía total (J)")
    plt.title(title)
    plt.grid(True)

def animate_trajectory(r1_list, r2_list, title="Animación"):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title(title)

    # Límites globales teniendo en cuenta toda la trayectoria
    all_x = np.concatenate([r1_list[:, 0], r2_list[:, 0]])
    all_y = np.concatenate([r1_list[:, 1], r2_list[:, 1]])
    margin = 0.5
    ax.set_xlim(all_x.min() - margin, all_x.max() + margin)
    ax.set_ylim(all_y.min() - margin, all_y.max() + margin)

    line1, = ax.plot([], [], color="blue", label="Cuerpo 1")
    line2, = ax.plot([], [], color="orange", label="Cuerpo 2")
    point1, = ax.plot([], [], "o", color="blue")
    point2, = ax.plot([], [], "o", color="orange")
    ax.legend()

    def update(frame):
        line1.set_data(r1_list[:frame, 0], r1_list[:frame, 1])
        line2.set_data(r2_list[:frame, 0], r2_list[:frame, 1])
        point1.set_data([r1_list[frame, 0]], [r1_list[frame, 1]])
        point2.set_data([r2_list[frame, 0]], [r2_list[frame, 1]])
        return line1, line2, point1, point2

    ani = FuncAnimation(fig, update, frames=len(r1_list), interval=20, blit=True)
    return ani