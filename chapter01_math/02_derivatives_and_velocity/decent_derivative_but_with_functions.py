import os

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

""" Hopefully, you've seen that `plot_a_decent_derivative.py` has much duplicated code.
To reduce duplication, we'll create a function that contains all of our plotting code.
After that, we'll call it from within a for loop to plot all of our data
"""

# Generate array from 0 to 4, with step of 0.1
tstart = 0
tend = 4
step = 0.1
time = np.arange(tstart, tend, step)

# Define a function for the car's position at any time
def car_position_eq(time):
    return time ** 3

car_positions = car_position_eq(time)

# We'll evaluate the 'velocity line' at instant ta:
ta = 2.0

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(1, 3)

# Define the values for dt
dt_values = (1.0, 0.5, 0.01)

def plot_tangential_line(dt, plot_nr):
    tb = ta + dt

    xa = car_position_eq(ta)
    xb = car_position_eq(tb)

    v = (xb - xa) / (tb - ta)  # Which is the same as m = (xb - xa) / dt, from the awful plot

    v_line = v * (time - ta) + xa

    # Generate "plt" object using plot() method, and add title.
    axis[plot_nr].plot(time, car_positions, 'b-', linewidth=1)
    axis[plot_nr].plot(time, v_line, 'r--', linewidth=1)
    axis[plot_nr].plot(ta, xa, 'rs', fillstyle='none', markersize=12)
    axis[plot_nr].plot(tb, xb, 'ro', fillstyle='none', markersize=10)

    # Set limits for axis. If not using "plt.xlim(...)" notation, use axis[].set_...
    axis[plot_nr].set_xlim(0, max(time))
    axis[plot_nr].set_ylim(0, max(car_positions))
    axis[plot_nr].set_title(f'{dt=}')

for idx, dt in enumerate(dt_values):
    plot_tangential_line(dt, idx)

# Save the image
save_path = Path(__file__).parent / 'img'

if not save_path.is_dir():
    save_path.mkdir()  # Create the directory if it does not exist

plt.savefig(save_path / 'fig_derivative_new.png')
