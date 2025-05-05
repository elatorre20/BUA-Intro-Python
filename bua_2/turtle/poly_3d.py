import turtle
import math

def draw_poly(t, points, color, fill):
    t.pencolor(color)
    t.penup()
    start = (points[0][0], points[0][1]) #extract the x,y dimensions
    t.goto(start)
    t.pendown()
    if(fill):
        t.fillcolor(color)
        t.begin_fill()
    for i in points:
        next_point = (i[0], i[1])
        t.goto(next_point)
    t.goto(start)
    if(fill):
        t.end_fill()
        
def translate_poly(points, x, y, z):
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        z0 = points[i][2]
        points[i] = (x0 + x, y0 + y, z0 + z)
        
def rotate_poly(points, theta, axis):
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        z0 = points[i][2]
        if(axis == 'x'):
            points[i] = (x0, (y0*math.cos(theta))-(z0*math.sin(theta)), (y0*math.sin(theta))+(z0*math.cos(theta)))
        if(axis == 'y'):
            points[i] = ((x0*math.cos(theta)) + (z0*math.sin(theta)), y0, -(x0*math.sin(theta))+(z0*math.cos(theta)))
        if(axis == 'z'):
            points[i] = ((x0*math.cos(theta))-(y0*math.sin(theta)), (x0*math.sin(theta))+(y0*math.cos(theta)), z0)
        
def scale_poly(points, x, y, z):
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        z0 = points[i][2]
        points[i] = (x0 * x, y0 * y, z0 * z)
        
def mirror_poly(points, x, y, z):
    for i in range(len(points)):
        x1 = points[i][0]
        y1 = points[i][1]
        z1 = points[i][2]
        if(x):
            x1 = x1 * -1
        if(y):
            y1 = y1 * -1
        if(z):
            z1 = z1 * -1
        points[i] = (x1, y1, z1)
        
def translate_sprite(sprite, x, y, z):
    for i in sprite:
        translate_poly(sprite[i]["points"], x, y, z)
        
def rotate_sprite(sprite, theta, axis):
    for i in sprite:
        rotate_poly(sprite[i]["points"], theta, axis)
        
def scale_sprite(sprite, x, y, z):
    for i in sprite:
        scale_poly(sprite[i]["points"], x, y, z)
        
def get_zmin(poly):
    zmin = poly["points"][0][2]
    for i in poly["points"]:
        if i[2] > zmin:
            zmin = i[2]
    return zmin
        
def draw_sprite(t, sprite):
    polygons = list(sprite.values())
    polygons = sorted(polygons, key = lambda x: get_zmin(x))
    for i in polygons:
        draw_poly(t, points = i["points"], color = i["color"], fill = i["fill"])

def add_poly_to_sprite(sprite, points, color, fill):
    sprite[len(sprite)] = {"points": points, "color": color, "fill": fill}
    
turtle.clearscreen()
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
cube = {}
add_poly_to_sprite(cube, [( 100,100,100),(-100,100,100),(-100,-100,100),(100,-100,100)], "red", True)
add_poly_to_sprite(cube, [(100,100,100),(-100,100,100),(-100,100,-100),(100,100,-100)], "green", True)
add_poly_to_sprite(cube, [(-100,100,100),(-100,100,-100),(-100,-100,-100),(-100,-100,100)], "blue", True)
add_poly_to_sprite(cube, [(100,100,100),(100,-100,100),(100,-100,-100),(100,100,-100)], "cyan", True)
add_poly_to_sprite(cube, [(100,-100,100),(-100,-100,100),(-100,-100,-100),(100,-100,-100)], "yellow", True)
add_poly_to_sprite(cube, [(-100,-100,-100),(100,-100,-100),(100,100,-100),(-100,100,-100)], "magenta", True)
scale_sprite(cube, 0.25, 0.25, 0.25)
rotate_sprite(cube, math.pi/4, 'y')
rotate_sprite(cube, math.pi/4, 'x')
draw_sprite(t, cube)
rotate_sprite(cube, math.pi/3, 'x')
rotate_sprite(cube, math.pi/3, 'y')
rotate_sprite(cube, math.pi/3, 'z')
translate_sprite(cube, 200, 200, 0)
draw_sprite(t, cube)
rotate_sprite(cube, math.pi/3, 'x')
rotate_sprite(cube, math.pi/3, 'y')
rotate_sprite(cube, math.pi/3, 'z')
translate_sprite(cube, -200, -25, 0)
draw_sprite(t, cube)
rotate_sprite(cube, math.pi/3, 'x')
rotate_sprite(cube, math.pi/3, 'y')
rotate_sprite(cube, math.pi/3, 'z')
translate_sprite(cube, -75, -250, 0)
draw_sprite(t, cube)
rotate_sprite(cube, math.pi/3, 'x')
rotate_sprite(cube, math.pi/3, 'y')
rotate_sprite(cube, math.pi/3, 'z')
translate_sprite(cube, 50, 50, 0)
draw_sprite(t, cube)