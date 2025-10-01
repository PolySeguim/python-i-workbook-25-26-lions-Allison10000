import math
"""
Exercise 21:  Area of a Triangle
The area of a triangle can be computed using the following formula,
where b is the length of the base of the triangle, and h is its 
height:
        area = (b*h)/2
Write a program that allows the user to enter values for b and h.
The program should then compute and display the area of a triangle
with base length b and height h
"""
def exercise21():
    b = float(input("base:"))
    h = float(input("height:"))
    area = (b*h)/2
    print(round(area,2))
"""
Exercise 22: Area of a triangle (Again)
In the previous exercise you created a program that computed the area
of a triangle when the length of its base and its height were known.
It is also possible to compute the area of a triangle when the lengths
of all three sides are known.  Let s1, s2, and s3 be the lengths of the
sides.  Let s = (s1 + s2 + s3)/2.  Then the area of a triangle can be 
calculated using the following formula:

     area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)

Develop a program that reads the lengths of the sides of a triangle from
the user and display its area.
"""
def exercise22():
    s1 = float(input("s1:"))
    s2 = float(input("s2:"))
    s3 = float(input("s3:"))
    s = (s1+s2+s3)/2
    area = (s*(s-s1)*(s-s2)*(s-s3))**(1/2)
    print(round(area,2))


"""
Exercise 23:  Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles
between all of the adjacent sides are equal.  The area of a regular polygon
can be computed using the following formula, where s is the length of a side
and n is the number of sides: 
     area = (n * s**(2))/(4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area
of a regular polygon constructed from these values.
"""
def exercise23():
    n = float(input("number of sides:"))
    s = float(input("side length:"))
    area = (n*2**(2))/(4*math.tan(math.pi/n))
    print(round(area, 2))
"""
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds.  Compute the total number of seconds represented
by this duration.
"""
def exercise24():
    days = float(input("days:"))
    hours = float(input("hours"))
    minutes = float(input("minutes"))
    seconds = float(input("seconds"))
    days = days * 24 * 60 * 60
    hours = hours * 60 * 60
    minutes = minutes * 60 
    seconds = seconds + days + hours + minutes
    print(round(seconds, 2))

""" 
Exercise 25: Units of Time (again)
In this exercise you will reverse the process described in the previous 
exercise.  Develop a program that begins by reading a number of seconds from 
the user.  Then your program should display the equivalent amount of time 
in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, 
minutes and seconds respectively.  The hours, minutes and seconds should all
be formatted so that they occupy exactly two digits, with a leading 0 displayed
if necessary.
"""
def exercise25():
    seconds = float(input("seconds:"))
    days = seconds//(60.0*60.0*24.0)
    seconds = seconds % (60*60*24)
    hours = seconds//(60*60)
    seconds = seconds % (60*60)
    minutes = seconds//60
    seconds = seconds%60
    print(days, ":", hours, ":", minutes, ":", seconds)



exercise25()