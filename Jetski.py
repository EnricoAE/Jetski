# Hi! this game is called capture the white box. The rules are simple, catch white boxes as many as you can and don't let it go out of the border...
# If the white box gets out of the boundary... game is over </3
# Controls: Arrow keys to move Jetski(the cyan avatar) -- "w" to increase speed -- "s" to decrease speed -- "r" to reset speed
import turtle
import math
import random

#screen setup
scr = turtle.Screen()
scr.title("Capture the white flag")
scr.bgpic("C:\\Users\\enric\\OneDrive\\Desktop\\CTWF\\discharge.gif")

#pen
p = turtle.Pen()
p.color('black')
p.hideturtle()

#border
bor = turtle.Turtle()
bor.hideturtle()
bor.penup()
bor.setposition(-300,-300)
bor.speed(0)
bor.pendown()
bor.pensize(4)
bor.color('red')

#enemy
enemy = turtle.Turtle()
enemy.color("white")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(random.randint(-50, 50), random.randint(-50, 50))


for side in range(4):
    bor.fd(600)
    bor.lt(90)
    
#player
user = turtle.Turtle()
usr = turtle.Screen()
usr.addshape("asrNew1.gif")
usr.addshape("asrNewL.gif")
usr.addshape("asrNewD.gif")
usr.addshape("asrNewR.gif")
user.color("cyan")
user.shape("asrNewR.gif")
user.penup()
user.speed(0)

#speed
speed = 5

#functions via keys
def turnleft():
    user.setheading(180)
    user.shape("asrNewL.gif")

def turnright():
    user.setheading(0)
    user.shape("asrNewR.gif")

def goUp():
    user.setheading(90)
    user.shape("asrNew1.gif")

def goDown():
    user.setheading(270)
    user.shape("asrNewD.gif")

def gofaster():
    global speed
    speed += 1

def goSlower():
    global speed
    speed -= 1

def speedreset():
    global speed
    speed = 5

def colided(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 40:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(goUp, "Up")
turtle.onkey(goDown, "Down")
turtle.onkey(gofaster, "w")
turtle.onkey(goSlower, "s")
turtle.onkey(speedreset, "r")
score = 0
while True:
  user.fd(speed)
  enemy.fd(2)

  #out of bounds user
  if user.xcor() > 300 or user.xcor() < -300:
    enemy.hideturtle()
    user.hideturtle()
    p.write(score, font=('Arial', 35, 'bold'))
    p.hideturtle()
    p.color("yellow")
  if user.ycor() > 300 or user.ycor() < -300:
    enemy.hideturtle()
    user.hideturtle()
    p.write(score, font=('Arial', 35, 'bold'))
    p.hideturtle()
    p.color("yellow")

  #out of bounds enemy
  if enemy.xcor() > 300 or enemy.xcor() < -300:
    enemy.hideturtle()
    user.hideturtle()
    p.write(score, font=('Arial', 35, 'bold'))
    p.hideturtle()
    p.color("yellow")
  if enemy.ycor() > 300 or enemy.ycor() < -300:
    enemy.hideturtle()
    user.hideturtle()
    p.write(score, font=('Arial', 35, 'bold'))
    p.hideturtle()
    p.color("yellow")
  # d = math.sqrt(math.pow(user.xcor()-enemy.xcor(), 2) + math.pow(user.ycor()-enemy.ycor(), 2))
  #collision
  #On collision
  if colided(user, enemy):
    enemy.setposition(random.randint(-150, 250), random.randint(-120, 190))
    enemy.rt(random.randint(0, 360))
    score += 1
    speed += 1