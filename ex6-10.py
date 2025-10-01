"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
def exercise6():
    mealCost = float(input("how much did your meal cost?"))
    tax = round((mealCost * 0.05),2)
    tip = round((mealCost * 0.18),2)
    total = mealCost+tax+tip
    print("the tax for your meal is", tax, "dollars")
    print("the tip for your meal is", tip, "dollars")
    print("your total is", total, "dollars")
"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
def exercise7():
    n = float(input("input positive integer"))
    sum = (n*(n+1))/2
    print(sum)

"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""
def exercise8():
    widgetW = 75.0
    gizmoW = 112
    widgets = float(input("how many widgets are there?"))
    gizmos = float(input("how many gizmos are there?"))
    totalWeight = (widgets*widgetW)+(gizmos*gizmoW)
    print(totalWeight)
"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
def exercise9():
    interest = 0.04
    initial = float(input("how much money is in the account?"))
    after1 = round(initial*((1+interest)**1),2)
    after2 = round(initial*((1+interest)**2),2)
    after3 = round(initial*((1+interest)**3),2)
    print("the amount in the account after one year is", after1, "dollars")
    print("the amount in the account after two years is", after2, "dollars")
    print("the amount in the account after three years is", after3, "dollars")
"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
def exercise10():
    a = float(input("what is integer a"))
    b = float(input("what is integer b"))
    print("the sum of a and b is", a+b)
    print("the difference when b is subtracted from a is", b-a)
    print("the product of a and b is", a*b)
    print("the quotient when a is divided by b is", a/b)
    print("the remainder when a is divided by b is", a%b)
    print("the result of a to the power of b is", a**b)

