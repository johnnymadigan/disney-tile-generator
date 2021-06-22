
from turtle import *
import shapes

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
    forward(shapes.single + 53)
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
