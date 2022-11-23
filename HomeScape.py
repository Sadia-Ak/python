# Build your own home 
# Student: Sadia Akther
#  Course Name: DSCI-006
#  Date: Nov. 8, 2020
#  Description of Program: In this assignemnt, we given to create a graphics design of a house. 

import turtle
turtle.setup(800,500)

turtle.speed(5)
#grass
turtle.bgcolor('#007500')

#sky
turtle.penup()
turtle.goto(-400,-90)
turtle.pendown()
turtle.color('#0096FF')

turtle.begin_fill()

for i in range(2):
    turtle.fd(800)
    turtle.lt(90)
    turtle.fd(500)
    turtle.lt(90)
turtle.end_fill() 

#cloud
turtle.penup()
turtle.goto(155,155)
turtle.pendown()
turtle.color('#FFFFFF')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(170,195)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(140,180)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(185,155)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#Sun
turtle.penup()
turtle.goto(-200,80)
turtle.pendown()
turtle.pensize(5)
turtle.speed(5)

turtle.color('#FFD700')
turtle.begin_fill()
turtle.begin_fill
turtle.circle(50)
turtle.end_fill()

for i in range(18):
    turtle.rt(90)
    turtle.fd(40)
    turtle.bk(40)
    turtle.lt(90)
    turtle.circle(50,20)
    
#house 
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.color('#000000','#FFFFFF')
turtle.begin_fill()

for i in range(4):
    turtle.fd(170)
    turtle.lt(90)
turtle.end_fill()

# Roof 
turtle.penup()
turtle.goto(-114,70)
turtle.pendown()
turtle.color('#000000')
turtle.begin_fill()
for i in range(3):
    turtle.fd(200)
    turtle.lt(120)
turtle.end_fill()

# window 1
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color('#000000','#FFFFFF')
turtle.begin_fill()

for i in range(4):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()

# cross HR
turtle.penup()
turtle.goto(0,25)
turtle.pendown()
turtle.color('#000000')
turtle.fd(50)
# VR
turtle.penup()
turtle.goto(25,0)
turtle.pendown()
turtle.lt(90)
turtle.fd(50)

# window 2
turtle.penup()
turtle.goto(-80,0)
turtle.pendown()
turtle.rt(90)
turtle.color('#000000','#FFFFFF')
turtle.begin_fill()

for i in range(4):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()

# cross HR
turtle.penup()
turtle.goto(-80,25)
turtle.pendown()
turtle.color('#000000')
turtle.fd(50)
# VR
turtle.penup()
turtle.goto(-55,0)
turtle.pendown()
turtle.lt(90)
turtle.fd(50)

# Door
turtle.penup()
turtle.goto(-40,-97)
turtle.pendown()
turtle.rt(90)
turtle.color('#000000','#FF0000')
turtle.begin_fill()

for i in range(2):
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(80)
    turtle.lt(90)
turtle.end_fill()



#Flowers
turtle.penup()
turtle.goto(-155,-155)
turtle.pendown()
turtle.color('#FFC0CB')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-170,-145)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-135,-145)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Flowers 2
turtle.penup()
turtle.goto(155,-155)
turtle.pendown()
turtle.color('#800080')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(170,-140)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(135,-145)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Flowers 3
turtle.penup()
turtle.goto(-220,-220)
turtle.pendown()
turtle.color('#8d76c5')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-240,-225)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-210,-235)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#Flowers 3
turtle.penup()
turtle.goto(220,-220)
turtle.pendown()
turtle.color('#76b6c5')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(240,-225)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(210,-235)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.done()