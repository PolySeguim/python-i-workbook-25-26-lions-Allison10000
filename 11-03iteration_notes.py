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