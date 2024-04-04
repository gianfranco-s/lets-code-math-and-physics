import os

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

""" We'll plot three 'velocity lines': they are not strictly velocities, but should illustrate why the velocity
is thought of as the tangent of a curve.
Values:
ta = 2.0

a) dt = 1.0 (we already covered this before, but we'll repeat it)
b) dt = 0.5
c) dt = 0.1
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

# -------------------------- Velocity with dt = 1.0 -------------------------
dt = 1.0
tb = ta + dt

xa = car_position_eq(ta)
xb = car_position_eq(tb)

v = (xb - xa) / (tb - ta)  # Which is the same as m = (xb - xa) / dt, from the awful plot

v_line = v * (time - ta) + xa

# Generate "plt" object using plot() method, and add title.
plot1 = axis[0]
plot1.plot(time, car_positions, 'b-', linewidth=1)
plot1.plot(time, v_line, 'r--', linewidth=1)
plot1.plot(ta, xa, 'rs', fillstyle='none', markersize=12)
plot1.plot(tb, xb, 'ro', fillstyle='none', markersize=10)

# Set limits for axis. If not using "plt.xlim(...)" notation, use axis[].set_...
plot1.set_xlim(0, max(time))
plot1.set_ylim(0, max(car_positions))
plot1.set_title(f'{dt=}')

# -------------------------- Velocity with dt = 0.5 -------------------------
dt = 0.5
tb = ta + dt

xa = car_position_eq(ta)
xb = car_position_eq(tb)

v = (xb - xa) / (tb - ta)
v_line = v * (time - ta) + xa

# Generate "plt" object using plot() method, and add title.
plot2 = axis[1]
plot2.plot(time, car_positions, 'b-', linewidth=1)
plot2.plot(time, v_line,'r--', linewidth=1)
plot2.plot(ta, xa, 'rs', fillstyle='none', markersize=12)
plot2.plot(tb, xb, 'ro', fillstyle='none', markersize=10)

# Set limits for axis. If not using "plt.xlim(...)" notation, use axis[].set_...
plot2.set_xlim(0, max(time))
plot2.set_ylim(0, max(car_positions))
plot2.set_title(f'{dt=}')

# -------------------------- Velocity with dt = 0.01 -------------------------
dt = 0.01
tb = ta + dt

xa = car_position_eq(ta)
xb = car_position_eq(tb)

v = (xb - xa) / (tb - ta)
v_line = v * (time - ta) + xa

# Generate "plt" object using plot() method, and add title.
plot3 = axis[2]
plot3.plot(time, car_positions, 'b-', linewidth=1)
plot3.plot(time, v_line, 'r--', linewidth=1)
plot3.plot(ta, xa, 'rs', fillstyle='none', markersize=12)
plot3.plot(tb, xb, 'ro', fillstyle='none', markersize=10)

# Set limits for axis. If not using "plt.xlim(...)" notation, use axis[].set_...
plot3.set_xlim(0, max(time))
plot3.set_ylim(0, max(car_positions))
plot3.set_title(f'{dt=}')

# Save the image
save_path = Path(__file__).parent / 'img'

if not save_path.is_dir():
    save_path.mkdir()  # Create the directory if it does not exist

plt.savefig(save_path / 'fig_derivative.png')

""" When using this method of defining the plot subplot first,
and then filling it with data, the method plt.show() cannot be used. The image will be saved in fig_derivative.png
"""
