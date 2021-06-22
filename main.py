#       
#           .x88888x.            x*8888x.:*8888: -"888;
#          :8**888888X.  :>     X   48888X/`8888H/`8888H
#          f    `888888x./     X8x.  8888X  8888X  8888X;
#         '       `*88888~     X8888 X8888  88888  88888;
#          \.    .  `?)X.      '*888!X8888  X8888  X8888;
#           `~=-^   X88> ~       `?8 `8888  X888X  X888X
#                  X8888  ~      ~"  '888"  X888   X888
#                  488888           !888;  !888;  !888;
#          .xx.     88888X         888!   888!   888!
#         '*8888.   '88888>       88"    88"    88"
#           88888    '8888>        "~     "~     "~
#           `8888>    `888                           
#            "8888     8%           Johnny Madigan
#             `"888x:-"    https://johnnymadigan.github.io/
#       
# -----------------------Statement of Authorship------------------------#
#
#                       IFB104 Building IT Systems
#
# This is an individual assessment item.  By submitting this code I agree 
# that it represents my own work. I am aware of the University rule that a 
# student must not act in a manner which constitutes academic dishonesty as 
# stated and explained in QUT's Manual of Policies and Procedures, Section 
# C/5.3 "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#                      Student name: Johnny Madigan
#
# NB: Files submitted without a completed copy of this statement will not 
# be marked.  All files submitted will be subjected to software plagiarism 
# analysis using the MoSS system (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------Task Description--------------------------#
#
#                             TESSELLATION
#
# This assignment tests your skills at processing data stored in lists, 
# creating reusable code and following instructions to display a complex 
# visual image. The incomplete Python program below is missing a crucial 
# function, "tessellate". You are required to complete this function so 
# that when the program is run it fills a rectangular space with differently
# shaped tiles, using data stored in a list to determine which tiles to 
# place and where.
#
# ------------------------Imports & Constants-------------------------#

from turtle import *
from math import *
from random import *

import tiles
import broken_tiles

cell_size = 99
grid_width = 10  # Width in cells
grid_height = 7  # Height in cells
x_margin = cell_size * 2.75  # Pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2  # Pixels, the size of the margin below/above the grid

window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2

small_font = ('Arial', 18, 'normal')  # Font for the coords
big_font = ('Arial', 24, 'normal')  # Font for any other text

# Assertions for the canvas - do not change
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

# ----------Functions for Creating the Drawing Canvas----------------------#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour='#d3d3d3'): # Hex codes: light grey
    """
    Set up the canvas for the turtle drawing.

    :param bg_colour: background colour
    :param line_colour: grid line colour
    """

    # Set up the drawing canvas with enough space for the grid and legend padded around
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Reset
    penup()
    pencolor('black')
    width(1)
    home()

def release_drawing_canvas():
    """
    Ends the program by releasing the canvas to the OS.
    """
    tracer(False)
    done()

# -------------Test Data for Use During Code Development--------------#
#
# The hard-coded data sets in this section are provided to help you develop
# and test your code. You can use them as the argument to the "tesselate" 
# function while perfecting your solution. However, they will NOT be used to 
# assess your program. Your solution will be assessed using the "random_pattern" 
# function appearing below. Your program must work correctly for any data set 
# that can be generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying what cells the
# tile will fill and its condition (X = broken). The instructions are encoded like:
#
#                         [squares, condition]

# Small tile
fixed_pattern_0 = [['A1', 'O']]
fixed_pattern_1 = [['J7', 'X']]

# Wide tile
fixed_pattern_2 = [['A7', 'B7', 'O']]
fixed_pattern_3 = [['I1', 'J1', 'X']]

# Tall tile
fixed_pattern_4 = [['A1', 'A2', 'O']]
fixed_pattern_5 = [['J6', 'J7', 'X']]

# Big tile
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7', 'O']]
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2', 'X']]

# Small tiles
fixed_pattern_8 = [['E1', 'O'],
                   ['J4', 'O'],
                   ['C5', 'O'],
                   ['B1', 'O'],
                   ['I1', 'O']]
