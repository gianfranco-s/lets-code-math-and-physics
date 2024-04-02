import numpy as np
import matplotlib.pyplot as plt


time = np.arange(0, 10, 0.1)

# Alternatively, we could create an array from 0 to 10, with 10 elements
# time = np.linspace(0, 10, 10)

y = np.sin(time)

plt.plot(time, y)

plt.title('Sine wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.axhline(y=0, color='k',ls=':')
plt.axvline(x=0, color='k',ls=':')

# plt.show()  # <----- Uncomment this line to view the plot
