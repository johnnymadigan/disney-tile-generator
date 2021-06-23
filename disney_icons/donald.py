from turtle import *
import shapes

def draw_donald():
    """
    Draws Donald Duck.
    """
    
    # Background
    setheading(0)
    forward(shapes.single // 2)
    right(shapes.angle)
    forward(shapes.single // 2)
    shapes.draw_star('#87cefa', 35) # light sky blue
    setheading(shapes.angle)
    forward(shapes.single // 2)
    setheading(180)
    forward(shapes.single // 2)

    # Hat
    setheading(0)
    forward(shapes.single // 2)
    forward(5)
    right(shapes.angle)
    forward(shapes.single // 2)
    setheading(120)
    fillcolor('#0000FF') # blue
    begin_fill()
    shapes.draw_oval(30)
    end_fill()
    setheading(0)
    forward(15)
    left(shapes.angle)
    forward(8)
    setheading(160)
    fillcolor('#0000FF') # blue
    begin_fill()
    shapes.draw_oval(25)
    end_fill()
    setheading(0)
    forward(15)
    right(shapes.angle)
    forward(5)
    setheading(160)
    fillcolor('#0000FF') # blue
    begin_fill()
    shapes.draw_oval(20)
    end_fill()
    setheading(180)
    forward(32.5)
    left(shapes.angle)
    forward(10)
    dot(25, '#000000') # black
    right(shapes.angle)
    forward(12.5)
    pendown()
    color('#000000') # black
    left(shapes.angle)
    fillcolor('#000000') # black
    begin_fill()
    forward(15)
    left(shapes.angle)
    forward(25)
    left(shapes.angle)
    forward(12.5)
    end_fill()
    penup()

    # Head
    left(shapes.angle)
    forward(12.5)
    left(shapes.angle)
    forward(40)
    dot(70, '#FFFFFF') # white
    setheading(180)
    forward(6)
    fillcolor('#FFFFFF') # white
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(25)
    end_fill()
    setheading(0)
    forward(30)
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(25)
    end_fill()

    # Eyes
    setheading(180)
    forward(5)
    setheading(270)
    forward(5)
    fillcolor('#d3d3d3') # light grey
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(25, 6)
    end_fill()
    setheading(180)
    forward(30)
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(25, 6)
    end_fill()

    # Pupils
    fillcolor('#000000') # black
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(11, 5)
    end_fill()
    setheading(0)
    forward(25)
    setheading(shapes.angle)
    begin_fill()
    shapes.draw_oval(11, 5)
    end_fill()

    # Mouth
    setheading(180)
    forward(44)
    left(shapes.angle)
    forward(0)
    fillcolor('#FFA500') # orange
    setheading(270)
    begin_fill()
    circle(30, 180)
    end_fill()
    setheading(180)
    forward(30)
    dot(20, '#FFA500') # orange
    setheading(180)
    forward(25)
    width(5)
    setheading(0)
    forward(52)
    color('#FFA500') # orange
    fillcolor('#800000') # crimson
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
    fillcolor('#FFA500') # orange
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
    right(shapes.angle)
    forward(11)
    color('#ff8c00') # dark orange
    width(8)
    pendown()
    setheading(150)
    circle(30, 55)
    penup()
    color('#000000') # black

    # Bowtie
    setheading(0)
    forward(11)
    right(shapes.angle)
    forward(shapes.single // 2)
    fillcolor('#FF0000') # red
    begin_fill()
    shapes.draw_oval(10)
    end_fill()
    setheading(180)
    forward(2)
    left(shapes.angle)
    forward(2)
    setheading(160)
    pendown()
    width(3)
    color('#8B0000') # dark red
    fillcolor('#FF0000') # red
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
    setheading(shapes.angle)
    circle(6, 180)
    end_fill()

    # Resets back to default drawing values
    fillcolor('#000000') # black
    color('#000000') # black
    width(1)
    penup()
