
def turtleclock():
    shape=float(input("spiral or circle, spiral is 1, circle is 2:"))
    import turtle
    screen = turtle.Screen()
    screen.title("Clock Turtle")
    screen.bgcolor("lightgreen")
    #turtle1 is the object
    allison = turtle.Turtle()
    allison.speed(10)
    allison.shape("turtle")
    allison.color("blue")
    screen.listen()
    if shape == 2.0:
        distance = 50
        angle = 30
        number = 12
    else:
        distance = 5
        angle = 5
        number = 500
    def drawclock():
        allison.penup()
        allison.forward(distance)
        allison.pendown()
        allison.stamp()
        allison.penup()
        allison.backward(distance)
        allison.left(angle)
        allison.pendown

    for i in range(number):
        drawclock()
        if shape == 1.0:
            distance = distance +5
    screen.mainloop()


def squareexercise():
    shape = input("what shape, 1 for square, 2 for spiral")
    if shape == "spiral":
        shape == 2
    elif shape == "square":
        shape == 1
    else:
        print("there was a spelling error")
    import turtle
    screen = turtle.Screen()
    screen.title("Clock Turtle")
    screen.bgcolor("lightgreen")
    allison = turtle.Turtle()
    allison.speed(10)
    screen.listen()
    def spiral():
        distance = 15
        angle = 90
        def drawside():
            allison.forward(distance)
            allison.right(angle)
        for i in range(150):
            drawside()
            distance = distance + 2
            angle = angle + 0.005
    def square():
        distance = 15
        angle = 90
        def drawside():
            allison.forward(distance)
            allison.right(angle)
        for i in range(150):
            drawside()
            distance = distance + 2
    if shape == 1.0:
        square()
    else:
        spiral()
    screen.mainloop()
squareexercise()