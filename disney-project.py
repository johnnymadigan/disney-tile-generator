# -----Statement of Authorship----------------------------------------#
#
# IFB104 Building IT Systems

#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student name: Johnny Madigan
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Task Description-----------------------------------------------#
#
#  TESSELLATION
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "tessellate".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped tiles, using data
#  stored in a list to determine which tiles to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
# --------------------------------------------------------------------#


# -----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

cell_size = 100  # pixels (default is 100)
grid_width = 10  # squares (default is 10)
grid_height = 7  # squares (default is 7)
x_margin = cell_size * 2.75  # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2  # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', 18, 'normal')  # font for the coords
big_font = ('Arial', 24, 'normal')  # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'


#
# --------------------------------------------------------------------#


# -----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour='#d3d3d3',
                          line_colour='#708090',
                          draw_grid=True, mark_legend=True):
    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0)  # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)

        # Draw the vertical grid lines
        setheading(90)  # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27  # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align='center', font=small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10  # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align='right', font=small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    # Optionally mark the spaces for drawing the legend
    if mark_legend:
        # Left side
        goto(-(grid_width * cell_size) // 2 - 75, -25)
        write('Put your\nlegend here', align='right', font=big_font)
        # Right side
        goto((grid_width * cell_size) // 2 + 75, -25)
        write('Put your\nlegend here', align='left', font=big_font)

        # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    tracer(True)  # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()


#
# --------------------------------------------------------------------#


# -----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "tesselate" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying
# where to place a particular tile.  The general form of each
# instruction is
#
#     [squares, mystery_value]
#
# where there may be one, two or four squares in the grid listed
# at the beginning.  This tells us which grid squares must be
# filled by this particular tile.  This information also tells
# us which shape of tile to produce.  A "big" tile will occupy
# four grid squares, a "small" tile will occupy one square, a
# "wide" tile will occupy two squares in the same row, and a
# "tall" tile will occupy two squares in the same column.  The
# purpose of the "mystery value" will be revealed in Part B of
# the assignment.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single tile in the grid, in one of the corners.

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

# Each of these patterns puts multiple copies of the same
# type of tile in the grid.

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


# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with tiles.

#
# --------------------------------------------------------------------#


# -----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
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
#
def random_pattern(print_pattern=True):
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
    print('Draw the tiles in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "tessellate" function.


# ------------------------------------------
#           GLOBAL CONSTANTS          
# ------------------------------------------
#
# Length of two grid spaces
double = 200

# Length of one grid space
single = 100

# Right angle
angle = 90


# ------------------------------------------
#           REUSABLE OVAL SHAPE          
# ------------------------------------------
# OVAL function
# Draws ovals using a radius & a value that stretches the oval's length
# Used to create better drawings
#
def draw_oval(radius, stretch=2):
    right(angle // 2)

    for loop in range(2):
        circle(radius, 90)
        circle(radius / stretch, 90)


# ------------------------------------------
#           REUSABLE STAR SHAPE          
# ------------------------------------------
# STAR function
# Draws stars using a colour & a length value to change its size
# Used to create better drawings
#
def draw_star(colour, length):
    turn_left = angle - 18
    turn_right = angle + 54

    setheading(288)
    color(colour)
    fillcolor(colour)
    pendown()
    begin_fill()

    for points in range(5):
        forward(length)
        left(turn_left)
        forward(length)
        right(turn_right)
    end_fill()
    penup()


# ------------------------------------------
#               DISNEY ICONS          
# ------------------------------------------
# MICKEY MOUSE function
# Draws Mickey starting from the top left corner of a tile
# (do not change code)
#
def draw_mickey():
    # Background
    setheading(0)
    forward(single)
    right(angle)
    forward(15)
    draw_star('#990000', 70) # crimson
    setheading(angle)
    forward(15)
    setheading(180)
    forward(single)

    # Head
    setheading(0)
    forward(single)
    right(angle)
    forward(single + 20)
    dot(102, '#000000') # black
    forward(33)
    setheading(180)
    forward(35)

    # Face
    fillcolor('#FFFFFF') # white
    setheading(0)
    begin_fill()
    draw_oval(50)
    end_fill()
    forward(50)
    setheading(angle)
    forward(65)
    setheading(105)
    begin_fill()
    draw_oval(30)
    end_fill()
    setheading(0)
    forward(20)
    right(angle)
    forward(5)
    setheading(75)
    begin_fill()
    draw_oval(30)
    end_fill()

    # Eyes
    fillcolor('#000000') # black
    setheading(180)
    forward(7)
    setheading(90)
    begin_fill()
    draw_oval(15, 5)
    end_fill()
    setheading(180)
    forward(17)
    setheading(90)
    begin_fill()
    draw_oval(15, 5)
    end_fill()

    # Nose
    setheading(180)
    forward(2)
    setheading(270)
    forward(11)
    setheading(0)
    begin_fill()
    draw_oval(10)
    end_fill()

    # Chin
    setheading(235)
    forward(5)
    setheading(180)
    forward(20)
    setheading(270)
    fillcolor('#FFFFFF') # white
    begin_fill()
    circle(30, 180)
    end_fill()

    # Mouth
    setheading(180)
    forward(60)
    left(angle)
    forward(3)
    color('#000000') # black
    setheading(320)
    pendown()
    width(3)
    circle(45, 90)
    penup()
    setheading(180)
    forward(43)
    left(angle)
    forward(17)
    setheading(265)
    pendown()
    width(3)
    fillcolor('#800000') # maroon
    begin_fill()
    circle(10, 195)
    end_fill()
    penup()
    width(1)

    # Pupils
    setheading(angle)
    forward(35)
    setheading(0)
    forward(2)
    dot(7, '#FFFFFF') # white
    setheading(180)
    forward(17)
    dot(7, '#FFFFFF') # white

    # Ears
    setheading(180)
    forward(57)
    right(angle)
    forward(25)
    setheading(45)
    fillcolor('#000000') # black
    begin_fill()
    draw_oval(40)
    end_fill()
    setheading(0)
    forward(140)
    left(angle)
    forward(20)
    setheading(135)
    begin_fill()
    draw_oval(40)
    end_fill()

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# MINNIE MOUSE function
# Draws Minnie starting from the top left corner of a tile
# (do not change code)
#
def draw_minnie():
    # Background
    setheading(0)
    forward(single // 2)
    right(angle)
    forward(7)
    draw_star('plum', 35)
    setheading(angle)
    forward(7)
    setheading(180)
    forward(single // 2)

    # Head
    setheading(0)
    forward(single // 2)
    right(angle)
    forward(60)
    dot(55, '#000000') # black

    # Ears
    setheading(180)
    forward(30)
    right(angle)
    forward(20)
    dot(30, '#000000') # black
    forward(10)
    right(angle)
    forward(30)
    dot(30, '#000000') # black

    # Face
    setheading(0)
    forward(15)
    setheading(270)
    forward(40)
    fillcolor('#FFFFFF') # white
    setheading(170)
    begin_fill()
    draw_oval(20)
    end_fill()
    setheading(180)
    forward(0)
    setheading(270)
    forward(10)
    setheading(30)
    begin_fill()
    draw_oval(20, 5)
    end_fill()
    setheading(angle)
    forward(8)
    setheading(200)
    begin_fill()
    draw_oval(15)
    end_fill()
    setheading(100)
    begin_fill()
    draw_oval(20, 5)
    end_fill()
    setheading(0)
    forward(10)
    left(angle)
    forward(3)
    setheading(100)
    begin_fill()
    draw_oval(18, 5)
    end_fill()

    # Nose
    setheading(angle)
    forward(9)
    setheading(0)
    forward(12)
    pendown()
    width(2)
    setheading(175)
    circle(30, 30)
    penup()
    setheading(0)
    forward(17)
    setheading(270)
    forward(3)
    fillcolor('#000000') # black
    setheading(65)
    begin_fill()
    draw_oval(7)
    end_fill()

    # Mouth
    setheading(180)
    forward(43)
    setheading(270)
    forward(6)
    pendown()
    color('#000000') # black
    setheading(320)
    circle(35, 60)
    penup()
    setheading(180)
    forward(29)
    setheading(angle)
    forward(4)
    pendown()
    fillcolor('#800000')
    begin_fill()
    setheading(240)
    circle(9, 195)
    end_fill()
    penup()

    # Eyes
    setheading(angle)
    forward(17)
    setheading(180)
    forward(4)
    fillcolor('#000000') # black
    setheading(angle)
    begin_fill()
    draw_oval(8, 5)
    end_fill()
    setheading(0)
    forward(11)
    setheading(angle)
    begin_fill()
    draw_oval(8, 5)
    end_fill()

    # Bowtie
    setheading(180)
    forward(33)
    setheading(angle)
    forward(25)
    fillcolor('deep pink')
    begin_fill()
    setheading(100)
    draw_oval(7)
    end_fill()
    setheading(180)
    forward(8)
    setheading(angle)
    forward(10)
    fillcolor('hot pink')
    begin_fill()
    setheading(170)
    draw_oval(12)
    end_fill()
    setheading(180)
    forward(1)
    setheading(270)
    forward(5)
    begin_fill()
    setheading(210)
    draw_oval(12)
    end_fill()
    setheading(0)
    forward(10)
    setheading(30)
    begin_fill()
    draw_oval(12)
    end_fill()
    setheading(270)
    forward(2)
    setheading(350)
    begin_fill()
    draw_oval(12)
    end_fill()

    # Polka dots
    dot(5, '#FFFFFF') # white
    setheading(0)
    forward(10)
    right(angle)
    forward(2)
    dot(5, '#FFFFFF') # white
    setheading(angle)
    forward(13)
    setheading(180)
    forward(3)
    dot(5, '#FFFFFF') # white
    forward(28)
    left(angle)
    forward(2)
    dot(5, '#FFFFFF') # white
    forward(10)
    setheading(0)
    forward(5)
    dot(5, '#FFFFFF') # white
    setheading(180)
    forward(5)
    left(angle)
    forward(7)
    dot(5, '#FFFFFF') # white

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# DONALD DUCK function
# Draws Donald starting from the top left corner of a tile
# (do not change code)
#
def draw_donald():
    # Background
    setheading(0)
    forward(single // 2)
    right(angle)
    forward(single // 2)
    draw_star('lightskyblue', 35)
    setheading(angle)
    forward(single // 2)
    setheading(180)
    forward(single // 2)

    # Hat
    setheading(0)
    forward(single // 2)
    forward(5)
    right(angle)
    forward(single // 2)
    setheading(120)
    fillcolor('blue')
    begin_fill()
    draw_oval(30)
    end_fill()
    setheading(0)
    forward(15)
    left(angle)
    forward(8)
    setheading(160)
    fillcolor('blue')
    begin_fill()
    draw_oval(25)
    end_fill()
    setheading(0)
    forward(15)
    right(angle)
    forward(5)
    setheading(160)
    fillcolor('blue')
    begin_fill()
    draw_oval(20)
    end_fill()
    setheading(180)
    forward(32.5)
    left(angle)
    forward(10)
    dot(25, '#000000') # black
    right(angle)
    forward(12.5)
    pendown()
    color('#000000') # black
    left(angle)
    fillcolor('#000000') # black
    begin_fill()
    forward(15)
    left(angle)
    forward(25)
    left(angle)
    forward(12.5)
    end_fill()
    penup()

    # Head
    left(angle)
    forward(12.5)
    left(angle)
    forward(40)
    dot(70, '#FFFFFF') # white
    setheading(180)
    forward(6)
    fillcolor('#FFFFFF') # white
    setheading(angle)
    begin_fill()
    draw_oval(25)
    end_fill()
    setheading(0)
    forward(30)
    setheading(angle)
    begin_fill()
    draw_oval(25)
    end_fill()

    # Eyes
    setheading(180)
    forward(5)
    setheading(270)
    forward(5)
    fillcolor('#d3d3d3')
    setheading(angle)
    begin_fill()
    draw_oval(25, 6)
    end_fill()
    setheading(180)
    forward(30)
    setheading(angle)
    begin_fill()
    draw_oval(25, 6)
    end_fill()

    # Pupils
    fillcolor('#000000') # black
    setheading(angle)
    begin_fill()
    draw_oval(11, 5)
    end_fill()
    setheading(0)
    forward(25)
    setheading(angle)
    begin_fill()
    draw_oval(11, 5)
    end_fill()

    # Mouth
    setheading(180)
    forward(44)
    left(angle)
    forward(0)
    fillcolor('#FFA500')
    setheading(270)
    begin_fill()
    circle(30, 180)
    end_fill()
    setheading(180)
    forward(30)
    dot(20, '#FFA500')
    setheading(180)
    forward(25)
    width(5)
    setheading(0)
    forward(52)
    color('#FFA500')
    fillcolor('#800000')
    begin_fill()
    pendown()
    setheading(250)
    forward(40)
    setheading(210)
    forward(5)
    setheading(180)
    forward(20)
    right(40)
    forward(5)
    setheading(110)
    forward(40)
    end_fill()
    fillcolor('#FFA500')
    begin_fill()
    setheading(320)
    circle(40, 82)
    setheading(180)
    forward(7)
    forward(40)
    end_fill()
    penup()
    setheading(0)
    forward(35)
    right(angle)
    forward(11)
    color('dark orange')
    width(8)
    pendown()
    setheading(150)
    circle(30, 55)
    penup()
    color('#000000') # black

    # Bowtie
    setheading(0)
    forward(11)
    right(angle)
    forward(single // 2)
    fillcolor('#FF0000')
    begin_fill()
    draw_oval(10)
    end_fill()
    setheading(180)
    forward(2)
    left(angle)
    forward(2)
    setheading(160)
    pendown()
    width(3)
    color('dark red')
    fillcolor('#FF0000')
    begin_fill()
    forward(25)
    setheading(310)
    forward(15)
    setheading(230)
    forward(15)
    setheading(20)
    forward(25)
    end_fill()
    setheading(270)
    circle(6, 180)
    begin_fill()
    setheading(340)
    forward(25)
    setheading(130)
    forward(15)
    setheading(50)
    forward(15)
    setheading(200)
    forward(25)
    setheading(angle)
    circle(6, 180)
    end_fill()

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# GOOFY function
# Draws Goofy starting from the top left corner of a tile
# (do not change code)
#
def draw_goofy():
    # Background
    setheading(0)
    forward(single)
    right(angle)
    forward(5)
    draw_star('darkorange', 35)
    setheading(angle)
    forward(5)
    setheading(180)
    forward(single)

    # Hat
    setheading(0)
    forward(75)
    right(angle)
    forward(35)
    setheading(150)
    color('#000000') # black
    pendown()
    width(2)
    fillcolor('yellow green')
    begin_fill()
    forward(15)
    setheading(60)
    circle(5, 180)
    setheading(160)
    forward(10)
    setheading(70)
    circle(5, 230)
    setheading(240)
    forward(5)
    setheading(170)
    circle(5, 230)
    setheading(340)
    forward(10)
    setheading(250)
    circle(5, 180)
    setheading(320)
    forward(15)
    end_fill()
    penup()
    setheading(180)
    forward(18)
    right(angle)
    forward(12)
    setheading(60)
    pendown()
    width(7)
    forward(17)
    penup()

    # Head
    setheading(0)
    forward(10)
    right(angle)
    forward(40)
    setheading(0)
    fillcolor('#000000') # black
    begin_fill()
    draw_oval(30)
    end_fill()
    setheading(0)
    forward(40)
    setheading(angle)
    forward(10)
    setheading(120)
    begin_fill()
    draw_oval(20)
    end_fill()
    setheading(0)
    forward(15)
    setheading(angle)
    forward(5)
    setheading(120)
    begin_fill()
    draw_oval(20)
    end_fill()

    # Eyes
    fillcolor('#FFFFFF') # white
    setheading(120)
    begin_fill()
    draw_oval(16, 5)
    end_fill()
    setheading(180)
    forward(10)
    setheading(270)
    forward(5)
    setheading(120)
    begin_fill()
    draw_oval(16, 5)
    end_fill()
    fillcolor('#000000') # black
    setheading(120)
    begin_fill()
    draw_oval(6, 2)
    end_fill()
    setheading(0)
    forward(10)
    left(angle)
    forward(5)
    setheading(120)
    begin_fill()
    draw_oval(6, 2)
    end_fill()

    # Mouth
    setheading(180)
    forward(5)
    setheading(270)
    forward(22)
    fillcolor('bisque')
    setheading(50)
    begin_fill()
    draw_oval(15)
    end_fill()
    setheading(0)
    forward(12)
    setheading(angle)
    forward(3)
    setheading(50)
    begin_fill()
    draw_oval(15)
    end_fill()
    setheading(0)
    forward(12)
    setheading(270)
    forward(2)
    setheading(50)
    begin_fill()
    draw_oval(20)
    end_fill()
    setheading(0)
    forward(10)
    setheading(angle)
    forward(7)
    setheading(30)
    begin_fill()
    draw_oval(15, 5)
    end_fill()
    setheading(180)
    forward(35)
    setheading(280)
    begin_fill()
    circle(20, 180)
    end_fill()
    setheading(180)
    forward(40)
    setheading(270)
    forward(5)
    setheading(170)
    begin_fill()
    draw_oval(15, 5)
    end_fill()

    # Lips
    setheading(180)
    forward(15)
    setheading(angle)
    forward(1)
    setheading(325)
    pendown()
    width(2)
    color('#000000') # black
    circle(40, 80)
    setheading(310)
    circle(10, 70)
    penup()

    # Nose
    setheading(angle)
    forward(13)
    left(angle)
    forward(7)
    fillcolor('#000000') # black
    setheading(80)
    begin_fill()
    draw_oval(10)
    end_fill()

    # Teeth
    setheading(270)
    forward(15)
    pendown()
    fillcolor('#FFFFFF') # white
    begin_fill()
    forward(3)
    setheading(10)
    forward(5)
    setheading(angle)
    forward(4)
    end_fill()
    penup()
    setheading(180)
    forward(20)
    setheading(270)
    forward(7)
    pendown()
    begin_fill()
    forward(3)
    setheading(180)
    forward(5)
    right(angle)
    forward(2)
    end_fill()

    # Wrinkles
    penup()
    forward(25)
    setheading(0)
    forward(5)
    pendown()
    setheading(200)
    circle(25, 35)
    penup()
    setheading(angle)
    forward(5)
    pendown()
    setheading(200)
    circle(25, 35)
    penup()

    # Ears
    setheading(270)
    forward(5)
    setheading(180)
    forward(50)
    pendown()
    width(7)
    setheading(240)
    forward(10)
    setheading(230)
    width(8.5)
    forward(10)
    setheading(210)
    width(10)
    forward(20)
    setheading(200)
    width(11.5)
    forward(20)
    penup()
    setheading(0)
    forward(70)
    left(angle)
    forward(25)
    pendown()
    setheading(240)
    width(7)
    forward(12)
    setheading(230)
    width(8.5)
    forward(9)
    setheading(210)
    width(10)
    forward(8)

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# ------------------------------------------
#               BROKEN TILES          
# ------------------------------------------
# BROKEN LARGE TILE function
# draws cracks on large tiles
#
def break_large_tile():
    color('#FFFFFF') # white
    fillcolor('#FFFFFF') # white
    setheading(157)
    forward(195)
    pendown()
    setheading(310)
    forward(20)
    width(3)
    forward(25)
    width(5)
    forward(25)
    width(7)
    forward(25)
    width(9)
    setheading(260)
    begin_fill()
    forward(90)
    setheading(20)
    forward(90)
    setheading(40)
    forward(60)
    end_fill()
    left(20)
    width(5)
    forward(20)
    width(3)
    forward(13)
    width(1)
    forward(10)
    penup()
    setheading(225)
    forward(100)
    setheading(310)
    width(12)
    pendown()
    forward(20)
    width(9)
    forward(20)
    width(7)
    forward(20)
    setheading(350)
    width(5)
    forward(16)
    width(3)
    forward(16)
    penup()
    setheading(175)
    forward(single + 53)
    pendown()
    setheading(260)
    width(9)
    forward(10)
    setheading(200)
    width(7)
    forward(15)
    width(5)
    forward(15)
    width(3)
    forward(12)

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# BROKEN SMALL TILE function
# draws cracks on small tiles
#
def break_small_tile():
    color('#FFFFFF') # white
    fillcolor('#FFFFFF') # white
    setheading(100)
    forward(42)
    pendown()
    setheading(290)
    forward(10)
    width(3)
    forward(10)
    width(5)
    forward(10)
    width(7)
    forward(10)
    begin_fill()
    forward(40)
    setheading(15)
    forward(35)
    setheading(60)
    forward(30)
    setheading(230)
    forward(25)
    setheading(170)
    forward(40)
    end_fill()
    setheading(270)
    forward(20)
    setheading(250)
    width(5)
    forward(15)
    setheading(200)
    width(3)
    forward(15)
    width(1)
    forward(15)
    penup()
    setheading(22)
    forward(80)
    pendown()
    setheading(320)
    width(5)
    forward(15)
    width(3)
    forward(12)
    penup()
    setheading(95)
    forward(45)
    pendown()
    width(5)
    setheading(80)
    forward(15)
    width(3)
    forward(10)
    width(1)
    forward(5)

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# BROKEN TALL TILE function
# draws cracks on tall tiles
#
def break_tall_tile():
    color('#FFFFFF') # white
    fillcolor('#FFFFFF') # white
    setheading(0)
    forward(15)
    pendown()
    begin_fill()
    setheading(130)
    forward(70)
    setheading(50)
    forward(100)
    setheading(250)
    forward(80)
    setheading(280)
    forward(60)
    end_fill()
    penup()
    setheading(111)
    forward(10)
    pendown()
    setheading(290)
    width(5)
    forward(14)
    width(3)
    forward(14)
    width(1)
    forward(13)
    penup()
    setheading(88.5)
    forward(162)
    pendown()
    width(5)
    setheading(110)
    forward(14)
    width(3)
    forward(12)
    width(1)
    forward(12)
    penup()
    setheading(250)
    forward(115)
    pendown()
    setheading(220)
    width(5)
    forward(18)
    width(3)
    forward(13)

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# BROKEN WIDE TILE function
# draws cracks on wide tiles
#
def break_wide_tile():
    color('#FFFFFF') # white
    fillcolor('#FFFFFF') # white
    pendown()
    setheading(140)
    begin_fill()
    forward(60)
    setheading(20)
    forward(120)
    end_fill()
    setheading(240)
    forward(4)
    setheading(350)
    width(6)
    forward(20)
    width(5)
    forward(10)
    width(3)
    forward(20)
    setheading(30)
    width(1)
    forward(20)
    penup()
    setheading(210)
    forward(153)
    pendown()
    setheading(250)
    width(3)
    begin_fill()
    forward(10)
    setheading(100)
    forward(20)
    end_fill()
    setheading(145)
    forward(45)
    setheading(100)
    width(3)
    forward(20)
    width(2)
    forward(20)
    width(1)
    forward(10)

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()


# ------------------------------------------
#                   TILES          
# ------------------------------------------
# LARGE TILE function
# draws a large red tile starting from top left corner
#
def draw_large_tile():
    setheading(angle)
    forward(101)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#FF0000')
    begin_fill()
    for border in range(4):
        forward(double)
        right(angle)
    end_fill()
    penup()
    # Draws Mickey image
    draw_mickey()


# SMALL TILE function
# draws a small pink tile starting from top left corner
#
def draw_small_tile():
    setheading(angle)
    forward(1)
    setheading(0)
    pendown()
    width(2)
    color('#800000')
    fillcolor('pink')
    begin_fill()
    for border in range(4):
        forward(single)
        right(angle)
    end_fill()
    penup()
    # Draws Minnie image
    draw_minnie()


# TALL TILE function
# draws a tall blue tile starting from top left corner
#
def draw_tall_tile():
    setheading(angle)
    forward(101)
    setheading(0)
    pendown()
    width(2)
    color('#800000')
    fillcolor('light blue')
    begin_fill()
    for border in range(4):
        forward(single)
        right(angle)
        forward(double)
        right(angle)
    end_fill()
    penup()
    # Draws Donald image
    draw_donald()


# WIDE TILE function
# draws a wide orange tile starting from top left corner
#
def draw_wide_tile():
    setheading(angle)
    forward(1)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#FFA500') # orange
    begin_fill()
    for border in range(2):
        forward(double)
        right(angle)
        forward(single)
        right(angle)
    end_fill()
    penup()
    # Draws Goofy image
    draw_goofy()


# ------------------------------------------
#                   LEGENDS          
# ------------------------------------------
# LEGEND function
# Places legends with visuals & text describing it

def legend():
    # LEFT SIDE
    goto(-(grid_width * cell_size) // 2 - 250, 250)
    setheading(0)

    # Draws Mickey image
    draw_large_tile()
    goto(-(grid_width * cell_size) // 2 - 65, 10)

    # Adds Mickey text
    write('Mickey Mouse', align='right', font="Verdana 15")

    goto(-(grid_width * cell_size) // 2 - 200, -50)
    setheading(0)

    # Draws Minnie image
    draw_small_tile()
    goto(-(grid_width * cell_size) // 2 - 65, -190)

    # Adds Minnie text
    write('Minnie Mouse', align='right', font="Verdana 15")

    # RIGHT SIDE
    goto((grid_width * cell_size) // 2 + 90, 250)
    setheading(0)

    # Draws Donald image
    draw_tall_tile()
    goto((grid_width * cell_size) // 2 + 220, 10)

    # Adds Donald Text
    write('Donald Duck', align='right', font="Verdana 15")

    goto((grid_width * cell_size) // 2 + 40, -50)
    setheading(0)

    # Draws Goofy image
    draw_wide_tile()

    # Adds Goofy text
    goto((grid_width * cell_size) // 2 + 180, -190)
    write('Goofy', align='right', font="Verdana 15")


# ------------------------------------------
#               TESSELLATE          
# ------------------------------------------
# TESSELLATE function
# Fills the grid with tiles as per the provided dataset

def tessellate(pattern):
    # Draws the legend
    legend()

    # ------------------------------------------
    # Decides where a tile should be placed by taking the first
    # string in a command and converting it into coordinates
    #
    for commands in pattern:
        grid_square = commands[0]

        # Converts a X coordinate
        if grid_square[0] == 'A':
            x = ord('A') - 565
        if grid_square[0] == 'B':
            x = ord('B') - 466
        if grid_square[0] == 'C':
            x = ord('C') - 367
        if grid_square[0] == 'D':
            x = ord('D') - 268
        if grid_square[0] == 'E':
            x = ord('E') - 169
        if grid_square[0] == 'F':
            x = ord('F') - 70
        if grid_square[0] == 'G':
            x = ord('G') + 29
        if grid_square[0] == 'H':
            x = ord('H') + 128
        if grid_square[0] == 'I':
            x = ord('I') + 227
        if grid_square[0] == 'J':
            x = ord('J') + 326

        # Converts a Y coordinate
        if grid_square[1] == '1':
            y = -250
        if grid_square[1] == '2':
            y = -150
        if grid_square[1] == '3':
            y = -50
        if grid_square[1] == '4':
            y = 50
        if grid_square[1] == '5':
            y = 150
        if grid_square[1] == '6':
            y = 250
        if grid_square[1] == '7':
            y = 350

        # Goes to the coordinates
        goto(x, y)

        # ------------------------------------------
        # Joins all strings in a command to be able to count
        # any repeated numbers (representing rows)
        #
        # This is to differentiate between long & wide tiles
        # as wide tiles need to fill multiple rows unlike tall tiles
        #
        # Counts rows 1, 2, 3, 4, 5, 6, 7
        string = " ".join(commands)
        count_1s = string.count('1')
        count_2s = string.count('2')
        count_3s = string.count('3')
        count_4s = string.count('4')
        count_5s = string.count('5')
        count_6s = string.count('6')
        count_7s = string.count('7')

        # ------------------------------------------
        # Determines which tile is needed by counting the
        # amount of grid spaces that need filling in a command
        #
        # Additionally if a command ends with an 'X' the tile
        # will be broken
        #
        # Small tiles
        if len(commands) == 2:
            draw_small_tile()
            if commands[-1] == 'X':
                break_small_tile()

        # Wide OR tall tiles
        elif len(commands) == 3:
            if count_1s == 2 or count_2s == 2 \
                    or count_3s == 2 or count_4s == 2 \
                    or count_5s == 2 or count_6s == 2 \
                    or count_7s == 2:
                draw_wide_tile()
                if commands[-1] == 'X':
                    break_wide_tile()

            else:
                draw_tall_tile()
                if commands[-1] == 'X':
                    break_tall_tile()

        # Large tiles
        elif len(commands) == 5:
            draw_large_tile()
            if commands[-1] == 'X':
                break_large_tile()


# ------------------------------------------
#
#           End of submission
#           ~JOHNNY MADIGAN~
#
# --------------------------------------------------------------------#


# -----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas('#F5F5F5', '#ffb6c1', mark_legend=False) # white smoke, light pink

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tiles
title("Disney Icons (Mickey, Minnie, Donald & Goofy)")

### Call the student's function to follow the path
### ***** While developing your program you can call the tessellate
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your tessellate function must work for any data
### ***** set that can be returned by the random_pattern function.
# tessellate(fixed_pattern_16) # <-- used for code development only, not marking
tessellate(random_pattern())  # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
# --------------------------------------------------------------------#