"""
Exercise 34:  Even or Odd?
Write a program that reads an integer from the user.  
Then your program should display a message indicating whether
the integer is even or odd    
"""
def exercise34():
    num = int(input("number:"))
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
"""
Exercise 36:  Vowel or consonant
In this exercise you will create a program that reads a letter
of the alphabet from the user.  If the user enters a, e, i, o, or u
then your program should display a message indicating that the 
entered letter is a vowel.  If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and 
sometimes y is a consonant.  Otherwise your program should display
a message indicating that the letter is a consonant.
"""
def exercise36():
    letter = input("letter:")
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("letter is a vowel")
    else:
        print("letter is a consonant")
"""
Exercise 40:  Name that triangle
A triangle can be classified based on the lengths of its sides as
equilateral, isosceles, or scalene.  All 3 sides of an equilateral
triangle have the same length.  As isosceles triangle has two sides
that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.

Write a program that reads the lengths of 3 sides of a triangle from the
user.  Display a message indicating the type of triangle

******  CHALLENGE:
Perform the same task as above but with angles and not sides.
"""
def exercise40():
    
    def angles():
        s1 = float(input("angle1:"))
        s2 = float(input("angle2:"))
        s3 = float(input("angle3:"))
        if s1 == s2 == s3:
            print("equilateral triangle")
        elif s1 == s2 or s2 == s3 or s3 == s1:
            print("isosceles triangle")
        else:
            print("scalene triangle")
    def sides():
        s1 = float(input("side1:"))
        s2 = float(input("side2:"))
        s3 = float(input("side3:"))
        if s1 == s2 == s3:
            print("equilateral triangle")
        elif s1 == s2 or s2 == s3 or s3 == s1:
            print("isosceles triangle")
        else:
            print("scalene triangle")
    sideangle = input("angles or sides?")
    if sideangle == "angles":
        angles()
    else:
        sides()
"""
Exercise 55: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and
50 text messages for $15.00 a month.  Each additional minute of 
air time costs $0.25 , while additional text messages cost $0.15
each.  All cell phone bills include an additional charge of $0.44
to support 911 call centers, and teh entire bill (including the 
911 charge) is subject to a 5 percent sales tax.

Write a program that reads the number of minutes and text messages
used in a month from the user.  Display the base charge, additional
minutes charge (if any), additional text message charge (if any), 
the 911 fee, tax and total bill amount.  Only display the additional 
minute and text charges if the user incurred costs in these 
categories.  Ensure that all of the charges are displayed using 2
decimal points
"""

def exercise55():
    minutes= float(input("minutes:"))
    texts = float(input("texts"))
    bill = 15
    minutes = minutes - 50
    texts = texts - 50 
    if minutes > 0:
        bill = bill + (minutes * 0.25)
    if texts > 0:
        bill = bill + (texts*0.15)
    bill =bill +0.44
    bill = bill * 1.05
    print("the bill is, $",round(bill,2))
exercise55()