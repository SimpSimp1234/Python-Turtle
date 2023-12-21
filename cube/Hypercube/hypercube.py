'''
idea from:
https://www.youtube.com/watch?v=XE3YDVdQSPo&t=278s
'''

import turtle as t
import numpy as np
import time, math

delay = 0.01
angle = 0
angle_x = math.pi /  3
distance = 2

def projection_4D(point):
    w = 1 / (distance - point[3])
    return np.matmul(
        np.array(
            [[w, 0, 0, 0],
             [0, w, 0, 0],
             [0, 0, w, 0]
             ]),
        point
    )

def projection_3D(point):
    return np.matmul(
            np.array(
                [[1,0,0],
                 [0,1,0],
                 [0,0,0],
                 ]),
            point
        )

def rotationXY(angle, point):
    return np.matmul(
            np.array(
                [[math.cos(angle), -math.sin(angle), 0, 0],
                 [math.sin(angle), math.cos(angle), 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]
                 ]),
            point,
        )

def rotationZW(angle, point):
    return np.matmul(
            np.array(
                [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, math.cos(angle), -math.sin(angle)],
                 [0, 0, math.sin(angle), math.cos(angle)]
                 ]),
            point,
        )

def rotationX_3D(angle, point):
    return np.matmul(
            np.array(
                [[1,0,0],
                 [0, math.cos(angle),-math.sin(angle)],
                 [0, math.sin(angle), math.cos(angle)],
                 ]),
            point,
        )

def rotationY_3D(angle, point):
    return np.matmul(
            np.array(
                [[math.cos(angle), 0, -math.sin(angle)],
                 [0,1,0],
                 [math.sin(angle), 0, math.cos(angle)],
                 ]),
            point,
        )

def rotationZ_3D(angle, point):
    return np.matmul(
            np.array(
                [[math.cos(angle), -math.sin(angle),0],
                 [math.sin(angle), math.cos(angle),0],
                 [0,0,1]
                 ]),
            point,
        )

def project_rotate_super_function(point):
    rotated_4D = rotationXY(angle, point)
    rotated_4D = rotationZW(angle, rotated_4D)
    projected_4D = projection_4D(rotated_4D)
    rotation_3D = rotationX_3D(angle_x, projected_4D)
    # rotation_3D = rotationY_3D(angle, rotation_3D)
    # rotation_3D = rotationZ_3D(angle, rotation_3D)
    projected = np.multiply(projection_3D(rotation_3D), 100)
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

    line_pen.goto(projected_points[8][0],projected_points[8][1])
    line_pen.down()
    line_pen.goto(projected_points[9][0],projected_points[9][1])
    line_pen.goto(projected_points[10][0],projected_points[10][1])
    line_pen.goto(projected_points[11][0],projected_points[11][1])
    line_pen.goto(projected_points[8][0],projected_points[8][1])
    line_pen.up()

    line_pen.goto(projected_points[12][0],projected_points[12][1])
    line_pen.down()
    line_pen.goto(projected_points[13][0],projected_points[13][1])
    line_pen.goto(projected_points[14][0],projected_points[14][1])
    line_pen.goto(projected_points[15][0],projected_points[15][1])
    line_pen.goto(projected_points[12][0],projected_points[12][1])
    line_pen.up()
    line_pen.goto(projected_points[8][0],projected_points[8][1])
    line_pen.down()
    line_pen.goto(projected_points[12][0],projected_points[12][1])
    line_pen.up()
    line_pen.goto(projected_points[9][0],projected_points[9][1])
    line_pen.down()
    line_pen.goto(projected_points[13][0],projected_points[13][1])
    line_pen.up()
    line_pen.goto(projected_points[10][0],projected_points[10][1])
    line_pen.down()
    line_pen.goto(projected_points[14][0],projected_points[14][1])
    line_pen.up()
    line_pen.goto(projected_points[11][0],projected_points[11][1])
    line_pen.down()
    line_pen.goto(projected_points[15][0],projected_points[15][1])
    line_pen.up()

    line_pen.goto(projected_points[0][0],projected_points[0][1])
    line_pen.down()
    line_pen.goto(projected_points[8][0],projected_points[8][1])
    line_pen.up()
    line_pen.goto(projected_points[1][0],projected_points[1][1])
    line_pen.down()
    line_pen.goto(projected_points[9][0],projected_points[9][1])
    line_pen.up()
    line_pen.goto(projected_points[2][0],projected_points[2][1])
    line_pen.down()
    line_pen.goto(projected_points[10][0],projected_points[10][1])
    line_pen.up()
    line_pen.goto(projected_points[3][0],projected_points[3][1])
    line_pen.down()
    line_pen.goto(projected_points[11][0],projected_points[11][1])
    line_pen.up()
    line_pen.goto(projected_points[4][0],projected_points[4][1])
    line_pen.down()
    line_pen.goto(projected_points[12][0],projected_points[12][1])
    line_pen.up()
    line_pen.goto(projected_points[5][0],projected_points[5][1])
    line_pen.down()
    line_pen.goto(projected_points[13][0],projected_points[13][1])
    line_pen.up()
    line_pen.goto(projected_points[6][0],projected_points[6][1])
    line_pen.down()
    line_pen.goto(projected_points[14][0],projected_points[14][1])
    line_pen.up()
    line_pen.goto(projected_points[7][0],projected_points[7][1])
    line_pen.down()
    line_pen.goto(projected_points[15][0],projected_points[15][1])
    line_pen.up()

