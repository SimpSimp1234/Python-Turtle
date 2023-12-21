from turtle import Screen, Turtle
from random import randint

def draw_art_cube(x, y):
    screen.onscreenclick(None)  # 禁止畫圖案時點擊
    pen.up()
    pen.setposition(x, y)
    pen.down()
    width = randint(25, 100)
    draw_triangle(width)
    screen.onscreenclick(draw_art_cube)  # 畫完圖案圖案後啟動點擊function

def draw_triangle(short):
    long = short * 2**0.5
    pen.seth(0)
    pen.fillcolor(colour[randint(0,6)])
    for i in range(4):
        pen.begin_fill()
        pen.forward(short)
        pen.right(135)
        pen.forward(long)
        pen.right(135)
        pen.forward(short)
        pen.end_fill()
        pen.right(180)


colour = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']

screen = Screen()
screen.title('on screen click')
screen.setup(600, 600)

pen = Turtle()
pen.hideturtle()
pen.speed('fastest')
pen.pensize(2)

screen.onscreenclick(draw_art_cube)
screen.mainloop()