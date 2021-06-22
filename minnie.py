from turtle import *
import shapes

# MINNIE MOUSE function
# Draws Minnie starting from the top left corner of a tile
# (do not change code)
#
def draw_minnie():
    # Background
    setheading(0)
    forward(shapes.single // 2)
    right(shapes.angle)
    forward(7)
    shapes.draw_star('plum', 35)
    setheading(shapes.angle)
    forward(7)
    setheading(180)
    forward(shapes.single // 2)

    # Head
    setheading(0)
    forward(shapes.single // 2)
    right(shapes.angle)
    forward(60)
    dot(55, '#000000') # black

    # Ears
    setheading(180)
    forward(30)
    right(shapes.angle)
    forward(20)
    dot(30, '#000000') # black
    forward(10)
    right(shapes.angle)
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
    shapes.draw_oval(20)
    end_fill()
    setheading(180)
    forward(0)
    setheading(270)
    forward(10)
    setheading(30)
    begin_fill()
    shapes.draw_oval(20, 5)
    end_fill()
    setheading(shapes.angle)
    forward(8)
    setheading(200)
    begin_fill()
    shapes.draw_oval(15)
    end_fill()
    setheading(100)
    begin_fill()
    shapes.draw_oval(20, 5)
    end_fill()
    setheading(0)
    forward(10)
    left(shapes.angle)
    forward(3)
    setheading(100)
    begin_fill()
    shapes.draw_oval(18, 5)
    end_fill()

    # Nose
    setheading(shapes.angle)
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
    shapes.draw_oval(7)
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
    setheading(shapes.angle)
    forward(4)
    pendown()
    fillcolor('#800000')
    begin_fill()
    setheading(240)
    circle(9, 195)
    end_fill()
    penup()

    # Eyes
    setheading(shapes.angle)
    forward(17)
    setheading(180)
    forward(4)
    fillcolor('#000000') # black
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(8, 5)
    end_fill()
    setheading(0)
    forward(11)
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(8, 5)
    end_fill()

    # Bowtie
    setheading(180)
    forward(33)
    setheading(shapes.angle)
    forward(25)
    fillcolor('deep pink')
    begin_fill()
    setheading(100)
    shapes.draw_oval(7)
    end_fill()
    setheading(180)
    forward(8)
    setheading(shapes.angle)
    forward(10)
    fillcolor('hot pink')
    begin_fill()
    setheading(170)
    shapes.draw_oval(12)
    end_fill()
    setheading(180)
    forward(1)
    setheading(270)
    forward(5)
    begin_fill()
    setheading(210)
    shapes.draw_oval(12)
    end_fill()
    setheading(0)
    forward(10)
    setheading(30)
    begin_fill()
    shapes.draw_oval(12)
    end_fill()
    setheading(270)
    forward(2)
    setheading(350)
    begin_fill()
    shapes.draw_oval(12)
    end_fill()

    # Polka dots
    dot(5, '#FFFFFF') # white
    setheading(0)
    forward(10)
    right(shapes.angle)
    forward(2)
    dot(5, '#FFFFFF') # white
    setheading(shapes.angle)
    forward(13)
    setheading(180)
    forward(3)
    dot(5, '#FFFFFF') # white
    forward(28)
    left(shapes.angle)
    forward(2)
    dot(5, '#FFFFFF') # white
    forward(10)
    setheading(0)
    forward(5)
    dot(5, '#FFFFFF') # white
    setheading(180)
    forward(5)
    left(shapes.angle)
    forward(7)
    dot(5, '#FFFFFF') # white

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()
