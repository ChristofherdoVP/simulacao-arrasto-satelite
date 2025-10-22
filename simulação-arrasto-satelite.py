# -------------------------------------------------------------
# Simulação didática: Comparação de movimento de partículas e blocos
# com e sem tempestade geomagnética, representando o efeito de aumento
# de densidade e arrasto na termosfera.
# -------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Número total de quadros da animação
frames = 200

# Eixo horizontal (0 a 10 unidades) representando o espaço ou tempo normalizado
x = np.linspace(0, 10, frames)

# Criação de vetores para simular o deslocamento vertical (decaimento) das partículas
decaimento_lento = np.linspace(0, 10, frames)   # movimento mais lento (sem tempestade)
decaimento_rapido = np.linspace(0, 40, frames)  # movimento mais rápido (com tempestade)

# Cor que representa a região de tempestade geomagnética
cor_fixa_tempestade = 'crimson'

# Criação da figura e dos eixos para o gráfico animado
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

# Geração de posições aleatórias de partículas na região superior e inferior
# A parte superior representa o ambiente sem tempestade geomagnética,
# enquanto a parte inferior representa o ambiente afetado por uma tempestade.
np.random.seed(42)  # garante reprodutibilidade da simulação

# Região superior — partículas em movimento lento
px_top = np.random.uniform(0, 10, 100)
py_top = np.random.uniform(0.5, 4.5, 100)
vx_top = -np.random.uniform(0.005, 0.01, 100)

# Região inferior — partículas em movimento rápido (devido ao aumento de arrasto)
px_bottom = np.random.uniform(0, 10, 250)
py_bottom = np.random.uniform(-4.5, -0.5, 250)
vx_bottom = -np.random.uniform(0.03, 0.06, 250)

# -------------------------------------------------------------
# Função que atualiza cada quadro da animação
# -------------------------------------------------------------
def update(frame):
    # Limpa o quadro anterior e redefine os eixos
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(-5, 5)
    ax.set_title("Comparação de Movimento com e sem Tempestade Geomagnética")

    # Atualiza as posições das partículas ao longo do tempo
    px_top_anim = (px_top + vx_top * frame) % 10
    px_bottom_anim = (px_bottom + vx_bottom * frame) % 10

    # Define o deslocamento vertical dos blocos que representam satélites ou objetos
    y_top = 2 - decaimento_lento[frame] * 0.05     # sem tempestade
    y_bottom = -2 - decaimento_rapido[frame] * 0.05  # com tempestade

    # Plota os blocos principais (representando satélites) em ambas as regiões
    ax.plot(x[frame], y_top, 's', color='darkblue', markersize=12)
    ax.plot(x[frame], y_bottom, 's', color=cor_fixa_tempestade, markersize=12)

    # Plota as partículas em movimento
    ax.plot(px_top_anim, py_top, '.', color='deepskyblue', alpha=0.5)
    ax.plot(px_bottom_anim, py_bottom, '.', color='orangered', alpha=0.5)

    # Linhas horizontais pontilhadas para indicar camadas atmosféricas
    for y in np.arange(0.5, 5, 1):
        ax.hlines(y, 0, 10, color='lightgray', linewidth=0.5, linestyles='dashed')
    for y in np.arange(-0.5, -5, -1):
        ax.hlines(y, 0, 10, color='lightgray', linewidth=0.5, linestyles='dashed')

    # Textos descritivos
    ax.text(0.5, 4.3, "Região sem tempestade", color='blue', fontsize=10)
    ax.text(0.5, -4.7, "Região com tempestade", color='darkred', fontsize=10)

    # Linha divisória central (altitude de referência)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)

    # Remove eixos numéricos para deixar a visualização mais limpa
    ax.set_xticks([])
    ax.set_yticks([])

# Cria a animação: chama a função 'update' a cada frame
ani = animation.FuncAnimation(fig, update, frames=frames, interval=30)

# Salva a animação em formato GIF
ani.save("simulacao_blocos_tempestade.gif", writer='pillow', fps=60)

# Exibe a simulação
plt.show()
