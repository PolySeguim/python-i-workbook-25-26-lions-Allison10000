"""
functions are either void or fruitful
"""
import math
import random
#globalvariable
f_name = ""
#defining functions
def setname(fname):
    f_name=fname
    print(fname)

def getname():
    return f_name


#calling functions
"""
setname("allison")
setname(":)")
name = getname()
print ("hi", name)
"""

#addition practice
def sum(numbers):
    sum = 0 
    for i in numbers:
        sum += i
    return sum #you can only return one thing

var1 = (1, 2, 3, 5, 6, 8, 10)
var2 = (3.5,25,5.9)

def absvalue(x):
    if x<0:
        return-x
    return x

def factorial(x):
    factorial = 0 
    for i in range(x+1):
        factorial += i
    return factorial 
#utilize the print function to debug code



def gradecalculation(x):
    numbergrade = (90, 80, 70, 60)
    lettergrade = ("A", "B", "C", "D")
    if x in numbergrade:
        grade = lettergrade.index(x)
    return grade


"""
def distanceformula(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
"""

#boolian functions 
def isdivisable(x,y):
    if x%y == 0:
        return True
    else:
        return False
def zscore(mean, observed, sd):
    z = (float(observed)-float(mean))/sd
    return z

def rpsgame():
    #rock = 1
    #paper = 2
    #scissors = 3
    playerresponse = input("your response:")
    if playerresponse == "rock":
        playerresponse = 1
    elif playerresponse == "paper":
        playerresponse = 2
    elif playerresponse == "scissors":
        playerresponse == 3
    else:
        print("spelling error")
    computerresponse = random.randint(1,3)
    #comp - scissors user - rock - win
    #comp - scissors user - paper - loose
    if computerresponse == playerresponse:
        result = "tie"
    if computerresponse == 1:
        print("computer chose rock")
        if playerresponse == 2:
            result = "win"
        if playerresponse == 3:
            result ="lose"
    if computerresponse == 2:
        print("computer chose paper")
        if playerresponse == 1:
            result ="looe"
        if playerresponse == 3:
            result = "win"
    if computerresponse == 3:
        print("computer chose scissors")
        if playerresponse ==1:
            result = "win"
        if playerresponse == 2:
            result = "lose"
    
    print("you", result)
