from turtle import Turtle
import random
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed('fastest')
        self.x_speed = 2
        self.y_speed = 4
        
    
        
        
        
    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y =  self.ycor() + self.y_speed
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.y_speed *= -1
        
        
    def bounce_x(self):
        self.x_speed *= -1
        
    def reset(self):
        self.goto(0,0)
        self.y_speed= random.randint(-5,5)
        self.x_speed = 2
        self.bounce_x()
        
        
        
        
        
        
        
    


