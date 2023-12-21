# Slime Volleyball
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Slime Volleyball")
wn.tracer(0)

player = turtle.Turtle()
player.shape("circle")
player.color("yellow")
player.shapesize(3.0, 3.0, 0)
player.speed(0)
player.penup()
player.dx = 0

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(1.0, 1.0, 0)
ball.speed(0)
ball.penup()
ball.dy = 0

GRAVITY = -0.1

player.goto(0, -200)
ball.goto(0,0)

while True:
    # Gravity
    ball.dy += GRAVITY
    ball.sety(ball.ycor() + ball.dy)

    # 碰撞
    if ball.distance(player) < 40:
        # 把ball移回原點
        ball.sety(ball.ycor() - ball.dy)
        # Update the dy
        ball.dy *= -0.99
    # print(ball.dy)
    wn.update()
    
wn.mainloop()