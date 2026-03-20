import turtle
import math

def draw_regular_poly(t, sides, length, color, position, angle, fill):
    t.penup()
    t.goto(position)
    t.pendown()
    t.pencolor(color)
    t.setheading(angle)
    internal_angle = 180-(180*(sides-2)/sides)
    if(fill):
        t.fillcolor(color)
        t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.right(internal_angle)
    if(fill):
        t.end_fill()

def draw_regular_sprite(t, sprite):
    for i in sprite:
        poly = sprite[i]
        draw_regular_poly(t, sides = poly["sides"], length = poly["length"], color = poly["color"], position = poly["position"], angle = poly["angle"], fill = poly["fill"])

def add_regular_poly_to_sprite(sprite, sides, length, color, position, angle, fill):
    sprite[len(sprite)] = {"sides": sides, "length": length, "color": color, "position": position, "angle": angle, "fill": fill}
    
turtle.clearscreen()
t = turtle.Turtle()
t.speed(0)
mondrian = {}
add_regular_poly_to_sprite(mondrian, 4, 140, "black", (-100,0), 45, True)
add_regular_poly_to_sprite(mondrian, 4, 60, "blue", (-5,0), 225, True)
add_regular_poly_to_sprite(mondrian, 4, 60, "red", (5,0), 45, True)
add_regular_poly_to_sprite(mondrian, 4, 60, "yellow", (0,5), 135, True)
add_regular_poly_to_sprite(mondrian, 4, 25, "blue", (-5,-(math.sqrt(1800))-4), 225, True)
add_regular_poly_to_sprite(mondrian, 4, 25, "red", (5,-(math.sqrt(1800))-4), 45, True)
add_regular_poly_to_sprite(mondrian, 4, 25, "yellow", (0,-(math.sqrt(1800))-1), 135, True)
add_regular_poly_to_sprite(mondrian, 4, 25, "white", (0,-(math.sqrt(1800))-7), 315, True)
draw_regular_sprite(t, mondrian)
    