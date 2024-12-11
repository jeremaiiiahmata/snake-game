from turtle import Turtle
import random

class Food(Turtle): #Inherits the turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.generate()

    def generate(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)

        self.goto(randomX, randomY)