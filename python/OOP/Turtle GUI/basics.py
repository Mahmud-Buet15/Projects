# from turtle import Turtle,Screen
# import random

# timmy_the_tutle=Turtle()
# timmy_the_tutle.shape("turtle")
# timmy_the_tutle.color("cyan4")

# timmy_the_tutle.forward(100)
# timmy_the_tutle.right(90)

# timmy_the_tutle.forward(100)


# turtle_obj=Turtle()



# #making a square
# turtle_obj.forward(100)
# turtle_obj.right(90)
# turtle_obj.forward(100)
# turtle_obj.right(90)
# turtle_obj.forward(100)
# turtle_obj.right(90)
# turtle_obj.forward(100)

# #making a dashed line

# for i in range(30):
#     turtle_obj.forward(5)
#     turtle_obj.penup()
#     turtle_obj.forward(5)
#     turtle_obj.pendown()
#     turtle_obj.forward(5)

#making triangle,square,pentagon,hexagon,heptagon,octagon,nonagon,decagon

# side=3
# total_angle=360
# turtle_colors=["forest green","blue","maroon","medium slate blue","gold","dim gray"]
# while side<11:
    
#     angle=total_angle/side
#     turtle_obj.color(random.choice(turtle_colors))
#     for i in range(side):
        
#         turtle_obj.forward(100)
#         turtle_obj.right(angle)
        
#     # for i in range(side):
        
#     #     turtle_obj.forward(100)
#     #     turtle_obj.left(angle)
        
#     # for i in range(side):
#     #     turtle_obj.left(angle)
#     #     turtle_obj.forward(100)
        
#     side+=1
    
    
    
# #random walks

# turtle_obj=Turtle()
# turtle_obj.pensize(10)
# turtle_obj.speed(8)

# turtle_colors=["forest green","blue","coral","maroon","medium slate blue","gold","dim gray"]

# # for i in range(200):
# #     turtle_obj.color(random.choice(turtle_colors))
# #     x=random.choice([1,2,3,4])
# #     if x==1:
# #         turtle_obj.forward(30)
# #     elif x==2:
# #         turtle_obj.backward(30)
# #     elif x==3:
# #         turtle_obj.right(90)
# #     elif x==4:
# #         turtle_obj.left(90)

# directions=[0,90,180,270]

# for i in range(200):
#     turtle_obj.forward(30)
#     turtle_obj.color(random.choice(turtle_colors))
#     turtle_obj.setheading(random.choice(directions))
    









# screen=Screen()
# screen.exitonclick()




#random color generator

import turtle as t
import random

# turtle_obj=t.Turtle()
# turtle_obj.pensize(10)
# turtle_obj.speed(8)

# t.colormode(255)

# def random_color():
#     r=random.randint(1,255)
#     g=random.randint(1,255)
#     b=random.randint(1,255)
#     return (r,g,b)

# directions=[0,90,180,270]

# for i in range(200):
#     turtle_obj.forward(30)
#     turtle_obj.color(random_color())
#     turtle_obj.setheading(random.choice(directions))


#making a spirograph

turtle_obj=t.Turtle()
t.colormode(255)
turtle_obj.speed(0)
angle=10

def random_color():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)

# while angle<370:
#     turtle_obj.color(random_color())
#     turtle_obj.circle(120)
#     turtle_obj.right(5)
#     angle+=5

def make_spirograph(angle):
    for _ in range(360//angle):
        turtle_obj.color(random_color())
        turtle_obj.circle(120)
        turtle_obj.setheading(turtle_obj.heading()+angle)
    
make_spirograph(5)
    

    








screen=t.Screen()
screen.exitonclick()
