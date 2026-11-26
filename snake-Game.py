# simpe snake game build with pythoen 

# 1part

import turtle

# set screen 
wn = turtle.Screen()
wn.title("Snake Game by @ZAC")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  #off screen updates

# Snack head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"



wn.update()
wn.mainloop()




