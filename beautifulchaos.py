import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Function to plot an equilateral triangle
def plot_equilateral_triangle(ax, start_point, side_length):
    x_start, y_start = start_point
    x_middle = x_start + side_length / 2
    y_middle = y_start + (np.sqrt(3) / 2) * side_length
    x_end = x_start + side_length
    triangle_points = np.array([[x_start, y_start], [x_middle, y_middle], [x_end, y_start], [x_start, y_start]])
    ax.plot(triangle_points[:, 0], triangle_points[:, 1], '-o')
    return [(x_start, y_start), (x_middle, y_middle), (x_end, y_start)]

# Function to move towards a point
def move_towards_point(old_point, target_point):
    new_x = (old_point[0] + target_point[0]) / 2
    new_y = (old_point[1] + target_point[1]) / 2
    return new_x, new_y

# Function for the dice roll and move
def roll_dice_and_move(start_point, triangle_points):
    roll = random.randint(1, 6)
    if roll in [1, 2]:
        target_point = triangle_points[0]
    elif roll in [3, 4]:
        target_point = triangle_points[1]
    else:
        target_point = triangle_points[2]
    new_point = move_towards_point(start_point, target_point)
    return new_point

# Adjusted Animation function
def update(frame, dot_size):
    global current_point, dots, last_lines
    new_point = roll_dice_and_move(current_point, corner_points)
    
    # Create a new dot for each move
    dot, = ax.plot(new_point[0], new_point[1], 'bo', markersize=dot_size)
    dots.append(dot)

    # Create a new line for each move and update the last 5 lines
    if len(last_lines) >= 5:
        last_lines.pop(0)  # Remove the oldest line if there are 5 already

    new_line = ax.plot([current_point[0], new_point[0]], [current_point[1], new_point[1]], 'r-', lw=1, alpha=0.75)[0]
    last_lines.append(new_line)

    # Update line transparency
    for i, line in enumerate(last_lines):
        line.set_alpha((i + 1) / len(last_lines))  # Increase transparency for older lines

    current_point = new_point
    return dots + last_lines

# Setting up the plot
fig, ax = plt.subplots()
corner_points = plot_equilateral_triangle(ax, (0, 0), 2)
start_point = (1, 0.5)  # Starting point
current_point = start_point
dots = []  # List to store dot objects
last_lines = []  # List to store the last 5 line objects
dot_size = 2  # Dot size, can be adjusted

# Plot the starting point in red
ax.plot(start_point[0], start_point[1], 'ro', markersize=dot_size)

# Create and display the animation
anim = FuncAnimation(fig, lambda frame: update(frame, dot_size), frames=np.arange(0, 100), interval=25, blit=True)

plt.show()