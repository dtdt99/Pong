from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        self.paddle_parts = []
        self.create_paddle()
        
        
    def create_paddle(self):
        for i in range(6):
            new_part = Turtle()
            new_part.shape("square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(self.x,self.y)
            self.paddle_parts.append(new_part)
            self.y += 20
            
            
        
    
    def go_up(self):
        for part in self.paddle_parts:
            new_y = part.ycor() + 40
            part.goto(part.xcor(), new_y)
    

    def go_down(self):
        for part in self.paddle_parts:
            new_y = part.ycor() - 40
            part.goto(part.xcor(), new_y)
        
        
        
