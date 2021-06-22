from turtle import *
import shapes
import mickey
import minnie
import donald
import goofy

def draw_large_tile():
    """
    Draws large 2x2 red tile starting from top left corner.
    Draws Mickey.
    """
    setheading(shapes.angle)
    forward(101)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#FF0000') # red
    begin_fill()
    for border in range(4):
        forward(shapes.double)
        right(shapes.angle)
    end_fill()
    penup()
    mickey.draw_mickey()


def draw_small_tile():
    """
    Draws small 1x1 pink tile starting from top left corner.
    Draws Minnie.
    """
    setheading(shapes.angle)
    forward(1)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#FFC0CB') # pink
    begin_fill()
    for border in range(4):
        forward(shapes.single)
        right(shapes.angle)
    end_fill()
    penup()
    minnie.draw_minnie()



def draw_tall_tile():
    """
    Draws tall 1x2 blue tile starting from top left corner.
    Draws Donald.
    """
    setheading(shapes.angle)
    forward(101)
    setheading(0)
    pendown()
    width(2)
    color('#800000') # maroon
    fillcolor('#add8e6') # light blue
    begin_fill()
    for border in range(4):
        forward(shapes.single)
        right(shapes.angle)
        forward(shapes.double)
        right(shapes.angle)
    end_fill()
    penup()
    donald.draw_donald()



def draw_wide_tile():
    """
    Draws small 2x1 orange tile starting from top left corner.
    Draws Goofy.
    """
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
    goofy.draw_goofy()
