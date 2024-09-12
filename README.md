# Beautiful Chaos

This project implements the Sierpinski triangle using the chaos game method, as demonstrated in the Numberphile video: [How to create the Sierpinski triangle](https://www.youtube.com/watch?v=kbKtFN71Lfs&ab_channel=Numberphile)

## Description

The Sierpinski triangle is a fractal pattern that emerges from a simple iterative process. This implementation uses NumPy for efficient calculations and Matplotlib for animated visualization.

![Still image of the Sierpinski triangle animation](https://github.com/user-attachments/assets/910dbbd8-2b7b-4bf6-8ff8-31de1a1ff088)

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

To set up the project, create a virtual environment and install the required packages:


bash
python3 -m venv venv
source venv/bin/activate
pip install numpy matplotlib


## Usage

Run the script to generate and display the Sierpinski triangle:

bash
python beautifulchaos.py


## How it works

The script implements the chaos game method:
1. Start with three vertices of an equilateral triangle.
2. Choose a random point inside the triangle.
3. Repeatedly:
   - Select one of the three vertices at random.
   - Move halfway from the current point towards the selected vertex.
   - Plot the new point.

After many iterations, the Sierpinski triangle pattern emerges.
