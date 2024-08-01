import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "blue", "yellow", "green", 
          "orange", "purple", "white"] #Color with iterate

for x in range(500): #For cicle iterate 500
    t.pensize(x/1000 + 1) #rotate
    t.pencolor(colors[x % 6]) #Change color by a draw line
    t.forward(x)
    t.left(59)

t.hideturtle()
turtle.done()