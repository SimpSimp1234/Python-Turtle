import turtle as t
import time

def paddle_A_up():
	if paddle_A.ycor()+50 < 300:
		paddle_A.sety(paddle_A.ycor() + paddle_A.dy)
def paddle_A_down():
	if paddle_A.ycor()-50 > -300:
		paddle_A.sety(paddle_A.ycor() - paddle_A.dy)
def paddle_B_up():
	if paddle_B.ycor()+50 < 300:
		paddle_B.sety(paddle_B.ycor() + paddle_B.dy)
def paddle_B_down():
	if paddle_B.ycor()-50 > -300:
		paddle_B.sety(paddle_B.ycor() - paddle_B.dy)

if __name__ == "__main__":
	FPS = 0.01
	score_A = 0
	score_B = 0

	# Screen
	screen = t.Screen()
	screen.title('Pong')
	screen.bgcolor('black')
	screen.setup(width=800, height=600)
	screen.tracer(0)

	# Ball
	ball = t.Turtle()
	ball.shape('circle')
	ball.color('white')
	ball.up()
	ball.speed(0)
	ball.dx = 1
	ball.dy = 1

	# paddle A
	paddle_A = t.Turtle()
	paddle_A.shape('square')
	paddle_A.color('white')
	paddle_A.shapesize(stretch_len=1, stretch_wid=5)
	paddle_A.up()
	paddle_A.speed(0)
	paddle_A.goto(-350,0)
	paddle_A.dy = 30

	# paddle B
	paddle_B = t.Turtle()
	paddle_B.shape('square')
	paddle_B.color('white')
	paddle_B.shapesize(stretch_len=1, stretch_wid=5)
	paddle_B.up()
	paddle_B.speed(0)
	paddle_B.goto(350,0)
	paddle_B.dy = 30


	# score writer
	score_writer = t.Turtle()
	score_writer.pencolor("white")
	score_writer.hideturtle()
	score_writer.up()
	score_writer.goto(0,250)
	score_writer.write(f'{score_A} | {score_B}', font=('OpenSans', 32, 'bold'), align = "Center")

	# keyboard
	screen.listen()
	screen.onkeypress(paddle_A_up,"w")
	screen.onkeypress(paddle_A_down,"s")
	screen.onkeypress(paddle_B_up,"Up")
	screen.onkeypress(paddle_B_down,"Down")

	while True:
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# 撞到邊
		# 上下邊框
		if ball.ycor() > 290 or ball.ycor() < -280:
			ball.dy *= -1
		# 左右邊框
		if ball.xcor() > 380:
			ball.dx *= -1
			ball.goto(0,0)
			score_A += 1
			score_writer.clear()
			score_writer.write(f'{score_A} | {score_B}', font=('OpenSans', 32, 'bold'), align = "Center")

		elif ball.xcor() < -390:
			ball.dx *= -1
			ball.goto(0,0)
			score_B += 1
			score_writer.clear()
			score_writer.write(f'{score_A} | {score_B}', font=('OpenSans', 32, 'bold'), align = "Center")

		# hit the ball
		if ball.xcor() < paddle_A.xcor()+20 and ball.ycor() < paddle_A.ycor()+65 and ball.ycor() > paddle_A.ycor()-65:
			ball.dx *= -1
		if ball.xcor() > paddle_B.xcor()-20 and ball.ycor() < paddle_B.ycor()+65 and ball.ycor() > paddle_B.ycor()-65:
			ball.dx *= -1

		screen.update()
		time.sleep(FPS)

	screen.mainloop()