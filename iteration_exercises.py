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

#with user input
def exercise1082():
    intlist = []
    try: 
        userinput = int(input("input:"))
        while userinput != "":
            intlist.append(userinput)
    except:
       print("error")
def sort108(list):
    l1 =[]
    l2=[]
    l3=[]
    for i in list:
        if i > 0:
            l3.append(i)
        if i <0:
            l1.append(i)
        if i == 0:
            l2.append(i)
    return (l1,l2,l3)

#this is the way that i had origionally done it, its different than in class but I think it works better and its more efficient 
def exrecise108(integers):
    intlist = []
    for i in integers:
        intlist.append(i)
    return intlist
def sort108differently(list):
    list.sort()
    return list
#print(sort108(exrecise108([2,6,3,6,3,7])))
#print(sort108differently(exrecise108([2,6,3,7,4,7,-3,3,0,-5,5])))


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

#more excersizes from the book
"""
exercise 111: perfect numbers
in this excersese you will create a program that identifies all of the words in a string
entered by the user. begin by writing a function that takes a string of text as its only 
paramater your function should return a list of words in a string with the punctuation 
marks at the edges of the words removed. the punctuation makes that you must remove 
include commoas, periods, question marks, hyphens, apostrophes, explanationn points, 
colons, and semicolons. Do not remove punctuation marks that appear in the middle of words.
 for example, if the function is provided with "examples of contractions include: don't, isn't
   and wouldn't" then returns the list ["examples", "of", etc.]
"""
def exercise111(words):
    string = words.split()
    for i in string:
        
    print (string)
exercise111("hello my nae is allison")



"""
excersize 112: remove outliers 
takes a list of numbers and removes the two largest and two smallest numbers, if there are
less than 4 values entered, show an error code"""
def exercise112(values):
    mylist = []
    for i in values:
            mylist.append(i)
    mylist.sort()
    if mylist.len() > 4:
        return False
    mylist = mylist[2:-2]
    return(mylist)
#print(exercise112([7,2,525,2,5,46,9,242]))
#print(exercise112([7,2,525]))
