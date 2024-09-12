import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

fig.patch.set_facecolor('black')
numero_estrella = 75
n_giros = numero_estrella *5
radio_inicial = 0.1
aumento_radio = 0.3
angulo_giro = 145

x_vals, y_vals, z_vals = [], [], []

def update (i):
    ax.clear()
    angulo_rad = np.deg2rad(i * angulo_giro)
    radio = radio_inicial + aumento_radio *i

    x=radio * np.cos(angulo_rad)
    y=radio * np.sin(angulo_rad)
    z = i * 0.2

    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

    ax.plot(x_vals, y_vals, z_vals, color="red", lw=0.5)
    ax.set_xlim ([-numero_estrella *2, numero_estrella *2])
    ax.set_ylim ([-numero_estrella *2, numero_estrella *2])
    ax.set_zlim ([0, n_giros * 0.1])

    ax.set_title("Estrella 3D", color = "white")
     
    ax.set_xlabel("x", color="white")
    ax.set_ylabel("y", color="white")
    ax.set_zlabel("z", color="white")

    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.tick_params(axis="z", colors="white")

anim = FuncAnimation(fig, update, frames=n_giros, interval=50)

plt.show()