# import colorgram
from turtle import Turtle, Screen
from random import choice

# Get colors
# colors = colorgram.extract('image.jpg', 30)
# rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))

color_list = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56)]

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.setpos(-250, -200)

y = -200

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, choice(color_list))
        turtle.forward(50)
    y += 50
    turtle.setx(-250)
    turtle.sety(y)


screen.exitonclick()
