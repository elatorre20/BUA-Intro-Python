import turtle

def draw_regular_polygon(t, sides, length, color, position, angle, fill):
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

points = [(100,100), (200,200), ...]

def draw_polygon(t, points, color, fill):
        
t = turtle.Turtle()
draw_regular_polygon(t, 4, 30, "red", (100,100),45, True)
