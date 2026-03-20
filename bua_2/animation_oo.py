import math

class vector3:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def cross_product(self, b):
        c0 = (self.y * b.z) - (self.z * b.y)
        c1 = (self.z * b.x) - (self.x * b.z)
        c2 = (self.x * b.y) - (self.y * b.x)
        return vector3(c0, c1, c2)
    
    def dot_product(self, b):
        return (self.x * b.x) + (self.y * b.y) + (self.z * b.z)
    
    def add(self, b):
        return vector3(self.x + b.x, self.y + b.y, self.z + b.z)
    
    def __add__(self, b):
        return self.add(b)
    
    def subtract(self, b):
        return vector3(self.x - b.x, self.y - b.y, self.z - b.z)
    
    def __sub__(self, b):
        return self.subtract(b)
    
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def get_normal(self):
        magnitude = self.get_magnitude()
        if magnitude == 0:
            return vector3(0, 0, 0)
        return vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude)

class polygon:
    
    def __init__(self, points, color = (255,0,0)):
        self.points = points
        self.color = color
    
    def translate(self, a):
        for i in range(len(self.points)):
            self.points[i] = self.points[i] + a
        
    def rotate(self, theta, axis):
        for i in range(len(self.points)):
            if(axis == 'x'):
                self.points[i] = vector3(self.points[i].x, (self.points[i].y*math.cos(theta))-(self.points[i].z*math.sin(theta)), (self.points[i].y*math.sin(theta))+(self.points[i].z*math.cos(theta)))
            elif(axis == 'y'):
                self.points[i] = vector3((self.points[i].x*math.cos(theta)) + (self.points[i].z*math.sin(theta)), self.points[i].y, -(self.points[i].x*math.sin(theta))+(self.points[i].z*math.cos(theta)))
            elif(axis == 'z'):
                self.points[i] = vector3((self.points[i].x*math.cos(theta))-(self.points[i].y*math.sin(theta)), (self.points[i].x*math.sin(theta))+(self.points[i].y*math.cos(theta)), self.points[i].z)
        
    def scale(self, a):
        for i in range(len(self.points)):
            self.points[i] = vector3(self.points[i].x * a.x, self.points[i].y * a.y, self.points[i].z * a.z)
        
    def mirror(self, a):
        for i in range(len(self.points)):
            b = vector3(self.points[i].x, self.points[i].y, self.points[i].z)
            if(a.x != 0):
                b.x = self.points[i].x * -1
            if(a.y != 0):
                b.y = self.points[i].y * -1
            if(a.z != 0):
                b.z = self.points[i].z * -1
            self.points[i] = b

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
        