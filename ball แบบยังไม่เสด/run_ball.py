import turtle
import ball
import random

num_balls = 5
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
print(canvas_width, canvas_height)
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
xpos = []
ypos = []
vx = []
vy = []
ball_color = []

# create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
for i in range(num_balls):
    xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
    ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
    vx.append(10*random.uniform(-1.0, 1.0))
    vy.append(10*random.uniform(-1.0, 1.0))
    ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def draw_border():
    turtle.penup()
    turtle.goto(-canvas_width, -canvas_height)
    turtle.pensize(10)
    turtle.pendown()
    turtle.color((0, 0, 0))
    for i in range(2):
        turtle.forward(2*canvas_width)
        turtle.left(90)
        turtle.forward(2*canvas_height)
        turtle.left(90)

import turtle

def init(my_turtle, color):
    turtle.speed(0)
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.colormode(255)
    
    my_turtle.color(color)
    my_turtle.penup()
    my_turtle.setheading(0)
    my_turtle.goto(0, 0)
    my_turtle.pensize(10)


def draw(my_turtle, digit):
    if digit == 0:
        my_turtle.goto(-50, 100)
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.penup()

    if digit == 1:
        my_turtle.goto(50, 100)
        my_turtle.pendown()
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.penup()

    if digit == 2:
        my_turtle.goto(-50, 100)
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.penup()

    if digit == 3:
        my_turtle.goto(-50, 100)
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.forward(-100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.left(90)
        my_turtle.penup()

    if digit == 4:
        my_turtle.goto(-50, 100)
        my_turtle.pendown()
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.forward(-100)
        my_turtle.forward(-100)
        my_turtle.right(90)
        my_turtle.penup()

    if digit == 5:
        my_turtle.goto(-50, 100)
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.forward(-100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.left(90)
        my_turtle.penup()

    if digit == 6:
        draw(my_turtle, 5)
        my_turtle.goto(-50, 0)
        my_turtle.pendown()
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.penup()
    
    if digit == 7:
        my_turtle.goto(-50, 100)
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.forward(-100)
        draw(my_turtle, 1)

    if digit == 8:
        draw(my_turtle, 0)
        my_turtle.goto(-50, 0)
        my_turtle.pendown()
        my_turtle.forward(100)
        my_turtle.penup()

    if digit == 9:
        draw(my_turtle, 5)
        my_turtle.goto(50, 100)
        my_turtle.pendown()
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.penup()

def clear(my_turtle):
    my_turtle.clear()

def my_delay(dt):
    import time
    start =  time.time()
    while time.time() - start < dt:
        pass

Tom = turtle.Turtle()
tom_color = (255, 0, 0)
init(Tom, tom_color)
delay_in_seconds = 0.2



dt = 0.2 # time step
while (True):
    turtle.clear()
    draw_border()
    for i in range(num_balls):
        ball.draw_ball(ball_color[i], ball_radius, xpos[i], ypos[i])
        ball.move_ball(i, xpos, ypos, vx, vy, dt)
        ball.update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
        clear(Tom)
        draw(Tom, i)
        my_delay(delay_in_seconds)
        turtle.update()
    turtle.update()



# hold the window; close it by clicking the window close 'x' mark
turtle.done()
