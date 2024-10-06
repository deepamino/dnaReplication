import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Crear figura y eje
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(-5, 5)

threshold = 30
cycle_duration = 400
replication_start = 100
leader_full_progress = 300

plt.title("DNA Replication Process\nSemi-Conservative Model")

# Inicializar las líneas
line1, = ax.plot([], [], lw=2, label="Leading Strand")
line2, = ax.plot([], [], lw=2, label="Lagging Strand")
leader_line, = ax.plot([], [], lw=2, linestyle='--', color='blue', label="Leading Strand Replica")
okazaki_line, = ax.plot([], [], lw=2, linestyle='--', color='orange', label="Okazaki Fragments")

# Definir el ancho de la figura en caracteres
fig_width_in_chars = 120

# Crear objetos de texto
nucleotide_text = ax.text(5, 1.7, '', fontsize=12, ha='center', va='center')
comp_nucleotide_text = ax.text(5, -1.7, '', fontsize=12, ha='center', va='center')

ax.legend()

def random_nucleotide_sequence(length):
    nucleotides = ['A', 'T', 'G', 'C']
    if not hasattr(random_nucleotide_sequence, 'sequence'):
        random_nucleotide_sequence.sequence = [random.choice(nucleotides) for _ in range(length)]
    else:
        random_nucleotide_sequence.sequence = random_nucleotide_sequence.sequence[1:] + [random.choice(nucleotides)]
    return ' '.join(random_nucleotide_sequence.sequence)

def complement_chain(chain):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', ' ': ' '}
    return ''.join([complement[n] for n in chain])

def init():
    """Inicializa las líneas vacías y el texto de nucleótidos"""
    line1.set_data([], [])
    line2.set_data([], [])
    leader_line.set_data([], [])
    okazaki_line.set_data([], [])
    nucleotide_text.set_text('')
    comp_nucleotide_text.set_text('')
    return line1, line2, leader_line, okazaki_line, nucleotide_text

def animate(i):
    """Actualiza las funciones en cada frame y simula la replicación de ADN"""
    x = np.linspace(0, 20, 100)

    if i == cycle_duration:
        plt.close()

    leader_x = np.array([])
    leader_y = np.array([])
    okazaki_x = np.array([])
    okazaki_y = np.array([])

    phase = i % cycle_duration

    if phase > threshold:
        smooth_factor = np.exp(-(phase - threshold) * 0.05) if phase <= leader_full_progress else np.exp(-(cycle_duration - phase) * 0.05)

        y1 = (np.sin(x + 0.1 * i) * smooth_factor) + (1 - smooth_factor)
        y2 = (np.sin(x + 0.1 * i - np.pi) * smooth_factor) - (1 - smooth_factor)

    else:
        y1 = np.sin(x + 0.1 * i)
        y2 = np.sin(x + 0.1 * i - np.pi)

    line1.set_data(x, y1)
    line2.set_data(x, y2)

    if threshold <= phase <= leader_full_progress:
        okazaki_fragment_length = 20 
        if phase >= replication_start + okazaki_fragment_length:
            leader_progress = (phase - replication_start) / (leader_full_progress - replication_start)
            leader_x = x[:int(leader_progress * len(x))]
            leader_y = y1[:int(leader_progress * len(y1))] - 0.3
            leader_line.set_data(leader_x, leader_y)

            okazaki_progress = (phase - replication_start) / (leader_full_progress - replication_start)
            num_fragments = int(okazaki_progress * len(x) / okazaki_fragment_length)
            for f in range(num_fragments):
                start = f * okazaki_fragment_length
                end = start + okazaki_fragment_length

                if end > len(x):
                    end = len(x)

                okazaki_x = np.append(okazaki_x, x[start:end]) 
                okazaki_y = np.append(okazaki_y, y2[start:end] + 0.3) 

                if len(okazaki_x) > 0:
                    okazaki_line.set_data(okazaki_x, okazaki_y)

    else:
        leader_line.set_data([], [])
        okazaki_line.set_data([], [])

    if phase > leader_full_progress and phase <= cycle_duration - threshold:
        removal_progress = (phase - leader_full_progress) / (cycle_duration - threshold - leader_full_progress)
        smooth_removal = 0.5 * (1 - np.cos(removal_progress * np.pi))

        leader_x_end = int(len(leader_x) * (1 - smooth_removal))
        okazaki_x_end = int(len(okazaki_x) * (1 - smooth_removal))
        leader_line.set_data(leader_x[:leader_x_end], leader_y[:leader_x_end])
        okazaki_line.set_data(okazaki_x[:okazaki_x_end], okazaki_y[:okazaki_x_end])

    nucleotide_sequence = random_nucleotide_sequence(fig_width_in_chars)
    nucleotide_text.set_text(nucleotide_sequence)
    comp_nucleotide_sequence = complement_chain(nucleotide_sequence)
    comp_nucleotide_text.set_text(comp_nucleotide_sequence)

    return line1, line2, leader_line, okazaki_line, nucleotide_text, comp_nucleotide_text

# Crear la animación
anim = FuncAnimation(fig, animate, init_func=init, frames=1000, interval=50, blit=True)

# Guardar la animación como un archivo de video
anim.save('dna_replication_process.mp4', writer='ffmpeg', fps=30)

# Mostrar la animación
plt.show()
