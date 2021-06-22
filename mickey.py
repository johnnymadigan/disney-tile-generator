from turtle import *
import shapes

def draw_mickey():
    """
    Draws Mickey Mouse.
    """
    
    setheading(0)
    forward(shapes.single)
    right(shapes.angle)
    forward(15)
    shapes.draw_star('#990000', 70) # crimson
    setheading(shapes.angle)
    forward(15)
    setheading(180)
    forward(shapes.single)

    # Head
    setheading(0)
    forward(shapes.single)
    right(shapes.angle)
    forward(shapes.single + 20)
    dot(102, '#000000') # black
    forward(33)
    setheading(180)
    forward(35)

    # Face
    fillcolor('#FFFFFF') # white
    setheading(0)
    begin_fill()
    shapes.draw_oval(50)
    end_fill()
    forward(50)
    setheading(shapes.angle)
    forward(65)
    setheading(105)
    begin_fill()
    shapes.draw_oval(30)
    end_fill()
    setheading(0)
    forward(20)
    right(shapes.angle)
    forward(5)
    setheading(75)
    begin_fill()
    shapes.draw_oval(30)
    end_fill()

    # Eyes
    fillcolor('#000000') # black
    setheading(180)
    forward(7)
    setheading(90)
    begin_fill()
    shapes.draw_oval(15, 5)
    end_fill()
    setheading(180)
    forward(17)
    setheading(90)
    begin_fill()
    shapes.draw_oval(15, 5)
    end_fill()

    # Nose
    setheading(180)
    forward(2)
    setheading(270)
    forward(11)
    setheading(0)
    begin_fill()
    shapes.draw_oval(10)
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
    left(shapes.angle)
    forward(3)
    color('#000000') # black
    setheading(320)
    pendown()
    width(3)
    circle(45, 90)
    penup()
    setheading(180)
    forward(43)
    left(shapes.angle)
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
    setheading(shapes.angle)
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
    right(shapes.angle)
    forward(25)
    setheading(45)
    fillcolor('#000000') # black
    begin_fill()
    shapes.draw_oval(40)
    end_fill()
    setheading(0)
    forward(140)
    left(shapes.angle)
    forward(20)
    setheading(135)
    begin_fill()
    shapes.draw_oval(40)
    end_fill()

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()
