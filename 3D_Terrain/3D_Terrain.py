import turtle as t
import math

scl = 20
w = 600
h = 600
cols = w//scl
rows = h//scl

rotateX=(math.pi/3)


# setup the screen
screen = t.Screen()
screen.title('3D Terrain')
screen.bgcolor('black')
screen.setworldcoordinates(-w//2,0,w//2,h)
screen.tracer(0)

# pen
pen = t.Turtle()
pen.color('white')
pen.hideturtle()
pen.speed(0)

for y in range(0, rows):
	for x in range(-cols//2, cols//2):
		pen.up()
		pen.goto(x*scl, y*scl)
		pen.down()
		for i in range(0,4):
			pen.fd(scl)
			pen.left(90)
		pen.goto(x*scl+scl, y*scl+scl)

t.done()