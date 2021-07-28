from turtle import Screen,Turtle


STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90   #North
DOWN=270 #South
LEFT=180 #West
RIGHT=0 #East


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
        
        
    def create_snake(self):        
        #A snake with 3 squares
        for position in STARTING_POSITION:
            self.add_segment(position)
            
            
    def add_segment(self,position):
        new_segment=Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend_segment(self):
        self.add_segment(self.segments[-1].position())
    
            
    def move(self):    
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()      #finding the x co-ordinate of a segment
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)    #one segment will goto the the position of the segment before it
        
        self.head.forward(MOVE_DISTANCE)
        
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading()!=RIGHT:
             self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
        

  