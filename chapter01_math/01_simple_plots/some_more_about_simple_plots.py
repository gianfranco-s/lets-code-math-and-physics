import os
import numpy as np
import matplotlib.pyplot as plt
import math

N = 100  # Samples
T = 2 * math.pi  # Period
Tfin = 1 * T  # End time
Tini = 0  # Start time

t = np.linspace(Tini, Tfin, N)  # Check sine_wave.py if you're lost

fun01 = np.sin(t)
fun02 = np.sin(3 * t)
fun03 = 2 * np.sin(3 * t + math.pi / 2) + 1

plt.plot(t, fun01, 'b-', linewidth=1)
plt.plot(t, fun02, 'g--', linewidth=1)
plt.plot(t, fun03, 'ko', linewidth=1, markersize=2)

# Alternatively:
# plt.plot(t, fun01,'b-', \
#          t, fun02,'g--',\
#          t, fun03,'k^'  )
# En esta sintaxis, no estoy seguro de cómo se pasan los parámetros
# de linewidth y markersize

# Plot main axii
plt.axhline(y=0, color='k', ls=':', linewidth=0.5)
plt.axvline(x=0, color='k', ls=':', linewidth=0.5)

plt.rc('font', size=10)
plt.title('Some more sine waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

n_xticks = math.ceil(Tfin / math.pi) + 1  # Calculate how many ticks we'll use
xticks = np.linspace(0, Tfin, n_xticks)

xticks_labels = ['0']

for tick_nr in range(n_xticks):
    xticks_labels.append(fr'${tick_nr} \pi$')  # f allows to have variables inside the string
                                                    # r indicates that the string is raw

# xticks_labels = [fr'${tick_nr} \pi$' for tick_nr in range(n_xticks)]

plt.xticks(xticks, xticks_labels)


# Guardar imagen en varios formatos
# save_path = os.path.dirname(os.path.abspath(__file__)) + '/img/'

# if not os.path.isdir(save_path):
#     os.mkdir(save_path)

# plt.savefig(save_path+'sine.png')
# plt.savefig(save_path+'sine_transparent.png',transparent=True)
# plt.savefig(save_path+'sine_vector.svg')
# plt.savefig(save_path+'sine_vector_transparente.svg',transparent=True)

# Mostrar la gráfica (se abrirá una ventana)
plt.show()