fixed_pattern_9 = [['C6', 'X'],
                   ['I4', 'X'],
                   ['D6', 'X'],
                   ['J5', 'X'],
                   ['F6', 'X'],
                   ['F7', 'X']]

# Wide tiles
fixed_pattern_10 = [['A4', 'B4', 'O'],
                    ['C1', 'D1', 'O'],
                    ['C7', 'D7', 'O'],
                    ['A7', 'B7', 'O'],
                    ['D4', 'E4', 'O']]
fixed_pattern_11 = [['D7', 'E7', 'X'],
                    ['G7', 'H7', 'X'],
                    ['H5', 'I5', 'X'],
                    ['B3', 'C3', 'X']]

# Tall tiles
fixed_pattern_12 = [['J2', 'J3', 'O'],
                    ['E5', 'E6', 'O'],
                    ['I1', 'I2', 'O'],
                    ['E1', 'E2', 'O'],
                    ['D3', 'D4', 'O']]
fixed_pattern_13 = [['H4', 'H5', 'X'],
                    ['F1', 'F2', 'X'],
                    ['E2', 'E3', 'X'],
                    ['C4', 'C5', 'X']]

# Big tiles
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6', 'O'],
                    ['I5', 'J5', 'I6', 'J6', 'O'],
                    ['C2', 'D2', 'C3', 'D3', 'O'],
                    ['H2', 'I2', 'H3', 'I3', 'O'],
                    ['A3', 'B3', 'A4', 'B4', 'O']]
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3', 'X'],
                    ['E5', 'F5', 'E6', 'F6', 'X'],
                    ['E3', 'F3', 'E4', 'F4', 'X'],
                    ['B3', 'C3', 'B4', 'C4', 'X']]

# Each of these patterns puts one instance of each type
# of tile in the grid.
fixed_pattern_16 = [['I5', 'O'],
                    ['E1', 'F1', 'E2', 'F2', 'O'],
                    ['J5', 'J6', 'O'],
                    ['G7', 'H7', 'O']]
fixed_pattern_17 = [['G7', 'H7', 'X'],
                    ['B7', 'X'],
                    ['A5', 'B5', 'A6', 'B6', 'X'],
                    ['D2', 'D3', 'X']]

# --------------Function for Assessing Your Solution-------------------#
#
# The following function creates a random data set specifying a
# tessellation to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "tessellate"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place tiles using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# tiles and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger tiles placed.  In the worst case, only one big
# tile will be placed in the grid (but this is very unlikely)!
#
# As well as the coordinates for each tile, an additional value which
# is either an 'O' or 'X' accompanies each one.  The purpose of this
# "mystery" value will be revealed in Part B of the assignment.

