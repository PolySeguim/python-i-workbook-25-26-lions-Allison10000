import math
# zscore = (observed value - mean)/ standard deviation
#function for filtering the list
def filterlist(list):
    newlist = []
    for i in range(len(list)):
        try:
            newlist.append(float(list[i]))
        except:
            print("error on the", (i+1),"th term")
    return newlist
#function for mean 
def meanvalue(list):
    mean = 0
    n = len(list)
    for i in range(n):
        mean += list[i]
    mean = mean/n
    return mean
#function for standard deviation
def standarddev(list):
    mean = meanvalue(list)
    n = len(list)
    s = 0 
    for i in range(n):
        s += ((list[i] - n) **2)
    s = (s/(n))
    s = s ** (1/2)
    return s 
#zscore function
def zscore(value, list):
    newlist = filterlist(list)
    mean = meanvalue(newlist)
    s = standarddev(newlist)
    z = (value - mean)/s
    return round(z,4)
print(zscore(5, [6,6,2,6,7,8,4,2,6,67,4,4,5,8]))
print(zscore(5, [6,6,500, 600, 'hi', 50, "9"]))
print (standarddev([5,6,5,5,5,5,4,5]))
