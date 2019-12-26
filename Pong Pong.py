import turtle

#screen setup
pc=turtle.Screen()
pc.title("Pong Pong by ANAND")
pc.bgcolor("green")
pc.setup(width=800,height=500)
pc.tracer(0)

#Score of paddles A & B
sc_a=0
sc_b=0

#Setup of paddle A
pd_a=turtle.Turtle()
pd_a.speed(0)
pd_a.shape("square")
pd_a.color("black")
pd_a.shapesize(stretch_wid=5,stretch_len=1)
pd_a.penup()
pd_a.goto(-350,0)

#Setup of paddle B
pd_b=turtle.Turtle()
pd_b.speed(0)
pd_b.shape("square")
pd_b.color("black")
pd_b.shapesize(stretch_wid=5,stretch_len=1)
pd_b.penup()
pd_b.goto(350,0)

#Setup of ball
ball=turtle.Turtle()
ball.speed(0)
ball.color("black")
ball.shape("square")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

#writing
wr=turtle.Turtle()
wr.speed(0)  
wr.color("blue")
wr.shape("turtle")
wr.penup()
wr.hideturtle()
wr.goto(0,220)
wr.write("Player A = 0 AND Player B = 0",align="center",font=("arial",20,"normal"))

#Functions:

def paddle_a_up():
    y=pd_a.ycor()
    y+=5
    pd_a.sety(y)

def paddle_a_down():
    y=pd_a.ycor()
    y-=5
    pd_a.sety(y)

def paddle_b_up():
    y=pd_b.ycor()
    y+=5
    pd_b.sety(y)

def paddle_b_down():
    y=pd_b.ycor()
    y-=5
    pd_b.sety(y)

#Keyboard Settings
pc.listen()
pc.onkeypress(paddle_a_up,"w")
pc.onkeypress(paddle_a_down,"s")
pc.onkeypress(paddle_b_up,"Up")
pc.onkeypress(paddle_b_down,"Down")


while(True):
    pc.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border Setup
    #For top and bottom
    if (ball.ycor()>240):
        ball.sety(240)
        ball.dy*=-1
        

    if (ball.ycor()<-240):
        ball.sety(-240)
        ball.dy*=-1
        
    if(ball.xcor()>390):
        sc_a+=1
        wr.clear()
        wr.write("Player A = {} AND Player B = {}".format(sc_a,sc_b),align="center",font=("arial",20,"normal"))
        ball.goto(0,0)
        ball.dx*=-1

    if(ball.xcor()<-390):
        sc_b+=1
        wr.clear()
        wr.write("Player A = {} AND Player B = {}".format(sc_a,sc_b),align="center",font=("arial",20,"normal"))
        ball.goto(0,0)
        ball.dx*=-1

    if(ball.xcor()==-330 and ball.ycor()<pd_a.ycor()+60 and ball.ycor()>pd_a.ycor()-60):
        ball.dx*=-1

    elif(ball.xcor()==330 and ball.ycor()<pd_b.ycor()+60 and ball.ycor()>pd_b.ycor()-60):
        ball.dx*=-1

    if(ball.xcor()<-330 and ball.xcor()>-370 and (ball.ycor()==pd_a.ycor()+60 or ball.ycor()==pd_a.ycor()-60)):
        ball.dy*=-1
    elif(ball.xcor()>330 and ball.xcor()<370 and (ball.ycor()==pd_b.ycor()+60 or ball.ycor()==pd_b.ycor()-60)):
        ball.dy*=-1
    
    if(pd_a.ycor()>200):
        pd_a.sety(200)
    if(pd_a.ycor()<-200):
        pd_a.sety(-200)

    if(pd_b.ycor()>200):
        pd_b.sety(200)
    if(pd_b.ycor()<-200):
        pd_b.sety(-200)
        


    


