#question 1
def question1():
    a = 9
    while a>0:
        print(a)
        a -= 1
        if a == 1:
            break
        else:
            print("reached 0")
#question 1 was pertially right
#the thing that I did wrond was I said that it would also print 1 and reached 0 but it did not 

#question 2 
def question2():
    for i in range(3):
        for j in range(3):
            print("*", end = " ")
    print()
# I got this correct because I said that it would print 9 * in a row

#question 3
def question3():
    i = 1
    while i <= 5:
        print(i)
        i+= 1
#I got this correct because I said that it would print 1 through 5 in seperate lines

#question 4
def question4():
    x = 0 
    while x < 10:
        x+=2
    print(x)
#I got this correct because I said that it would print just 10 

#question 5
#Im pretty sure that I got this correct because I said break 

#question 6 
def question6():
    result = 0 
    for i in range(4):
        if i % 2 == 0:
            result = result +1
        else:
            result = result - 1
#I got this correct because I said that it would print 0 

#question 7 
def question7():
    nums = [10,20,30]
    for num in nums:
        if num > 25:
            print("large number not found")
    else:
        print("no large numbers")
#I got this incorrect, I selected d when it should have been a

#question 8 
def question8():
    count = 0 
    while count < 5:
        print(count)
        if count == 2:
            break
        count += 1
    else:
        print("loop completed")
#I got this incorrect, it should have been B but i put a 

#question 9 
def question9():
    for i in range(99):
        num = i+1
        if num % 2 == 1:
            print(num)
#I got this correct because it displays all odd numbers

#question 10 
def question10():
    mylist = [10,20,30]
    for i in range(len(mylist)):
        print(mylist[i])
#I got this correct becuase I said b 

#question 11
#this was a multiple choice quesiton, and from what i could find, i got it correct

#question 12
def question12():
    x = 0 
    a = 0 
    b = -5
    if a >0:
        if b < 0 :
            x = x+5
        elif a > 5:
            x = x+4
        else:
            x = x+3
    else:
        x = x+2
    print(x)
#I got this correct because it printed 2, which is what I said would happen
 
#question 13
def question13():
    x= 0 
    while x < 3:
        x += 1 
        if x ==2:
            continue
        print(x)
#I got this incorrect because I thought the continue would cause an error but it didnt 

#question 14
#This was a multiple choice question that I think is correct

#question 15
#this is also a multiple choice question that I think is correct 

#question 16
def question16():
    x = 0 
    a = 5
    b = 5
    if a >0:
        if b <0:
            x = x+5
        elif a >5:
            x = x+4
        else:
            x = x+3
    else:
        x =x+2
    print(x)
#I got this correct because I said it would print 3, which it did

#question 17 
#I had said b, but I think it could also be C

#question 18
#I was unsure what this question meant, but im interpereting it as an and function where both questions had to be true, so if the first expression is false, the second dosent need to be evaluated

#question 19
def question19():
    for num in range(10):
        print(num)
#I was correct because I said that it would print 0 to 9, each on their own line

#question 20
"""
def question20():
    newlist = []
    def program(userinputlist):
        for i in range(len(userinputlist)):
            if i == 0:
                return newlist
            else:
                newlist.append(userinputlist(i))
    print(program([1,2,5,4,0]))
"""
#this is my answer, where i say i == 0, it should be  userinput[i]==0
#this is the correct answer:
"""
def question20corrected():
    newlist = []
    def program(userinputlist):
        for i in range(len(userinputlist)):
            if i == 0:
                return newlist
            else:
                newlist.append(userinputlist(i))
    print(program([1,2,5,4,0]))
question20corrected()
"""

def question20corrected(userinputlist):
    newlist = []
    for i in userinputlist:
        if i == 0:
            return newlist
        else:
            newlist.append(i)
    return newlist
print(question20corrected([1,2,5,4,0]))