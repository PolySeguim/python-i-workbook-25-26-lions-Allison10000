"""
Exercise 51: Letter Grade to Grade Points
At a particular university, letter grades are mapped to grade
points in the following manner:
Letter Grade points
A+ 4.0
A 4.0
A- 3.7
B+ 3.3
B 3.0
B- 2.7
C+ 2.3
C 2.0
C- 1.7
D+ 1.3
D 1.0
F 0
Write a program that begins by reading a letter grade from the
user. Then your program should compute and display the equivalent
number of grade points. Ensure that your program generates an
appropriate error message if the user enters an invalid letter
grade.
"""
#global variables (are all caps)
Aplus = 4.0
A = 4.0
Aminus = 3.7
Bplus = 3.3
B = 3.0
Bminus = 2.7
Cplus = 2.3
C = 2.0
Cminus = 1.7
Dplus = 1.3
D = 1.0
F = 0.0
Invalid = -1

def exercise51(letter):
    gpa = 0 
    if letter == "A+" or letter == "A":
        gpa = A
    elif letter == "A-":
        gpa = Aminus
    elif letter == "B+":
        gpa = Bplus
    elif letter == "B":
        gpa = B
    elif letter == "B-":
        gpa = Bminus
    elif letter == "C+":
        gpa = Cplus
    elif letter == "C":
        gpa = C
    elif letter == "C-":
        gpa = Cminus
    elif letter == "D+":
        gpa = Dplus
    elif letter == "D":
        gpa = D
    elif letter == "F":
        gpa = F
    return(gpa)



"""
Exercise 52: In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade. Ensure that your program handles grade point values that fall
between letter grades. These should be rounded to the closes letter
grade. Your program should report A+ for a 4.0 (or greater) grade
point average.
"""
def exercise52(given_gpa):
    grade = 0
    if(given_gpa >= 4.0):
        grade = "A+"
    elif given_gpa >= 3.7:
        grade = "A"
    elif given_gpa >= 3.3:
        grade = "A-"
    elif given_gpa >= B:
        grade = "B+"
    elif given_gpa >= Bminus:
        grade = "B"
    elif given_gpa >= Cplus:
        grade = "B-"
    elif given_gpa >= C:
        grade = "C+"
    elif given_gpa >= Cminus:
        grade = "C"
    elif given_gpa >= Dplus:
        grade = "C-"
    elif given_gpa >= D:
        grade = "D+"
    elif given_gpa >= F:
        grade = "D"
    elif given_gpa >= 0:
        grade = "F"
    return(grade)

"""
Exercise 66: Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution. In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by teh user. The user will enter a blank
line to indicate that all of the grades have been provided. For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this
exercise. Your program does not need to do any error checking. It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""
"""
#testing the function with imputing grades into variables
#this function works 
def exercise66test():
    grade1 = input("grade1:")
    grade2 = input("grade2")
    grade3 = input("grade3")
    grade4 = input("grade4")
    grade5 = input("grade5")
    totalgpa = 0
    totalgpa += exercise51(grade1)
    totalgpa += exercise51(grade2)
    totalgpa += exercise51(grade3)
    totalgpa += exercise51(grade4)
    totalgpa += exercise51(grade5)
    totalgpa = totalgpa / 5
    print (totalgpa)
"""

#because its in the instructions, you have to imput a blank item to indicate that all the grades have been imputed 
def exercise66(grades):
    totalgpa = 0
    for letter in grades:
        if letter == " " or letter == "":
            break
        else:
            totalgpa += exercise51(letter)
    totalgpa = totalgpa / (len(grades)-1)
    print (round(totalgpa, 3))

#exercise66(["A","C+","B","A","B", "F", "F", "D" ""])
