#All import statements need to be on top of your program
import turtle
def classexample():
    # Create a screen and a turtle object
    # creating a variable that will store the screen object
    # turtle.Screen you are instantiating a Screen Object
    screen = turtle.Screen()
    screen.title("Turtle Example in Python")
    # data types that are objects normally have a behavior attached to it.
    # behaviors are functions or method
    # Create a turtle instance - you are instantiating a Turtle object
    my_turtle = turtle.Turtle()

    # Draw a square
    #  The for loop will loop through the same code 4 times.
    # the i represents the loop variable.
    for i in range(4):
    #print(i)
        my_turtle.forward(100)  # Move forward by 100 units
        my_turtle.right(90)     # Turn right by 90 degrees

    # Keep the window open until clicked
    closeWindow = input("Press any key to close window. ")
    screen.mainloop()

    # Keep the window open until clicked
    turtle.done()
def morepractice():
    distance = float(input("distance:"))
    angle = float(input("angle:"))
    repeats = int(input("repeats"))
    screen=turtle.Screen()
    screen.title("tutle example in python")
    myturtle = turtle.Turtle()
    for i in range (repeats):
        myturtle.forward(distance)
        myturtle.right(angle)
    screen.mainloop()
    turtle.done
def keyboardinput():
    screen = turtle.Screen()
    myturtle = turtle.Turtle()
    screen.listen() #listens for keyboard input
    def moveup():
        myturtle.forward(50)
    def movedown():
        myturtle.back(50)
    def moveright():
        myturtle.right(45)
    def moveleft():
        myturtle.left(45)
    screen.onkey(moveup, "Up") #calls a function when key is pressed that is being listened for 
    screen.onkey(movedown, "Down")
    screen.onkey(moveright, "Right")
    screen.onkey(moveleft, "Left")
    screen.mainloop()
    turtle.done



keyboardinput()


