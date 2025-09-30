import turtle

def turtleclock():
    screen = turtle.Screen()
    screen.title("Clock Turtle")
    screen.bgcolor("lightgreen")
    #turtle1 is the object
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.color("blue")

    screen.listen()
    screen.mainloop()



turtleclock()