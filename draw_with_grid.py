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
plt.figure(figsize=(20, 20))
plt.imshow(smile, cmap=Cmap)
#plt.axis('off')
plt.xticks(color='w')
plt.yticks(color='w')
plt.savefig("media/smile.png", format="png", dpi=300)
plt.show()
plt.close()


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
plt.figure(figsize=(20, 20))
plt.imshow(GRID, cmap=Cmap)
#plt.axis('off')
plt.xticks(color='w')
plt.yticks(color='w')
plt.savefig("media/flower.png", format="png", dpi=300)
plt.show()
plt.close()
