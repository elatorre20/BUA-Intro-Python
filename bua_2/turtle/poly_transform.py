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
        
def translate_poly(points, x, y):
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        points[i] = (x0 + x, y0 + y)
        
def rotate_poly(points, theta):
    #offset = points[0]
    #translate_poly(points, -1*offset[0], -1*offset[1])
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        points[i] = ((x0*math.cos(theta))-(y0*math.sin(theta)), (x0*math.sin(theta))+(y0*math.cos(theta)))
    #translate_poly(points, offset[0], offset[1])
        
def scale_poly(points, x, y):
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        points[i] = (x0 * x, y0 * y)
        
def translate_sprite(sprite, x, y):
    for i in sprite:
        translate_poly(sprite[i]["points"], x, y)
        
def rotate_sprite(sprite, theta):
    for i in sprite:
        rotate_poly(sprite[i]["points"], theta)
        
def scale_sprite(sprite, x, y):
    for i in sprite:
        scale_poly(sprite[i]["points"], x, y)
        
def draw_sprite(t, sprite):
    for i in sprite:
        poly = sprite[i]
        draw_poly(t, points = poly["points"], color = poly["color"], fill = poly["fill"])

def add_poly_to_sprite(sprite, points, color, fill):
    sprite[len(sprite)] = {"points": points, "color": color, "fill": fill}
    
turtle.clearscreen()
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
mondrian = {}
add_poly_to_sprite(mondrian, [(-200,-100),(-200,100),(200,100),(200,-100)], "black", True)
add_poly_to_sprite(mondrian, [(-220,10),(-220,120),(70,120),(70,10)], "yellow", True)
add_poly_to_sprite(mondrian, [(-180,-90),(-180,-10),(170,-10),(170,-90)], "blue", True)
add_poly_to_sprite(mondrian, [(90,10),(90,120),(220,120),(220,10)], "red", True)
draw_sprite(t, mondrian)
scale_sprite(mondrian, 0.25, 0.5)
rotate_sprite(mondrian, math.pi/4)
translate_sprite(mondrian, 250, 300)
draw_sprite(t, mondrian)