import turtle
import math
import time



def vec3_cross_product(a,b):
    c0 = (a[1]*b[2]) - (a[2]*b[1])
    c1 = (a[2]*b[0]) - (a[0]*b[2])
    c2 = (a[0]*b[1]) - (a[1]*b[0])
    return (c0,c1,c2)

def vec3_dot_product(a,b):
    return(a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])

def vec3_sub(a,b):
    return (a[0]-b[0],a[1]-b[1],a[2]-b[2])

def vec3_normalize(a):
    magnitude=math.sqrt((a[0]*a[0])+(a[1]*a[1])+(a[2]*a[2]))
    return (a[0]/magnitude,a[1]/magnitude,a[2]/magnitude)
    
def get_poly_normal(points):
    a = vec3_sub(points[1], points[0])
    b = vec3_sub(points[2], points[1])
    return(vec3_normalize(vec3_cross_product(a,b)))

ambient=1.0 #magnitude applied to all polygons, simulates ambient light
directional=vec3_normalize((0,-1,-1))#magnitude-1 vector representing a directional source
def draw_poly(t, points, color, fill):
    #calculate the lighting
    color = (color[0]*ambient, color[1]*ambient, color[2]*ambient) #apply ambient lighting
    lighting_cos = vec3_dot_product(directional, get_poly_normal(points))
    color = (color[0]*lighting_cos,color[1]*lighting_cos,color[2]*lighting_cos)
    color = (max(color[0],0),max(color[1],0),max(color[2],0)) 
    color = (min(color[0],255),min(color[1],255),min(color[2],255))#ensure that lighting is within range
    color = (int(color[0]),int(color[1]),int(color[2]))
    #start drawing the polygon
    t.pencolor(color)
    t.penup()
    start = (points[0][0], points[0][1]) 
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

def tetrahedron(dim, colors=[], x=0, y=0):
    if colors == []:
        colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
    tetrahedron = {}
    h = dim/math.sqrt(2)
    add_poly_to_sprite(tetrahedron, [( x, y, h),( dim/2+x,-dim/2+y,0),(-dim/2+x,-dim/2+y,0)], colors[0], True)
    add_poly_to_sprite(tetrahedron, [( x, y, h),( dim/2+x, dim/2+y,0),( dim/2+x,-dim/2+y,0)], colors[1], True)
    add_poly_to_sprite(tetrahedron, [( x, y, h),(-dim/2+x, dim/2+y,0),( dim/2+x, dim/2+y,0)], colors[2], True)
    add_poly_to_sprite(tetrahedron, [(-dim/2+x,-dim/2+y,0),( dim/2+x,-dim/2+y,0),( dim/2+x, dim/2+y,0),(-dim/2+x, dim/2+y,0)], colors[3], True)
    return tetrahedron

def cube(dim, colors=[], x=0, y=0):
    if colors == []:
        colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
    cube = {}
    add_poly_to_sprite(cube, [( dim/2+x,dim/2+y,dim/2),(dim/2+x,-dim/2+y,dim/2),(-dim/2+x,-dim/2+y,dim/2),(-dim/2+x,dim/2+y,dim/2)], colors[0], True)
    add_poly_to_sprite(cube, [(dim/2+x,dim/2+y,dim/2),(-dim/2+x,dim/2+y,dim/2),(-dim/2+x,dim/2+y,-dim/2),(dim/2+x,dim/2+y,-dim/2)], colors[1], True)
    add_poly_to_sprite(cube, [(-dim/2+x,dim/2+y,dim/2),(-dim/2+x,-dim/2+y,dim/2),(-dim/2+x,-dim/2+y,-dim/2),(-dim/2+x,dim/2+y,-dim/2)], colors[2], True)
    add_poly_to_sprite(cube, [(dim/2+x,dim/2+y,dim/2),(dim/2+x,dim/2+y,-dim/2),(dim/2+x,-dim/2+y,-dim/2),(dim/2+x,-dim/2+y,dim/2)], colors[3], True)
    add_poly_to_sprite(cube, [(dim/2+x,-dim/2+y,dim/2),(dim/2+x,-dim/2+y,-dim/2),(-dim/2+x,-dim/2+y,-dim/2),(-dim/2+x,-dim/2+y,dim/2)], colors[4], True)
    add_poly_to_sprite(cube, [(-dim/2+x,-dim/2+y,-dim/2),(dim/2+x,-dim/2+y,-dim/2),(dim/2+x,dim/2+y,-dim/2),(-dim/2+x,dim/2+y,-dim/2)], colors[5], True)
    return cube

def octahedron(dim, colors=[], x=0, y=0):
    if colors == []:
        colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,128,0),(128,0,255)]
    octahedron = {}
    r = dim/2
    add_poly_to_sprite(octahedron, [( x, y, r),( r+x, y,0),( y+x, r+y,0)], colors[0], True)
    add_poly_to_sprite(octahedron, [( x, y, r),( y+x, r+y,0),(-r+x, y,0)], colors[1], True)
    add_poly_to_sprite(octahedron, [( x, y, r),(-r+x, y,0),( y+x,-r+y,0)], colors[2], True)
    add_poly_to_sprite(octahedron, [( x, y, r),( y+x,-r+y,0),( r+x, y,0)], colors[3], True)
    add_poly_to_sprite(octahedron, [( x, y,-r),( y+x, r+y,0),( r+x, y,0)], colors[4], True)
    add_poly_to_sprite(octahedron, [( x, y,-r),(-r+x, y,0),( y+x, r+y,0)], colors[5], True)
    add_poly_to_sprite(octahedron, [( x, y,-r),( y+x,-r+y,0),(-r+x, y,0)], colors[6], True)
    add_poly_to_sprite(octahedron, [( x, y,-r),( r+x, y,0),( y+x,-r+y,0)], colors[7], True)
    return octahedron

screen = turtle.Screen()
screen.clear()
screen.colormode(255)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0)
tetrahedron = tetrahedron(50,x=-100,y=0)
cube = cube(50)
octahedron = octahedron(50,x=100,y=0)
rotate_sprite(tetrahedron, math.pi/3, 'x')
rotate_sprite(cube, math.pi/3, 'y')
rotate_sprite(octahedron, math.pi/3, 'x')
while(True):
    t.clear()
    rotate_sprite(tetrahedron, math.pi/64, 'y')
    rotate_sprite(cube, math.pi/64, 'x')
    rotate_sprite(octahedron, math.pi/64, 'y')
    draw_sprite(t, tetrahedron)
    draw_sprite(t, cube)
    draw_sprite(t, octahedron)
    turtle.update()
    time.sleep(1/30)
