from turtle import Turtle,Screen
import random

is_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color:")
print(user_bet)

colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-100,-60,-20,20,60,100]

turtle_list=[]

for i in range(6):
    
    turtle_obj=Turtle(shape="turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(x=-230,y=y_positions[i])
    turtle_list.append(turtle_obj)
  
if  user_bet:     #if user bet exists then start the game
    is_on=True
    
while is_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            winner_turtle=turtle.pencolor()
            if winner_turtle==user_bet:
                print(f"You've won! The {winner_turtle} turtle is winning.")
            else:
                print(f"You've lost! The {winner_turtle} turtle is winning.")
                
            is_on=False
            
        turtle.forward(random.randint(0,10))

screen.exitonclick()