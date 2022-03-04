#####Turtle Intro######

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()

tim.speed(1)
colors = ["CadetBlue", "DeepPink","cyan3", "DarkOrange", "Wheat", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_size_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_size_n)

# for _ in range(3):
#     tim.color("CadetBlue")
#     tim.forward(100)
#     tim.right(120)
# for _ in range(4):
#     tim.color("DeepPink")
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(5):
#     tim.color("cyan3")
#     tim.forward(100)
#     tim.right(72)
# for _ in range(6):
#     tim.color("DarkOrange")
#     tim.forward(100)
#     tim.right(60)
# for _ in range(7):
#     tim.color("bisque2")
#     tim.forward(100)
#     tim.right(51.4)
# for _ in range(8):
#     tim.color("DarkSlateGrey")
#     tim.forward(100)
#     tim.right(45)
# for _ in range(9):
#     tim.color("DarkOrchid")
#     tim.forward(100)
#     tim.right(40)
screen = Screen()
