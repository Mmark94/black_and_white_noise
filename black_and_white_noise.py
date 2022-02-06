from matplotlib import pyplot as plt
from matplotlib import colors
import random

# This is a script to generate random images of black and white noise. This is also called "white noise".

# Generate the data
# Here you can chose the dimension of the grid and the image
grid_dimension = 100

# Here you can chose how many colours you want to have in the grid. Each number equal one colour.
number_of_colours = 2
numbers_grid = range(1, number_of_colours + 1)

# Here you can set a probability for each colour. For example you can set the black dots to be two times more frequent than white ones.
numbers_probability = [1, 1]
numbers_probability = [1 for _ in range(number_of_colours)]
# If you want to chose at random the probability of each colour
#numbers_probability = random.choices(range(1, 11), k=number_of_colours)    # sampling with replacement

# This loop generates as many random numbers as the grid size you set. And it stores the results in a list.
GRID = []
for _ in range(grid_dimension):
    square_colours = random.choices(numbers_grid, numbers_probability, k=grid_dimension)
    GRID.append(square_colours)
#print(GRID)

# Plot the data
# Here you can chose the colours to use in the image. Here there is a list of colours you can use: https://matplotlib.org/stable/gallery/color/named_colors.html
# Here there are a list of colours:
possible_colours = ["white", "black", "green", "orange", "blue", "yellow", "red", "pink"]
colours_grid = ["white", "black"]
colours_grid = possible_colours[:number_of_colours]
# If you want to chose at random which colours to use
#colours_grid = random.choices(possible_colours, k=number_of_colours)    # sampling with replacement
colours_grid = random.sample(possible_colours, k=number_of_colours)     # sampling without replacement
Cmap = colors.ListedColormap(colours_grid)

# Info about the image (e.g. colours and probability)
info = ""
for i in range(number_of_colours):
    info = info + "_" + str(numbers_probability[i]) + colours_grid[i]

# Show the image
plt.figure(figsize=(20, 20))
plt.imshow(GRID, cmap=Cmap)
#plt.axis('off')
plt.xticks(color='w')
plt.yticks(color='w')
plt.savefig("media/grid_" + str(grid_dimension) + info + ".png", format="png", dpi=300)
plt.show()
plt.close()

# This is a different way to plot the image. Each square will have a black frame. However, it cannot plot more than a 100x100 grid
#plt.figure(figsize=(grid_dimension, grid_dimension))
#plt.pcolor(GRID[::-1], cmap=Cmap, edgecolors='k', linewidths=3)
#plt.show()