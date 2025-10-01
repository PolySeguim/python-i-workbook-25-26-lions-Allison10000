
"""
Exercise 1:  Mailing Address
Create a program that displays your name and complete mailing 
address formatted in the manner that you would usually see it 
on the outside of an envelope.  Your program does not need to 
read any input from the user.  (9 lines)
"""
def exercise1():
    name = input("what is your name?")
    address = input("what is your address")
    city = input("what city do you live in")
    state = input("what is your state abbriviation")
    zip = input("what is your zip code")
    print(name)
    print(address)
    print(city, state,",", zip)
"""
Exercise 2:  Hello
Write a program that asks the user to enter his or her name.  
The program should respond with a message that says hello to 
the user, using his or her name.  (9 lines)
"""
def exercise2():
    name = input("what's your name")
    print("hello,", name)
"""
Exercise 3:  Area of a Room
Write a program that asks the user to enter the width and 
length or a room.  Once the values have been read, your 
program should compute and display the area of the room.  
The length and the width will be entered as floating point 
numbers.  Include units in your prompt and output message;  
either feet or meters, depending on which unit you are more 
comfortable working with.  (13 lines)
"""
def areaRoom():
    print("Area of Room")
    units = input("What units are you using?  feet or meters: ")
    width = float(input("Width: "))
    length = float(input("Length: "))

    areaRoom = width*length
    print("Area of the room is " + str(areaRoom) + " " + units + " squared")

"""
Exercise 4:  Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet.  Display the 
area of the field in acres.  
Hint: There are 43,560 square feet in an acre
"""
def exercise4():
    units = input("what units are you using?")
    length = float(input("what is the length of the feild"))
    width = float(input("what is the width of the feild"))
    area = length * width
    print("the area of the feild is",area,units)
"""
Exercise 5:  Bottle Deposits
In many jurisdictions a small deposit is added to drink 
containers to encourage people to recycle them.  In one 
particular jurisdiction, drink containers holding one liter 
or less have a $0.10 deposit, and drink containers holding 
more than one liter have $0.25 deposit.
Write a program that reads the number of containers of each 
size from the user.  Your program should continue by computing 
and displaying the refund that will be received for returning 
those containers.  Format the output so that it includes a dollar 
sign and always displays exactly two decimal places.  (15 lines)
"""

def bottleDeposits():
    # reads the number of bottles
    numOneLiterBottle = int(input("Number of 1L bottles: "))
    numMoreOneLiterBottle = int(input("Number of more than 1L bottles: "))
    refund = numMoreOneLiterBottle*0.25+numOneLiterBottle*0.1
    refund = round(refund, 2)
    print("Your refund will be: $", "{:.2f}".format(refund))
    # adding everything greater than 1


    # To ensure we have two decimal places
    # number_two_decimal = "{:.2f}".format(number_string)
    # print(number_two_decimal)

bottleDeposits()
#Testing Suite
#areaRoom()


#testingggggggggg
def testfunction():
    print(testing)
testfunction()


def testing():
    print("hi")