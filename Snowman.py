import turtle
import random

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor(36, 148, 40)
pen = turtle.Turtle()
pen.speed(1000)

racer_1 = turtle.Turtle()
racer_1.shape("turtle")
racer_1.color("blue")

racer_2 = turtle.Turtle()
racer_2.shape("turtle")
racer_2.color("white")


def rec():
    for i in range(2):
        pen.forward(500)
        pen.right(90)
        pen.forward(250)
        pen.right(90)


def move_1():
    racer_1.forward(10)


def move_2():
    racer_2.forward(10)


pen.color(160, 160, 160)

pen.begin_fill()
pen.up()
pen.goto(-125, -250)
pen.down()
pen.left(90)
rec()
pen.end_fill()

pen.color("black")
pen.up()
pen.goto(-70, 0)
pen.down()
pen.hideturtle()

racer_1.up()
racer_1.goto(-62, -230)
racer_1.left(90)

racer_2.up()
racer_2.goto(62, -230)
racer_2.left(90)

screen.listen()
screen.onkey(move_1, "W")

speed = random.uniform(0.5, 3.5)

while True:
    racer_2.forward(speed)
    if racer_1.ycor() == 230:
        pen.write("Blue wins", font=("arial", 20, "bold"))
        break
    elif racer_2.ycor() == 230:
        pen.write("White wins", font=("arial", 20, "bold"))
        break

