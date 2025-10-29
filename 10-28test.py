#truth tables
def tables(a,b,c):
    if (a and (b or c)):
        return True
    else:
        return False
print(tables(False, False, False))
#1 - I got this correct
print(tables(False,False,True))
#2 - I got this correct
print(tables(False,True,False))
#3 - I got this correct
print(tables(False,True,True))
#4 - I got this correct
print(tables(True,False,False))
#5 - I got this correct
print(tables(True, False, True))
#6 - I got this correct
print(tables(True, True, False))
#7 - I got this correct
print(tables(True, True, False))
#8 - I got this correct

#question 2, area of circle  
import math
def circlearea(radius):
    area = math.pi*radius**2
    return area
print(circlearea(1))
#this works as intended

# question 3, password guessing
password = "password"
def passwordguessing():
    for i in range (3):
        inputedpassword = input("password")
        if inputedpassword == password:
            print("correct password")
    print ("password not guessed in 3 tries")
#passwordguessing()
#because im interaccting with the program through the input function, the return values will not display so 
#I should have used the print function instead 


#question 6 
def question6():
    for i in [12,16,17,24,29]:
        if i% 2==1:
            break
        print (i)
    print ("done")
# I missinterprited the print(i) as print("i") so the correct output is 12 16 done

#question 7
def question7():
    for i in [12,16,17,24,29]:
        if i % 2 == 1:
            continue
        print (i)
    print ("done")
#I made the same mistake in this question as the last where I missinturpreted print(i) as print("i")
#the correct output is 12 16 24 done

#question 8 
def question8():
    x = 5 
    if x == 5:
        print ("Wow, X is Exactly five!")
    elif x>5:
        print ("X is now More than five!")
    else:
        print("X is now LESS than")
#I got this correct

#question 9 
def functionA(t,side,num):
    import turtle # I am calling the turtle because the function would not run without it, as I stated in my response
    t = turtle.Turtle()
    screen = turtle.Screen()
    def square(t,side):
        for i in range (4):
            t.forward(side)
            t.right(90)
    for i in range(num):
        square(t,side)
        t.penup()
        t.forward(side*2)
        t.pendown()
# I got this mostly right, the one thing I am unsure about is the use of t when it is called in the function square(t,side)
#because if it were the angle , it would no longer be a square if the user inputed anything other than 90 
 
#question 10 
def functionB():
    import turtle# I am calling the turtle because the function would not run without it, as I stated in my response
    t = turtle.Turtle()
    screen = turtle.Screen()
    for i in range(5):
        t.forward(100)
        t.right(72)
#I got this correct