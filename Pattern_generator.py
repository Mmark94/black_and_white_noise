from matplotlib import pyplot as plt
from matplotlib import colors
import random

# In this script there are functions to generate many patterns with white and black blocks

def make_matrix(x, y):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0]*y for _ in range(x)]

# This function allows you to generate a grid pattern where a block is in black if the block number divided by a divisor is equal to a remainder.
def simple_pattern_generator(grid_dimension: int, divisors: int, remainders: int):
    GRID = make_matrix(grid_dimension, grid_dimension)

    # Each block of the grid will have a number (counter)
    # This will loop for every block in the grid and if it follows the rules, it will colour it in black
    counter = 0
    for i in range(grid_dimension):
        for j in range(grid_dimension):
            if counter % divisors == remainders:
                GRID[i][j] = 1
            else:
                GRID[i][j] = 0
            counter += 1
    # print(GRID)

    # Plot the data
    # Here you can chose the colours to use in the image. Here there are a list of colours: ["white", "green", "black", "orange", "blue", "yellow", "red", "pink"]
    colours_grid = ["white", "black"]
    Cmap = colors.ListedColormap(colours_grid)

    # Show the image
    plt.imshow(GRID, cmap=Cmap)
    plt.savefig("patterns/grid_pattern_" + str(grid_dimension) + "_d_" + str(divisors) + "_r_" + str(remainders) + ".png", format="png")
    #plt.show()
    plt.close()
    return None

# This function is similar to the previous function, but it allows you to choose many divisors and remainders. It the block number satisfied one of the conditions (OR), it will colour it in black.
def complex_pattern_generator(grid_dimension: int, divisors: list, remainders: list):
    GRID = make_matrix(grid_dimension, grid_dimension)

    # Each block of the grid will have a number (counter)
    # This will loop for every block in the grid and if it follows the rules, it will colour it in black
    counter = 0
    for i in range(grid_dimension):
        for j in range(grid_dimension):
            LIST_conditions = []
            for element in range(len(divisors)):
                LIST_conditions.append(counter % divisors[element] == remainders[element])
            #print(LIST_conditions)
            #if all(LIST_conditions):   # all() is an AND statement
            if any(LIST_conditions):   # any() is an OR statement
                GRID[i][j] = 1
            else:
                GRID[i][j] = 0
            counter += 1
    # print(GRID)

    # Plot the data
    # Here you can chose the colours to use in the image. Here there are a list of colours: ["white", "green", "black", "orange", "blue", "yellow", "red", "pink"]
    colours_grid = ["white", "black"]
    Cmap = colors.ListedColormap(colours_grid)

    # Show or save the image
    plt.imshow(GRID, cmap=Cmap)
    plt.savefig("complex_patterns/grid_pattern_" + str(grid_dimension) + "_d_" + str(divisors) + "_r_" + str(remainders) + ".png", format="png")
    #plt.show()
    plt.close()
    return None

# This function will use the function "complex_pattern_generator" to generate pattern. It will choose the divisors and remainders at random from one list.
def random_pattern_generator(num_patterns: int, grid_dimension: int, divisors: list, remainders: list, number_conditions: int):
    for _ in range(num_patterns):
        div = random.choices(divisors, k=number_conditions)
        rem = random.choices(remainders, k=number_conditions)
        complex_pattern_generator(grid_dimension, div, rem)
    return None

# test the code
if __name__ == "__main__":

    # This loop allow to generate many simple patterns with only one divisor and one remainder
    """
    for d in range(3, 7, 2):
        for r in range(0, 2):
            print(d, r)
            simple_pattern_generator(20, d, r)
    """
    # Test the function complex_pattern_generator
    #complex_pattern_generator(100, [2, 5, 3, 5], [5, 1, 2, 3])

    # Test the function random_pattern_generator
    # Decide the divisors list
    Numbers = range(1, 31, 1)
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    # Decide the remainders list
    Reminders = range(0, 3, 1)
    number_conditions = 3   # Decide how many conditions you want to use to generate the patter

    num_patterns = 10   # How many pattern do you want to create
    grid_dimension = 25   # Decide the grid dimension

    random_pattern_generator(num_patterns=num_patterns, grid_dimension=grid_dimension, divisors=prime_numbers, remainders=Reminders, number_conditions=number_conditions)
