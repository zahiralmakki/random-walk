# 100 Days of Code
# Day 18: lec 133
# Trutle Challenge 4: Generate a Random Walk
# 9 Jan 2025, Thrusday

import random
from turtle import Turtle


zug = Turtle()

colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
zug.pensize(15)
zug.speed("fastest")


for _ in range(200):
    zug.color(random.choice(colors))
    zug.forward(30)
    zug.setheading(random.choice(directions))
