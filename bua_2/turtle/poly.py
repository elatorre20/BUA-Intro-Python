import turtle
import math

def draw_poly(t, points, color, fill):
    t.pencolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    if(fill):
        t.fillcolor(color)
        t.begin_fill()
    for i in points:
        t.goto(i)
    t.goto(points[0])
    if(fill):
        t.end_fill()
        
def draw_sprite(t, sprite):
    for i in sprite:
        poly = sprite[i]
        draw_poly(t, points = poly["points"], color = poly["color"], fill = poly["fill"])

def add_poly_to_sprite(sprite, points, color, fill):
    sprite[len(sprite)] = {"points": points, "color": color, "fill": fill}
    
turtle.clearscreen()
t = turtle.Turtle()
t.speed(0)
mondrian = {}
add_poly_to_sprite(mondrian, [(-200,-100),(-200,100),(200,100),(200,-100)], "black", True)
add_poly_to_sprite(mondrian, [(-220,10),(-220,120),(70,120),(70,10)], "yellow", True)
add_poly_to_sprite(mondrian, [(-180,-90),(-180,-10),(170,-10),(170,-90)], "blue", True)
add_poly_to_sprite(mondrian, [(90,10),(90,120),(220,120),(220,10)], "red", True)
draw_sprite(t, mondrian)