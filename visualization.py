import matplotlib.pyplot as plt
import time
from config import WIDTH, HEIGHT

def visualize_step(turn, survivor, zombies, survivor_path, zombies_paths):
    plt.clf()
    plt.xlim(-0.5, WIDTH - 0.5)
    plt.ylim(-0.5, HEIGHT - 0.5)
    plt.title(f"Turno {turn}")
    plt.gca().invert_yaxis()

    # Dibujar posiciones
    sx, sy = survivor
    plt.scatter(sx, sy, color="green", s=120, label="Sobreviviente")

    zx, zy = zip(*zombies)
    plt.scatter(zx, zy, color="red", s=80, label="Zombies")

    # Trayectoria
    if len(survivor_path) > 1:
        sx, sy = zip(*survivor_path)
        plt.plot(sx, sy, 'g--', alpha=0.6)

    plt.legend()
    plt.pause(0.2)  # velocidad más rápida
