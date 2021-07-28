import colorgram
import turtle as t
import random

#color extraction from an image
colors=colorgram.extract("spot paining.jpg", 30)
color_list=[]
for i in range(len(colors)):
    r=colors[i].rgb[0]
    g=colors[i].rgb[1]
    b=colors[i].rgb[2]
    color_list.append((r,g,b))

t.colormode(255)   #this allows to use random rgb color
turtle_obj=t.Turtle()
screen=t.Screen()


turtle_obj.hideturtle()
turtle_obj.penup()
turtle_obj.speed(0)
x=-200
y=-200

for i in range(10):
    turtle_obj.setpos((x,y))
    for _ in range(10):
        turtle_obj.dot(20,random.choice(color_list))
        turtle_obj.forward(50)
    y+=50
    
    





screen.exitonclick()


    
        
        
