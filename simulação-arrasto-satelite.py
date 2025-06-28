import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

frames = 200
x = np.linspace(0, 10, frames)
decaimento_lento = np.linspace(0, 10, frames)
decaimento_rapido = np.linspace(0, 40, frames)
cor_fixa_tempestade = 'crimson'

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

np.random.seed(42)
px_top = np.random.uniform(0, 10, 100)
py_top = np.random.uniform(0.5, 4.5, 100)
vx_top = -np.random.uniform(0.005, 0.01, 100)

px_bottom = np.random.uniform(0, 10, 250)
py_bottom = np.random.uniform(-4.5, -0.5, 250)
vx_bottom = -np.random.uniform(0.03, 0.06, 250)

def update(frame):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(-5, 5)
    ax.set_title("Comparação de Movimento com e sem Tempestade Geomagnética")

    px_top_anim = (px_top + vx_top * frame) % 10
    px_bottom_anim = (px_bottom + vx_bottom * frame) % 10

    y_top = 2 - decaimento_lento[frame] * 0.05
    y_bottom = -2 - decaimento_rapido[frame] * 0.05
    ax.plot(x[frame], y_top, 's', color='darkblue', markersize=12)
    ax.plot(x[frame], y_bottom, 's', color=cor_fixa_tempestade, markersize=12)

    ax.plot(px_top_anim, py_top, '.', color='deepskyblue', alpha=0.5)
    ax.plot(px_bottom_anim, py_bottom, '.', color='orangered', alpha=0.5)

    for y in np.arange(0.5, 5, 1):
        ax.hlines(y, 0, 10, color='lightgray', linewidth=0.5, linestyles='dashed')
    for y in np.arange(-0.5, -5, -1):
        ax.hlines(y, 0, 10, color='lightgray', linewidth=0.5, linestyles='dashed')

    ax.text(0.5, 4.3, "Região sem tempestade", color='blue', fontsize=10)
    ax.text(0.5, -4.7, "Região com tempestade", color='darkred', fontsize=10)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
    ax.set_xticks([])
    ax.set_yticks([])

ani = animation.FuncAnimation(fig, update, frames=frames, interval=30)
ani.save("simulacao_blocos_tempestade.gif", writer='pillow', fps=60)
plt.show()
