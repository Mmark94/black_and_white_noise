from matplotlib import pyplot as plt
from matplotlib import colors

# In this script, you can save or draw your own grid by writing 1 and 0 !

smile = [
    [0,0,0,1,1,1,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,1,0],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [0,1,0,0,1,1,0,0,1,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,0,1,1,1,1,0,0,0]
]
# Plot the data
# Here you can chose the colours to use in the image
colours_grid = ["white", "black"]
Cmap = colors.ListedColormap(colours_grid)

# Show the image
plt.imshow(smile, cmap=Cmap)
plt.show()


# This is a different draw as an example.
GRID = [
    [0,1,1,1,1,1,1,1,1,0],
    [1,1,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,1,1],
    [0,1,1,1,1,1,1,1,1,0]
]

# Plot the data
# Here you can chose the colours to use in the image
colours_grid = ["white", "black"]
Cmap = colors.ListedColormap(colours_grid)

# Show the image
plt.imshow(GRID, cmap=Cmap)
plt.show()