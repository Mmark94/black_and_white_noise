from matplotlib import pyplot as plt
from matplotlib import colors
import random

# This is a script to generate random images of black and white noise. This is also called "white noise".

# Generate the data
# Here you can chose the dimension of the grid and the image
grid_dimension = 100

# Here you can chose how many colours you want to have in the grid. Each number equal one colour.
numbers_grid = [1, 2]

# Here you can set a probability for each colour. For example you can set the black dots to be two times more frequent than white ones.
numbers_probability = [1, 1]

# This loop generates as many random numbers as the grid size you set. And it stores the results in a list.
GRID = []
for _ in range(grid_dimension):
    square_colours = random.choices(numbers_grid, numbers_probability, k=grid_dimension)
    GRID.append(square_colours)
#print(GRID)

# Plot the data
# Here you can chose the colours to use in the image. Here there is a list of colours you can use: https://matplotlib.org/stable/gallery/color/named_colors.html
# Here there are a list of colours: ["white", "green", "black", "orange", "blue", "yellow", "red", "pink"]
colours_grid = ["white", "black"]
Cmap = colors.ListedColormap(colours_grid)

# Show the image
plt.imshow(GRID, cmap=Cmap)
#plt.savefig("media/grid_" + str(grid_dimension) + ".png", format="png")
plt.show()

# This is a different way to plot the image. Each square will have a black frame. However, it cannot plot more than a 100x100 grid
#plt.figure(figsize=(grid_dimension, grid_dimension))
#plt.pcolor(GRID[::-1], cmap=Cmap, edgecolors='k', linewidths=3)
#plt.show()