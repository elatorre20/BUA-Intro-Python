import math
import turtle
import time

class Vector3:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def cross_product(self, b):
        c0 = (self.y * b.z) - (self.z * b.y)
        c1 = (self.z * b.x) - (self.x * b.z)
        c2 = (self.x * b.y) - (self.y * b.x)
        return Vector3(c0, c1, c2)
    
    def dot_product(self, b):
        return (self.x * b.x) + (self.y * b.y) + (self.z * b.z)
    
    def add(self, b):
        return Vector3(self.x + b.x, self.y + b.y, self.z + b.z)
    
    def __add__(self, b):
        return self.add(b)
    
    def subtract(self, b):
        return Vector3(self.x - b.x, self.y - b.y, self.z - b.z)
    
    def __sub__(self, b):
        return self.subtract(b)
    
    def mul(self, s):
        return Vector3(self.x * s, self.y * s, self.z * s)
    
    def __mul__(self, s):
        return self.mul(s)
    
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def get_normalized(self):
        magnitude = self.get_magnitude()
        if magnitude == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude)

class Polygon:
    
    def __init__(self, points, color = (255,0,0)):
        self.points = points
        self.color = color
    
    def translate(self, a):
        for i in range(len(self.points)):
            self.points[i] = self.points[i] + a
        
    def rotate(self, theta, axis):
        for i in range(len(self.points)):
            if(axis == 'x'):
                self.points[i] = Vector3(self.points[i].x, (self.points[i].y*math.cos(theta))-(self.points[i].z*math.sin(theta)), (self.points[i].y*math.sin(theta))+(self.points[i].z*math.cos(theta)))
            elif(axis == 'y'):
                self.points[i] = Vector3((self.points[i].x*math.cos(theta)) + (self.points[i].z*math.sin(theta)), self.points[i].y, -(self.points[i].x*math.sin(theta))+(self.points[i].z*math.cos(theta)))
            elif(axis == 'z'):
                self.points[i] = Vector3((self.points[i].x*math.cos(theta))-(self.points[i].y*math.sin(theta)), (self.points[i].x*math.sin(theta))+(self.points[i].y*math.cos(theta)), self.points[i].z)
        
    def scale(self, a):
        for i in range(len(self.points)):
            self.points[i] = Vector3(self.points[i].x * a.x, self.points[i].y * a.y, self.points[i].z * a.z)
        
    def mirror(self, a):
        for i in range(len(self.points)):
            b = Vector3(self.points[i].x, self.points[i].y, self.points[i].z)
            if(a.x != 0):
                b.x = self.points[i].x * -1
            if(a.y != 0):
                b.y = self.points[i].y * -1
            if(a.z != 0):
                b.z = self.points[i].z * -1
            self.points[i] = b
            
    def get_normal(self):
        a = self.points[1] - self.points[0]
        b = self.points[2] - self.points[1]
        return(a.cross_product(b).get_normalized())

class Mesh:
    
    def __init__(self, scene, polygons=[], offset=Vector3()):
        self.scene = scene
        self.polygons = polygons
        self.offset = Vector3()
        self.scene.meshes.append(self)
        self.translate(offset)
    
    def add_polygon(self, polygon):
        self.polygons.append(polygon)
        
    def translate(self, a):
        self.offset = self.offset + a
        for i in self.polygons:
            i.translate(a)
        
    def rotate(self, theta, axis):
        # shift to origin
        for i in self.polygons:
            i.translate(self.offset * -1)
        # rotate
        for i in self.polygons:
            i.rotate(theta, axis)
        # shift back
        for i in self.polygons:
            i.translate(self.offset)
                
    def scale(self, a):
        for i in self.polygons:
            i.scale(a)
        
    def mirror(self, a):
        for i in self.polygons:
            i.mirror(a)
            
    def draw(self):
        for i in self.polygons:
            normal = i.get_normal()
            color = i.color
            color = (color[0]*self.scene.ambient,color[1]*self.scene.ambient,color[2]*self.scene.ambient)
            directionalCosine = self.scene.directional.dot_product(normal)
            color = (color[0]*directionalCosine,color[1]*directionalCosine,color[2]*directionalCosine)
            color = (max(color[0],0),max(color[1],0),max(color[2],0)) 
            color = (min(color[0],255),min(color[1],255),min(color[2],255))
            color = (int(color[0]),int(color[1]),int(color[2]))
            self.scene.turtle.color(color[0], color[1], color[2])
            self.scene.turtle.pendown()
            self.scene.turtle.begin_fill()
            for j in i.points:
                self.scene.turtle.goto(j.x,j.y)
            self.scene.turtle.goto(i.points[0].x,i.points[0].y)
            self.scene.turtle.end_fill()
            self.scene.turtle.penup()

class Scene:
    
    def __init__(self, ambient = 0.9, directional = Vector3(1,0,1)):
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        turtle.tracer(0)
        self.ambient = 0.9
        self.directional = directional.get_normalized()
        self.meshes = []
        
    def update(self):
        self.turtle.clear()
        for i in self.meshes:
            i.draw()
        turtle.update()
        
canv = Scene()
a = Vector3(0,57,0)
b = Vector3(-50,-28,-0)
c = Vector3(50,-28,0)
tri = Polygon([a,b,c])
m = Mesh(canv,[tri], Vector3(100,100,0))
while(True):
    m.rotate(math.pi/64,'x')
    canv.update()
    time.sleep(0.03)