import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# ... [previous functions remain the same] ...

# Adjusted Animation function
def update(frame):
    global current_point
    new_point = roll_dice_and_move(current_point, corner_points)
    
    # Update line and point data
    line.set_data([current_point[0], new_point[0]], [current_point[1], new_point[1]])
    points.set_data([new_point[0]], [new_point[1]])  # Pass data as list or tuple
    
    current_point = new_point
    return line, points

# Setting up the plot
fig, ax = plt.subplots()
corner_points = plot_equilateral_triangle(ax, (0, 0), 2)
current_point = (1, 0.5)  # Starting point
line, = ax.plot([], [], 'r-', lw=1)
points, = ax.plot([], [], 'bo')

# Create and display the animation
anim = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=250, blit=True)

plt.show()
