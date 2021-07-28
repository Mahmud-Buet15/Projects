from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,270)
        self.hideturtle()        
        self.color("white")
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)
        
    def write_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)