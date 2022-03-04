#####Turtle Intro######

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")


colors = ["CadetBlue", "DeepPink", "cyan3", "DarkOrange", "Wheat", "SeaGreen", "Black", "Green"]
directions = [0, 90, 180, 270]
for i in range(200):
    tim.color(random.choice(colors))
    tim.fd(20)
    tim.seth(random.choice(directions))




t.Screen()
