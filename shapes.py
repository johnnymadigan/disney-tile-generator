from turtle import *
# Length of two grid spaces
double = 200

# Length of one grid space
single = 100

# Right angle
angle = 90

def draw_oval(radius, stretch=2):
    """
    Draws an oval.

    :param: radius: radius of the oval
    :param: stretch: distorts the oval, default value of 2
    """
    right(angle // 2)

    for loop in range(2):
        circle(radius, 90)
        circle(radius / stretch, 90)


def draw_star(colour, length):
    """
    Draws a star.

    :param: colour: colour of the star
    :param: length: length of any edge determining the star's size
    """
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


def draw_oval(radius, stretch=2):
    """
    Draws an oval.

    :param: radius: radius of the oval
    :param: stretch: distorts the oval, default value of 2
    """
    right(angle // 2)

    for loop in range(2):
        circle(radius, 90)
        circle(radius / stretch, 90)


def draw_star(colour, length):
    """
    Draws a star.

    :param: colour: colour of the star
    :param: length: length of any edge determining the star's size
    """
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