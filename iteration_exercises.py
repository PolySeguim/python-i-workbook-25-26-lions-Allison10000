"""
Exercise 108:  Negatives, Zeros, and Positives
Create a program that reads integers from the user until a blank 
line is entered.  Once all of the integers have been read your
program should display all the negative numbers, followed by all 
of the zeros, followed b y all of the positive numbers.  Within each
group the numbers should be displayed in the same order that they were
entered by the user.  For example, if the user enters the values 
3, -4, 1, 0, -1, 0, and -2 then your program should output the values
-4, -1, -2, 0 ,0 , 3, and 1.  Your program should display each value 
on its own line.
"""
def exrecise108(integers):
    intlist = []
    for i in integers:
        intlist.append(i)
    return intlist
def sort108(list):
    list.sort()
    return list
#print(sort108(exrecise108([2,6,3,6,3,7])))



"""
Exercise 109:  List of Proper Divisors
A proper divisor of a positive integer, n, is a positive integer
less than n which divides evenly into n.  Write a function that
computes all of the proper divisors of a positive integer.  The
integer will be passed to the function as its only parameter.
The function will return a list containing all of the proper divisors
as its only result.  Complete this exercise by writing a main program
that demonstrates the function by reading a value from the user and
displaying the list of its proper divisors.  Ensure that your main
program only runs when your solution has not been imported into
another file
"""
def exercise109(integer):
    mylist = []
    for i in range(1,integer):
        if integer % i == 0:
            mylist.append(i) 
    return mylist

#print(exercise109(12))





"""
Exercise 110: Perfect Numbers
An integer, n, is said to be perfect when the sum of all the proper
divisors of n is equal to n.  For example, 28 is a perfect number 
because its proper divisors are 1, 2, 4, 7, and 14, and 1+2+4+7+14 = 28.

Write a function that determines whether or not a positive integer is
perfect.  Your function will take one parameter.  If that parameter is a 
perfect number then your function will return true.  Otherwise it will
return false.  In addition, write a main program that uses your
function to identify and display all of the perfect numbers between 1 and
10,000.  Import your solution to Exercise 109 when completing this task.
"""
def exercise110(num):
    divisors = exercise109(num)
    divisorsum = 0 
    for i in divisors:
        divisorsum += i 
    if num == divisorsum:
        return True
    else:
        return False

#print(exercise110(28))
#print(exercise110(27))