def random_pattern():
    """
    Generate random data set.
    """
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 tiles as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are all free
        if (not [column, row] in been_there) and \
                (not [column, row + 1] in been_there) and \
                (not [column + 1, row] in been_there) and \
                (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 tiles as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
                (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 2x1 tiles as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
                (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Fill all remaining spaces with 1x1 tiles
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the tile's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1),
                                'X' if randint(1, 100) <= mystery_probability else 'O'])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('\nRandomly generated tiles:\n')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern



# --------------------------Student Solution--------------------------#
# Majority of solution functions have been extracted, see all other Python files.

def legend():
    """
    Draws legends with visuals & accompying text describing it.
    """
    # GOTO TOP LEFT POSITION
    goto(-(grid_width * cell_size) // 2 - 250, 250)
    setheading(0)

    # Draws Mickey image & adds text
    tiles.draw_large_tile()
    goto(-(grid_width * cell_size) // 2 - 65, 10)
    write('Mickey Mouse', align='right', font="Verdana 15")

    # GOTO BOTTOM LEFT POSITION
    goto(-(grid_width * cell_size) // 2 - 200, -50)
    setheading(0)

    # Draws Minnie image & adds text
    tiles.draw_small_tile()
    goto(-(grid_width * cell_size) // 2 - 65, -190)
    write('Minnie Mouse', align='right', font="Verdana 15")

    # GOTO TOP RIGHT POSITION
    goto((grid_width * cell_size) // 2 + 90, 250)
    setheading(0)

    # Draws Donald image & adds text
    tiles.draw_tall_tile()
    goto((grid_width * cell_size) // 2 + 220, 10)
    write('Donald Duck', align='right', font="Verdana 15")

    # GOTO BOTTOM RIGHT POSITION
    goto((grid_width * cell_size) // 2 + 40, -50)
    setheading(0)

    # Draws Goofy image & adds text
    tiles.draw_wide_tile()
    goto((grid_width * cell_size) // 2 + 180, -190)
    write('Goofy', align='right', font="Verdana 15")



def tessellate(pattern):
    """
    Fills the grid with tiles as per the provided dataset.
    """

    # For each tile's instructions, grab the first cell coordinates to begin drawing the tile
    for commands in pattern:
        grid_square = commands[0]

        # Converts X coord
        if grid_square[0] == 'A': x = ord('A') - 565
        elif grid_square[0] == 'B': x = ord('B') - 466
        elif grid_square[0] == 'C': x = ord('C') - 367
        elif grid_square[0] == 'D': x = ord('D') - 268
        elif grid_square[0] == 'E': x = ord('E') - 169
        elif grid_square[0] == 'F': x = ord('F') - 70
        elif grid_square[0] == 'G': x = ord('G') + 29
        elif grid_square[0] == 'H': x = ord('H') + 128
        elif grid_square[0] == 'I': x = ord('I') + 227
        elif grid_square[0] == 'J': x = ord('J') + 326

        # Converts Y coord
        if grid_square[1] == '1': y = -250
        elif grid_square[1] == '2': y = -150
        elif grid_square[1] == '3': y = -50
        elif grid_square[1] == '4': y = 50
        elif grid_square[1] == '5': y = 150
        elif grid_square[1] == '6': y = 250
        elif grid_square[1] == '7': y = 350

        # Send turtle to coords
        goto(x, y)

        # Joins all strings in a command to be able to count any repeated numbers (representing rows).
        # This is to differentiate between long & wide tiles as wide tiles need to fill multiple rows unlike tall tiles.
        string = " ".join(commands)
        count_1s = string.count('1')
        count_2s = string.count('2')
        count_3s = string.count('3')
        count_4s = string.count('4')
        count_5s = string.count('5')
        count_6s = string.count('6')
        count_7s = string.count('7')

        # Determines which tile is needed by counting the amount of grid spaces that need filling in a command.
        # Additionally if a command ends with an 'X' the tile will be broken.

        # Small tiles
        if len(commands) == 2:
            tiles.draw_small_tile()
            if commands[-1] == 'X': broken_tiles.break_small_tile()

        # Wide OR tall tiles
        elif len(commands) == 3:
            if count_1s == 2 or \
                count_2s == 2 or \
                count_3s == 2 or \
                count_4s == 2 or \
                count_5s == 2 or \
                count_6s == 2 or \
                count_7s == 2:
                tiles.draw_wide_tile()
                if commands[-1] == 'X': broken_tiles.break_wide_tile()

            else:
                tiles.draw_tall_tile()
                if commands[-1] == 'X': broken_tiles.break_tall_tile()

        # Large tiles
        elif len(commands) == 5:
            tiles.draw_large_tile()
            if commands[-1] == 'X': broken_tiles.break_large_tile()



# --------------------------------Main---------------------------------#

title("Disney Icons") # Window title

create_drawing_canvas('#F5F5F5') # Hex codes: white smoke

speed(0) # Drawing speed increases from 1-10 (exception: 0 = fastest)

tracer(False) # True = show the turtle drawing at the speed above

legend() # Draw legend

tessellate(random_pattern())  # Fills cells with Disney characters

release_drawing_canvas() # Exit gracefully
