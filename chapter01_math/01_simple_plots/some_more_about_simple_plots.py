import math

import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path  # Used to make path handling easier


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

# Plot main axii (optional)
plt.axhline(y=0, color='k', ls=':', linewidth=0.5)
plt.axvline(x=0, color='k', ls=':', linewidth=0.5)

# Set plot attributes
plt.rc('font', size=10)
plt.title('Some more sine waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Let's be fancy, and show ticks as a function of pi
n_xticks = math.ceil(Tfin / math.pi) + 1  # Calculate how many ticks we'll use
xticks = np.linspace(0, Tfin, n_xticks)

xticks_labels = ['0']

for tick_nr in range(1, n_xticks):
    xticks_labels.append(fr'${tick_nr} \pi$')  # f allows to have variables inside the string, r indicates that the string is raw

plt.xticks(xticks, xticks_labels)

# Save the image
save_path = Path(__file__).parent / 'img'

if not save_path.is_dir():
    save_path.mkdir()  # Create the directory if it does not exist

plt.savefig(save_path / 'sine.png')
plt.savefig(save_path / 'sine_transparent.png', transparent=True)
plt.savefig(save_path / 'sine_vector.svg')
plt.savefig(save_path / 'sine_vector_transparent.svg', transparent=True)

plt.show()  # The .show() method should be invoked after .savefig()
