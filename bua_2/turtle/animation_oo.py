import turtle
import math
import time

class polygon:
    
    def __init__(self, points = [], color = (255,0,0)):
        self.points = points
        self.color = color
        

class scene:
    
    def __init__(self, lighting = ):
        #set up screen
        self.screen = Turtle.screen()
        self.screen.colormode(255)
        #set up the turtle
        self.turtle = Turtle.turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.tracer(0)
        