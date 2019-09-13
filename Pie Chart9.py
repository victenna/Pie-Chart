import turtle
#import time
t=turtle.Turtle()
t.hideturtle()
position=(200,0)
t.left(90)
i=1
colors=['blue','red','violet','grey','pink','yellow','green','black']
for i in colors:
            print(i)
            t.goto(position)
            t.fillcolor(i)
            t.begin_fill()
            t.circle(200,45)
            position=t.position()
            print(position)
            t.goto(0,0)
            t.end_fill()

