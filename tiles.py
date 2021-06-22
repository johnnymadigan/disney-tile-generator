
from turtle import *
import shapes
import mickey
import minnie
import donald
import goofy

# ------------------------------------------
#                   TILES          
# ------------------------------------------
# LARGE TILE function
# draws a large red tile starting from top left corner
#
def draw_large_tile():
    setheading(shapes.angle)
    forward(101)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#FF0000')
    begin_fill()
    for border in range(4):
        forward(shapes.double)
        right(shapes.angle)
    end_fill()
    penup()
    # Draws Mickey image
    mickey.draw_mickey()


# SMALL TILE function
# draws a small pink tile starting from top left corner
#
def draw_small_tile():
    setheading(shapes.angle)
    forward(1)
    setheading(0)
    pendown()
    width(2)
    color('#800000')
    fillcolor('pink')
    begin_fill()
    for border in range(4):
        forward(shapes.single)
        right(shapes.angle)
    end_fill()
    penup()
    # Draws Minnie image
    minnie.draw_minnie()


# TALL TILE function
# draws a tall blue tile starting from top left corner
#
def draw_tall_tile():
    setheading(shapes.angle)
    forward(101)
    setheading(0)
    pendown()
    width(2)
    color('#800000')
    fillcolor('light blue')
    begin_fill()
    for border in range(4):
        forward(shapes.single)
        right(shapes.angle)
        forward(shapes.double)
        right(shapes.angle)
    end_fill()
    penup()
    # Draws Donald image
    donald.draw_donald()


# WIDE TILE function
# draws a wide orange tile starting from top left corner
#
def draw_wide_tile():
    setheading(shapes.angle)
    forward(1)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#FFA500') # orange
    begin_fill()
    for border in range(2):
        forward(shapes.double)
        right(shapes.angle)
        forward(shapes.single)
        right(shapes.angle)
    end_fill()
    penup()
    # Draws Goofy image
    goofy.draw_goofy()