import turtle
import time
import random
import tkinter
delay = 0.1
Gold = 0
MAX_GOLD = 0
# screen setup
wn = turtle.Screen()
wn.title("treasure hunt")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #anti screen updates cause that helps apparantly
#blob
blob = turtle.Turtle()
blob.speed(0)
blob.shape("square")
blob.color("black")
blob.penup()
blob.goto(0,0)
blob.direction = "stop"
#scoring
treasure=turtle.Turtle()
treasure.speed(0)
treasure.shape("circle")
treasure.color("red")
treasure.penup()
treasure.goto(0,100)
segments = []
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gold: 0  MAX_GOLD: 0", align="center", font=("Courier", 24, "normal"))
### Functions ###
def up():
    if blob.direction != "down":
        blob.direction = "up"

def down():
    if blob.direction != "up":
        blob.direction = "down"

def left():
    if blob.direction != "right":
        blob.direction = "left"

def right():
    if blob.direction != "left":
        blob.direction = "right"

def move():
    if blob.direction == "up":
        y = blob.ycor()
        blob.sety(y + 20)

    if blob.direction == "down":
        y = blob.ycor()
        blob.sety(y - 20)

    if blob.direction == "left":
        x = blob.xcor()
        blob.setx(x - 20)

    if blob.direction == "right":
        x = blob.xcor()
        blob.setx(x + 20)
#bindings
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
#main loop
while True:
    wn.update()
    # anti running off screen
    if blob.xcor()>290 or blob.xcor()<-290 or blob.ycor()>290 or blob.ycor()<-290:
        time.sleep(1)
        blob.goto(0,0)
        blob.direction = "stop"
        Gold = 0
        delay = 0.1
        #reset
        pen.clear()
        pen.write("Gold: {}  MAX_GOLD: {}".format(Gold, MAX_GOLD), align="center", font=("Courier", 24, "normal")) 

    #treasure collision checker
    if blob.distance(treasure) < 20:
        # Move the treasure to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        treasure.goto(x,y)
        # Shorten the delay
        delay -= 0.001
        # Increase the Gold
        Gold += 10
        if Gold > MAX_GOLD:
            MAX_GOLD = Gold      
        pen.clear()
        pen.write("Gold: {}  High Gold: {}".format(Gold, MAX_GOLD), align="center", font=("Courier", 24, "normal")) 
    move()    
    time.sleep(delay)

wn.mainloop()
