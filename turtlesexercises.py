
def turtleclock():
    shape=input("spiral or circle:")
    if shape == "circle":
        shape = 2
    elif shape == "spiral":
        shape = 1
    import turtle
    screen = turtle.Screen()
    screen.title("Clock Turtle")
    screen.bgcolor("lightgreen")
    allison = turtle.Turtle()
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
        allison.speed(1000)
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
    shape = input("what shape, square, spiral, or custom")
    if shape == "spiral":
        shape = float(2)
    elif shape == "square":
        shape = float(1)
    elif shape == "custom":
        shape = float(3)
    def spiral():
        import turtle
        screen = turtle.Screen()
        screen.bgcolor("lightblue")
        allison = turtle.Turtle()
        allison.speed(100)
        allison.color("purple")
        screen.listen()
        distance = 15
        angle = 90
        def drawside():
            allison.forward(distance)
            allison.right(angle)
        for i in range(150):
            drawside()
            distance = distance + 2
            angle = angle + 0.005
        screen.mainloop()
    def custom():
        distance = float(input("distance:"))
        angle = float(input("angle:"))
        changeinangle = float(input("change in angle:"))
        changeindistance = float(input("change in distance:"))
        repeats = int(input("repeats"))
        speed = float(input("speed"))
        import turtle
        screen = turtle.Screen()
        screen.bgcolor("orange")
        allison = turtle.Turtle()
        allison.speed(speed)
        allison.color("green")
        screen.listen()
        def drawside():
            allison.forward(distance)
            allison.right(angle)
        for i in range(repeats):
            drawside()
            distance = distance + changeindistance
            angle = angle + changeinangle
        screen.mainloop()
    def square():
        import turtle
        distance = 15
        angle = 90
        screen = turtle.Screen()
        screen.bgcolor("red")
        allison = turtle.Turtle()
        allison.speed(100)
        allison.color("orange")
        screen.listen()
        def drawside():
            allison.forward(distance)
            allison.right(angle)
        for i in range(150):
            drawside()
            distance = distance + 2
        screen.mainloop()
    if shape == float(1):
        square()
    elif shape == float(2):
        spiral()
    elif shape == float(3):
        custom()


squareexercise()