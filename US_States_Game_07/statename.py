from turtle import Turtle
import math

ALIGNMENT   = "center"
FONT        = ("Courier",10,"normal")
X_COR_INIT  = -300
Y_COR_INIT  = 200
SPEED       = 5

class StateName(Turtle):
    def __init__(self,state_name,x_cor,y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(X_COR_INIT,Y_COR_INIT)
        self.state_name = state_name
        self.xcor_destination = x_cor
        self.ycor_destination = y_cor
        self.distance = compute_distance(self.xcor_destination,X_COR_INIT,self.ycor_destination,Y_COR_INIT)

    def distance(self):
        return compute_distance(self.xcor_destination,X_COR_INIT,self.ycor_destination,Y_COR_INIT)

    def speed(self):    
        self.y_speed = SPEED*(self.ycor_destination-Y_COR_INIT)/self.distance
        self.x_speed = SPEED*(self.xcor_destination-X_COR_INIT)/self.distance

    def move(self):
        x_speed = self.x_speed
        y_speed = self.y_speed
        new_xcor  = self.xcor()+x_speed
        new_ycor  = self.ycor()+y_speed
        self.goto(new_xcor,new_ycor)

    def check_position(self):
        distance_2_destination = compute_distance(self.xcor(),self.xcor_destination,self.ycor(),self.ycor_destination)
        distance_2_origine     = compute_distance(self.xcor(),X_COR_INIT,self.ycor(),Y_COR_INIT)
            
        # check if arriving to the right positions
        if (self.distance<distance_2_destination) or (self.distance<distance_2_origine):
            return True
        else:
            return False

    def write_statename(self):
        self.clear()
        self.write(self.state_name,align = ALIGNMENT, font= FONT)

def compute_distance(x,x1,y,y1):
    return math.sqrt((y1-y)*(y1-y)+(x1-x)*(x1-x))
