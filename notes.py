# def is the keyword to define a function
# whatType is the name of the function
# userInput is the parameter of the function

def whatType(userInput):
    # print is a Python built-in function that prints to the console
    # type is a Python built-in function that finds the datatype
    # userInput is the variable that the user enters
    print(type(userInput))

# The pound symbol is for one line comments
# The program ignores all commments

"""
multiple lines comments
"""
# Call the function with different user inputs
# If you don't call the function, nothing will run in the program

"""
Test SUITE
"""

whatType(3)
whatType(3.0)
whatType("3.0")
whatType(True)
whatType("polyana")
whatType('p')

#Create a variable named message
message = """this is a
multiline message
to my bestie."""
print(message)

#test inputs to print and see how they print
print(42000)
#every time you have a comma between values, it will understand as a different
#parameter input
print(42,"poly",3,"chem","computer")
print(42,000)
print(42.000)

name = "polyana"
newName = "poly"
name = newName
newName = name

print(name)
print(newName)

classOf2026 = ["Student 1", "Student 2"]
seniors = "not a good variable name...  why???"

# MLS formatting for GEEKS
#Global variable for things that cannot change

# In naming variable the variable day <> Day
# we want to use lower case as much as possible...
# for Python day_of_the_week
# in Java dayOfTheWeek

"""
ILLEGAL VARIABLE NAMES!
21yearsold = "party!"
dolla$$$$

def = "def"
class = "python"
"""

print(20+12)
hour = 3
print(hour - 1)
print(hour * 60, " minutes in ", hour, " hour")

myName = "poly"
print(myName * 5)
# str is casting the integer data type to a string
# so you can concatenate (add) two strings together
print(myName + str(5))

#Operations
# Addition
#   add numbers or concatenate string
# Subtraction
#   to numbers only
# Division
#   numbers only... 
#   - / - division (typical) but the answer is always a float
#   - // - floor division (divides to the largest integer) answer is an int
#   - % - modulus operator (finds the remainder of the division) answer is an int
print(10/3)  #3.3333333333333335
print(10//3) #3
print(10%3)  #1
# Multiplication
#   for numbers and strings
#   - * - multiplies only
#   - ** - exponential
print(8*2)
print(8**2)

print(int(3.14))
print(int(3.99999))
print(int(-4.11212132))
print(int(-4.99999))
print(int("1977"))
#print(int("polyana"))

print(float(1977))
print(float(3.1415))

print(str(1977))
print(str(3.0))


#10/8 notes fruitful functions
def functionname(number,id):
    #void function - does not return 
    #fruitful function - returns 
