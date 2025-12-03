import turtle
import random
class Polygon:
    def __init__(self):
         pass
        
    
    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)




# draw a polygon at a random location, orientation, color, and border line thickness
p = Polygon()
shape = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))

if shape == 1:
    num_sides = 3 # triangle, square, or pentagon
    for i in range (21):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif shape == 2:
    num_sides = 4
    for i in range (21):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
            # specify a reduction ratio to draw a smaller polygon inside the one above

            
elif shape == 3:
    num_sides = 5
    for i in range (21):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
  
elif shape == 4:
    for i in range (21):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)

elif shape == 5:
    for i in range (21):
            num_sides = (3)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
            for i in range (1, 3):
                # specify a reduction ratio to draw a smaller polygon inside the one above
                minus = str(f'0.0{i}')
                reduction_ratio = 0.618-float(minus)

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original

                p.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif shape == 6:
    for i in range (21):
            num_sides = (4)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
            for i in range (1, 3):
                # specify a reduction ratio to draw a smaller polygon inside the one above
                minus = str(f'0.0{i}')
                reduction_ratio = 0.618-float(minus)

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original

                p.draw_polygon(num_sides, size, orientation, location, color, border_size)

elif shape == 7:
    for i in range (21):
            num_sides = (5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
            for i in range (1, 3):
                # specify a reduction ratio to draw a smaller polygon inside the one above
                minus = str(f'0.0{i}')
                reduction_ratio = 0.618-float(minus)

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original

                p.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif shape == 8:
    for i in range (21):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
            for i in range (1, 3):
                # specify a reduction ratio to draw a smaller polygon inside the one above
                minus = str(f'0.0{i}')
                reduction_ratio = 0.618-float(minus)

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original

                p.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif shape == 9:
    for i in range (21):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = p.get_new_color()
            border_size = random.randint(1, 10)
            p.draw_polygon(num_sides, size, orientation, location, color, border_size)
            for i in range (random.randint(0,3)):
                # specify a reduction ratio to draw a smaller polygon inside the one above
                minus = str(f'0.0{i}')
                reduction_ratio = 0.618-float(minus)

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original

                p.draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()