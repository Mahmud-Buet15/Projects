from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()



snake=Snake()
food=Food()
scoreboard=Scoreboard()

#binds the fuction to the key to control the snake
screen.onkey(key="Up",fun=snake.move_up)  
screen.onkey(key="Down",fun=snake.move_down)
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)
    
  
game_is_on=True
while game_is_on:    
    screen.update()    #updating the screen with new positions of the segments
    time.sleep(.1)     #delaying the update
    
    #detecting collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_segment()
        scoreboard.write_score()
        
    #detect collision to wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
       
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
        
    
   
    snake.move()
    


screen.exitonclick()