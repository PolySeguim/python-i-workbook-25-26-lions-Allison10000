def airtime():
    airtimeremaining = 15+3
    print (airtimeremaining)
    airtimeremaining = 7
    print (airtimeremaining)

# i = loop variable
#it should only be visible inside the loop 
#but it can still be visible outside the look for the last value but it still shouldnt be used 
for i in ["red", "blue", "yellow"]:
    print (i) 

print("outside the loop", i)
#pythn is kind in allowing access to the last value of the loop variable i 

# assignments look like a = 8 b = 9 etc

"""
a = 5 # the value 5 is assigned to the variable a
b= a  # the value of a is assigned to the variable b 
a = 3 # the value of 3 is assigned to the variable a
print(a,b)
"""

#traversing --> running trough all intems in a list
#bianary search - needs an ordered list and once everything is ordered, it cuts it in the middle repeatidly until it finds the value


def mysum(xs):
    runningtotal = 0
    for x in xs:
        runningtotal = runningtotal + x
    return runningtotal
def test(pass_fail):
    if pass_fail:
        return True
    else:
        return False
print(test(mysum([1,5,2,6,3])==10))
print(test(mysum([1,5,2,6,3])==17))

def mysum(xs):
   """ Sum all the numbers in the list xs, and return the total. """
   running_total = 0
   for x in xs:
       running_total = running_total + x
   return running_total

 def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss

#TESTING AREA
def test(pass_fail):
    if pass_fail:
        return True
    else:
        return False

def testsuite():
    # Add tests like these to your test suite ...
    print(test(mysum([1, 2, 3, 4]) == 10))
    print(test(mysum([1.25, 2.5, 1.75]) == 5.5))
    print(test(mysum([1, -2, 3]) == 2))
    print(test(mysum([ ]) == 0))
    print(test(mysum(range(11)) == 55))  # 11 is not included in the list.
    print(test(sum_to(4) == 10))
    print(test(sum_to(1000) == 500500))



#csv file = comma seperated values file 
# it will look like value1, value2, value3
#the first like will be column names