import turtle
import time
import random

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

if __name__ == "__main__":
    delay = 0.1

    # Score
    score = 0
    high_score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=800)
    wn.tracer(0) # 取消延遲

    # 邊框
    turtle.speed(10)
    turtle.pensize(4)
    turtle.up()
    turtle.goto(-310,-310)
    turtle.down()
    turtle.pencolor("red")
    for i in range(4):
        turtle.fd(620)
        turtle.left(90)
    turtle.hideturtle()

    # head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("green")
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 340)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    # Keyboard
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()

        # 檢查是否撞 border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # 隱藏 segment
            for segment in segments:
                segment.goto(10000, 10000)
            
            # 清空 smgments list
            segments.clear()

            # 重設 score
            score = 0

            # 重設 delay
            delay = 0.1

            # 刷新分數
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


        # 檢查是否撞到 food
        if head.distance(food) < 20:
            # random 新 food
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            # 新增一段 segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # 加速
            delay -= 0.001

            # 加分
            score += 10

            if score > high_score:
                high_score = score
            
            # 刷新分數
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

        # 從最後一段 segment 開始，每一段 segment 向前移一格
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # 把 segments 0 移到 head 的位置
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # 檢查 head 是否撞到 segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
            
                # 隱藏 segment
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # 清空 smgments list
                segments.clear()

                # 重設 score
                score = 0

                # R重設 delay
                delay = 0.1
            
                # 刷新分數
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)