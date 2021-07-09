from matplotlib import pyplot as plt
from matplotlib import colors

# In this script I create a chess board pattern

def make_matrix(x, y):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0]*y for _ in range(x)]

dimension = 8
chess_board = make_matrix(dimension, dimension)

# Here you can chose the colours to use in the image.
# Here there are a list of colours: ["white", "green", "black", "orange", "blue", "yellow", "red", "pink"]
colours_grid = ["white", "black"]
colours = range(len(colours_grid))

# Create the chess board pattern
counter = 0
for i in range(dimension):
    for j in range(dimension):
        chess_board[i][j] = counter
        counter += 1
        if counter == len(colours):
            counter = 0
    counter += 1
    if counter == len(colours):
        counter = 0
#print(chess_board)

# Plot the data
# Set the colours
Cmap = colors.ListedColormap(colours_grid)

# Show the image
plt.imshow(chess_board, cmap=Cmap)
plt.show()