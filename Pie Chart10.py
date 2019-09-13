import turtle
t=turtle.Turtle()
turtle.bgcolor('gold')
t1=turtle.Turtle()
t1.hideturtle()
t.hideturtle()
position=(200,0)
t.left(90)
i=1
angle=[75.6,57.6,68.4,57.6,28.8,36,25.2,10.8]
angle1=[21,16,19,16,8,10,7,3]
clr=['white','silver','black','grey','blue','red','brown','light green']    
for i in range(8):
    t.up()
    t.goto(position)
    t.down()
    t.color(clr[i])
    t.begin_fill()
    t1.up()
    t1.color(clr[i])
    t1.goto(250,-30*i)
    t1.down()
    t1.write(str(angle1[i])+'%',font=('Arial',20,'bold'))
    t.circle(200,angle[i])
    position=t.position()
    t.goto(0,0)
    t.end_fill()
t1.up()
t1.goto(-300,270)
t1.down()
t1.color('blue')
t1.write('Car Colour Popularity %, North America',font=('Arial',25,'bold')) 
turtle.exitonclick()
