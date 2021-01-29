import random
import turtle as t


t.colormode(255)

nonso = t.Turtle()
nonso.penup()
nonso.hideturtle()
color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

nonso.setheading(225)
nonso.forward(300)
nonso.setheading(0)
no_of_dots = 100

for count_dot in range(1, no_of_dots + 1):
    nonso.dot(20, random.choice(color_list))
    nonso.forward(50)

    if count_dot % 10 == 0:
        nonso.setheading(90)
        nonso.forward(50)
        nonso.setheading(180)
        nonso.forward(500)
        nonso.setheading(0)

screen = t.Screen()
screen.exitonclick()