'''
idea from:
https://www.youtube.com/watch?v=p4Iz0XJY-Qk&t=1302s
'''

import turtle as t
import numpy as np
import time, math

delay = 0.01
angle = 0

def projection(point):
    return np.matmul(
            np.array(
                [[1,0,0],
                 [0,1,0],
                 [0,0,0],
                 ]),
            point,
        )

def rotationX(angle,point):
    return np.matmul(
            np.array(
                [[1,0,0],
                 [0, math.cos(angle),-math.sin(angle)],
                 [0, math.sin(angle), math.cos(angle)],
                 ]),
            point,
        )

def rotationY(angle,point):
    return np.matmul(
            np.array(
                [[math.cos(angle), 0, math.sin(angle)],
                 [0,1,0],
                 [-math.sin(angle), 0, math.cos(angle)],
                 ]),
            point,
        )

def rotationZ(angle,point):
    return np.matmul(
            np.array(
                [[math.cos(angle), -math.sin(angle),0],
                 [math.sin(angle), math.cos(angle),0],
                 [0,0,1]
                 ]),
            point,
        )

def project_rotate_super_function(point):
    rotated = rotationX(angle,point)
    rotated = rotationY(angle,rotated)
    rotated = rotationZ(angle,rotated)
    projected = np.multiply(projection(rotated), 100)
    return projected

def connect(projected_points):
    line_pen.goto(projected_points[0][0],projected_points[0][1])
    line_pen.down()
    line_pen.goto(projected_points[1][0],projected_points[1][1])
    line_pen.goto(projected_points[2][0],projected_points[2][1])
    line_pen.goto(projected_points[3][0],projected_points[3][1])
    line_pen.goto(projected_points[0][0],projected_points[0][1])
    line_pen.up()
    line_pen.goto(projected_points[4][0],projected_points[4][1])
    line_pen.down()
    line_pen.goto(projected_points[5][0],projected_points[5][1])
    line_pen.goto(projected_points[6][0],projected_points[6][1])
    line_pen.goto(projected_points[7][0],projected_points[7][1])
    line_pen.goto(projected_points[4][0],projected_points[4][1])
    line_pen.up()
    line_pen.goto(projected_points[0][0],projected_points[0][1])
    line_pen.down()
    line_pen.goto(projected_points[4][0],projected_points[4][1])
    line_pen.up()
    line_pen.goto(projected_points[1][0],projected_points[1][1])
    line_pen.down()
    line_pen.goto(projected_points[5][0],projected_points[5][1])
    line_pen.up()
    line_pen.goto(projected_points[2][0],projected_points[2][1])
    line_pen.down()
    line_pen.goto(projected_points[6][0],projected_points[6][1])
    line_pen.up()
    line_pen.goto(projected_points[3][0],projected_points[3][1])
    line_pen.down()
    line_pen.goto(projected_points[7][0],projected_points[7][1])
    line_pen.up()

# points
points = [
    [-1,-1,-1],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1],
    [-1,-1,1],
    [1,-1,1],
    [1,1,1],
    [-1,1,1],
]

# set up the screen
wn = t.Screen()
wn.title("rotation cube")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)  # 取消延遲

# set up the pen
pen_0 = t.Turtle()
pen_0.speed(0)
pen_0.shape("circle")
pen_0.color("white")
pen_0.up()
pen_1 = t.Turtle()
pen_1.speed(0)
pen_1.shape("circle")
pen_1.color("white")
pen_1.up()
pen_2 = t.Turtle()
pen_2.speed(0)
pen_2.shape("circle")
pen_2.color("white")
pen_2.up()
pen_3 = t.Turtle()
pen_3.speed(0)
pen_3.shape("circle")
pen_3.color("white")
pen_3.up()
pen_4 = t.Turtle()
pen_4.speed(0)
pen_4.shape("circle")
pen_4.color("white")
pen_4.up()
pen_5 = t.Turtle()
pen_5.speed(0)
pen_5.shape("circle")
pen_5.color("white")
pen_5.up()
pen_6 = t.Turtle()
pen_6.speed(0)
pen_6.shape("circle")
pen_6.color("white")
pen_6.up()
pen_7 = t.Turtle()
pen_7.speed(0)
pen_7.shape("circle")
pen_7.color("white")
pen_7.up()

# set up the pen for drawing lines
line_pen = t.Turtle()
line_pen.speed(0)
line_pen.color("white")
line_pen.hideturtle()
line_pen.up()

while True:
    wn.update()

    # point_0
    projected_screen = project_rotate_super_function(points[0])
    pen_0.goto(projected_screen[0], projected_screen[1])
    # point_1
    projected_screen = project_rotate_super_function(points[1])
    pen_1.goto(projected_screen[0], projected_screen[1])
    # point_2
    projected_screen = project_rotate_super_function(points[2])
    pen_2.goto(projected_screen[0], projected_screen[1])
    # point_3
    projected_screen = project_rotate_super_function(points[3])
    pen_3.goto(projected_screen[0], projected_screen[1])
    # point_4
    projected_screen = project_rotate_super_function(points[4])
    pen_4.goto(projected_screen[0], projected_screen[1])
    # point_5
    projected_screen = project_rotate_super_function(points[5])
    pen_5.goto(projected_screen[0], projected_screen[1])
    # point_6
    projected_screen = project_rotate_super_function(points[6])
    pen_6.goto(projected_screen[0], projected_screen[1])
    # point_7
    projected_screen = project_rotate_super_function(points[7])
    pen_7.goto(projected_screen[0], projected_screen[1])

    # connect points
    projected_points = [
        pen_0.pos(),
        pen_1.pos(),
        pen_2.pos(),
        pen_3.pos(),
        pen_4.pos(),
        pen_5.pos(),
        pen_6.pos(),
        pen_7.pos(),
    ]
    line_pen.clear()
    connect(projected_points)

    angle += 0.02
    time.sleep(delay)