# points
points = [
    [-1, -1, -1, 1],
    [1, -1, -1, 1],
    [1, 1, -1, 1],
    [-1, 1, -1, 1],
    [-1, -1, 1, 1],
    [1, -1, 1, 1],
    [1, 1, 1, 1],
    [-1, 1, 1, 1],
    [-1, -1, -1, -1],
    [1, -1, -1, -1],
    [1, 1, -1, -1],
    [-1, 1, -1, -1],
    [-1, -1, 1, -1],
    [1, -1, 1, -1],
    [1, 1, 1, -1],
    [-1, 1, 1, -1],
]

# set up the screen
wn = t.Screen()
wn.title("hypercube")
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
pen_8 = t.Turtle()
pen_8.speed(0)
pen_8.shape("circle")
pen_8.color("white")
pen_8.up()
pen_9 = t.Turtle()
pen_9.speed(0)
pen_9.shape("circle")
pen_9.color("white")
pen_9.up()
pen_10 = t.Turtle()
pen_10.speed(0)
pen_10.shape("circle")
pen_10.color("white")
pen_10.up()
pen_11 = t.Turtle()
pen_11.speed(0)
pen_11.shape("circle")
pen_11.color("white")
pen_11.up()
pen_12 = t.Turtle()
pen_12.speed(0)
pen_12.shape("circle")
pen_12.color("white")
pen_12.up()
pen_13 = t.Turtle()
pen_13.speed(0)
pen_13.shape("circle")
pen_13.color("white")
pen_13.up()
pen_14 = t.Turtle()
pen_14.speed(0)
pen_14.shape("circle")
pen_14.color("white")
pen_14.up()
pen_15 = t.Turtle()
pen_15.speed(0)
pen_15.shape("circle")
pen_15.color("white")
pen_15.up()

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
    # point_8
    projected_screen = project_rotate_super_function(points[8])
    pen_8.goto(projected_screen[0], projected_screen[1])
    # point_9
    projected_screen = project_rotate_super_function(points[9])
    pen_9.goto(projected_screen[0], projected_screen[1])
    # point_10
    projected_screen = project_rotate_super_function(points[10])
    pen_10.goto(projected_screen[0], projected_screen[1])
    # point_11
    projected_screen = project_rotate_super_function(points[11])
    pen_11.goto(projected_screen[0], projected_screen[1])
    # point_12
    projected_screen = project_rotate_super_function(points[12])
    pen_12.goto(projected_screen[0], projected_screen[1])
    # point_13
    projected_screen = project_rotate_super_function(points[13])
    pen_13.goto(projected_screen[0], projected_screen[1])
    # point_14
    projected_screen = project_rotate_super_function(points[14])
    pen_14.goto(projected_screen[0], projected_screen[1])
    # point_15
    projected_screen = project_rotate_super_function(points[15])
    pen_15.goto(projected_screen[0], projected_screen[1])

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
        pen_8.pos(),
        pen_9.pos(),
        pen_10.pos(),
        pen_11.pos(),
        pen_12.pos(),
        pen_13.pos(),
        pen_14.pos(),
        pen_15.pos(),
    ]
    line_pen.clear()
    connect(projected_points)

    angle += 0.02
    time.sleep(delay)