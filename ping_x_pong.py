import turtle


wind=turtle.Screen()
wind.title("ping X pong")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)
madrab1=turtle.Turtle()
madrab1.speed(1)
madrab1.shape("square")
madrab1.shapesize(stretch_len=1,stretch_wid=5)
madrab1.color("blue")
#madrab1.penup()
madrab1.goto(-350,0)
#_______________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------
madrab2=turtle.Turtle()
madrab2.speed(1)
madrab2.shape("square")
madrab2.shapesize(stretch_len=1,stretch_wid=5)
madrab2.color("red")
#madrab2.penup()
madrab2.goto(350,0)
#_______________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------

ball=turtle.Turtle()
ball.speed(4)
ball.shape("circle")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=1
#_________________________________________
#+++++++++++++++++++++++++++++++++++++++++
#_________________________________________
player_1=0
player_2=0
scour=turtle.Turtle()
scour.speed(0)
scour.color("white")
#scour.penup()
scour.hideturtle
scour.goto(0,260)
#_______________________________________________________

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------
def madrab1_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)
wind.listen()
wind.onkeypress(madrab1_up,"w")    
#_______________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------
def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)
wind.listen()
wind.onkeypress(madrab1_down,"s")    
#_______________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------
def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)
wind.listen()
wind.onkeypress(madrab2_up,"Up")    
#_______________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
def End():
    wind.bye()
wind.listen()
wind.onkeypress(End,"space")
#-------------------------------------------------------
def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)
wind.listen()
wind.onkeypress(madrab2_down,"Down") 
wind.bgcolor('black')
       
while True:
    wind.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() >290 :
        ball.sety(290)
        ball.dy *=-1
    
    if ball.ycor() <-290 :
        ball.sety(-290)
        ball.dy *=-1
    #_______________________
    # ______________________
    if ball.xcor() >390 :
        ball.goto(0,0)
        ball.dx *=-1
        player_1+=1
        scour.clear()
        scour.write("player 1 : {} player 2 : {}".format(player_1, player_2),align="center",font=("Courier",24,"normal"))



    if ball.xcor() <-390 :
        ball.goto(0,0)
        ball.dx *=-1
        player_2+= 1
        scour.clear()
        scour.write("player 1 : {} player 2 : {}".format(player_1, player_2),align="center",font=("Courier",24,"normal"))


    if (ball.xcor()>340 and ball.xcor()< 350)and(ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1    
    if (ball.xcor()<-340 and ball.xcor()> -350)and(ball.ycor()<madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1    



       