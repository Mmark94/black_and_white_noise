from matplotlib import pyplot as plt
from matplotlib import colors
import random

# This is a script to generate random images of black and white noise. This is also called "white noise".

def make_matrix(x, y):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0]*y for _ in range(x)]

# This function generates a random grid with a gradient of probability
def random_gradient(grid_dimension: int, white: int, black: int, gradient=1):
    # Here you can chose how many colours you want to have in the grid. Each number equal one colour.
    numbers_grid = [1, 2]

    white_0, black_0 = white, black     # this will store the initial values of white and black
    # This loop generates as many random numbers as the grid size you set. And it stores the results in a matrix.
    GRID = make_matrix(grid_dimension, grid_dimension)
    for i in range(grid_dimension):
        for j in range(grid_dimension):
            GRID[i][j] = random.choices(numbers_grid, [white, black], k=1)
            white += gradient

    # Plot the data
    # Here there are a list of colours: ["white", "green", "black", "orange", "blue", "yellow", "red", "pink"]
    colours_grid = ["white", "black"]
    Cmap = colors.ListedColormap(colours_grid)

    # Show the image
    plt.imshow(GRID, cmap=Cmap)
    plt.savefig("pattern_from_random/grid_" + str(grid_dimension) + "_gradient" + str(gradient) + "_w" + str(white_0) + "_b" + str(black_0) + ".png", format="png")
    plt.show()
    plt.close()
    return None

# This function generates a random grid with different probabilities of each colours.
# You can set how much connectivity there is in the black and white noise.
# For instance, high connectivity means that the probability of a square being of a colours, it is higher if the previous square is the same colour.
# Low connectivity means that the probability of a square being of a colours, it is higher if the previous square is a different colour.
def random_connectivity(grid_dimension: int, white: int, black: int, connection=1):
    # Here you can chose how many colours you want to have in the grid. Each number equal one colour.
    numbers_grid = [1, 2]

    # This loop generates as many random numbers as the grid size you set. And it stores the results in a matrix.
    GRID = make_matrix(grid_dimension, grid_dimension)
    previous = 0
    counter = 0
    for i in range(grid_dimension):
        for j in range(grid_dimension):
            if previous == connection:  # previous == 1 or 2. 1 For very connected grids (positive feedback), 2 for very not connected (negative feedback). You can also set it to connection if you want to have it at random
                GRID[i][j] = random.choices(numbers_grid, [white, 1], k=1)
            else:
                GRID[i][j] = random.choices(numbers_grid, [1, black], k=1)
            counter += 1
            previous = GRID[i][j][0]
            # If you want, you can change the connectivity through the grid.
            #connection = random.choices(numbers_grid, [2, 1], k=1)[0]

    # Plot the data
    # Here there are a list of colours: ["white", "green", "black", "orange", "blue", "yellow", "red", "pink"]
    colours_grid = ["white", "black"]
    Cmap = colors.ListedColormap(colours_grid)

    # Show the image
    plt.imshow(GRID, cmap=Cmap)
    plt.savefig("pattern_from_random/grid_" + str(grid_dimension) + "_c" + str(connection) + "_w" + str(white) + "_b" + str(black) + ".png", format="png")
    #plt.show()
    plt.close()
    return None


# test the code
if __name__ == "__main__":

    #random_connectivity(grid_dimension=500, white=10, black=10, connection=1)

    W = range(1, 22, 3)
    B = range(1, 22, 3)
    """
    for w in W:
        for b in B:
            random_connectivity(grid_dimension=200, white=w, black=b, connection=1)
    """

    random_gradient(grid_dimension=500, white=1, black=25, gradient=0.0003)