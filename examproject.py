#for my exam project im going to do a planner that works with the mericci scedule 
#i also added functions to do things that typical high schoolers may find useful
#I would like to eventually add the ability to import CSVs for the functions that you have to imput values 
# and create a function to scheudle an appointment 
import time
import tkinter as tk
from tkinter import filedialog
import csv
import turtle
import random

LetterDay=""
A = []
B = []
C = []
D = []
E = []
F  = []
Mods = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
currentmod = 1
currenttime = 0
todos=[]
frees = []
classnumber = 0 
Totalgrade = 0
decspecialschedulemonthdays = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31]
decspecialscheduleevents = ["assembly", "christmas hope", "christmas hope", "christmas hope and spring sports signups", "christmas hope and the gingle", "church", "advent reconciliation", "resting before testing", "PALS, resting before testing", "resting before testing", "exams", "exams", "exams", "exams", "record day", "break", "break", "break","break","break","break","break","break"]# i intend to turn these long lists into csvs at some point            
decmonthdays = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
deccycledays = ["E","F","A", "A", "A", "B","C","D","E","F","F","F","F","F","F"]
decspecialschedules = ["ACT 1", "Regular", "Regular", "HR 1", "HR 2", "ACT 5", "Regular", "Regular", "HR 1", "Regular", "exam", "exam", "exam", "exam", "no school", "no school","no school","no school","no school","no school","no school","no school","no school",]
#refines the letter day to account for any errors 
def whatday():
    t = time.localtime()
    monthday = t.tm_mday
    for i in range(len(decmonthdays)):
        if decmonthdays[i] == monthday:
            day = deccycledays[i]
    if day == "A" or day == "a":
        return A
    elif day == "B" or day =="b":
        return B
    elif day == "C" or day == "c":
        return C
    elif day == "D" or day == "d":
        return D
    elif day == "E" or day == "e":
        return E
    elif day == "F" or day == "f":
        return F
    else:
        print("invalid day given")
#returns the letter day as a string
def whatletterday():
    t = time.localtime()
    monthday = t.tm_mday
    for i in range(len(decmonthdays)):
        if decmonthdays[i] == monthday:
            day = deccycledays[i]
    if day == "A" or day == "a":
        return "A"
    elif day == "B" or day =="b":
        return "B"
    elif day == "C" or day == "c":
        return "C"
    elif day == "D" or day == "d":
        return "D"
    elif day == "E" or day == "e":
        return "E"
    elif day == "F" or day == "f":
        return "F"
    else:
        print("invalid day given")
#determines the mod depending on the time using an annoying amount of conditionals 
def moddromtime(time1):
    #8 oclock
    currentmod = 1
    if time1[-4] == "8":
        if time1[-2] == "0":
            if time1[-1] == "9":
                currentmod = 1
            else:
                currentmod = "no mod"
        elif time1[-2] == "1" or time1[-2] == "2":
            currentmod = 1
        elif time1[-2] == "3" or time1[-2]=="4":
            currentmod = 2 
        elif time1[-2] == '5':
            if (time1[-1] == "0") or (time1[-1] == "1") or (time1[-1] == "2"):
                currentmod = 2
            else:
                currentmod = 3
        else:
            currentmod = "error, likely passing time"
    #9 oclock 
    if time1 [-4] == "9":
        if time1[-2] == "0":
            currentmod = 3
        elif time1[-2] == "1":
            if (time1[-1] == "0") or (time1[-1] == "1") or (time1[-1] == "2") or (time1[-1] == "3") or (time1[-1] == "4") or (time1[-1] == "5"):
                currentmod = 3
            else:
                currentmod = 4
        elif time1 [-2] == "2":
            currentmod = 4
        elif time1 [-2] == "3":
            currentmod = 4
        elif time1[-2] == "4" or time1[-2] == "5":
            currentmod = 5
        else:
            currentmod = "erroe, likely passing time"
    #10 oclock 
    if time1 [-4] == "0":
        if time1[-2] == "0":
            if time1[-1] == "0" or time1[-1] == "1":
                currentmod = 5
            else:
                currentmod = 6
        elif time1[-2] == "1":
            currentmod = 6
        elif time1 [-2] == "2":
            if time1[-1] == "1" or time1[-1] == "2" or time1[-1] == "3" or time1[-1] == "0" or time1[-1] == "4":
                currentmod = 6
            else:
                currentmod = 7
        elif time1 [-2] == "3" or time1[-2]=="4":
            currentmod = 7
        elif time1[-2] == "5":
            currentmod = 8
        else:
            currentmod = "erroe, likely passing time"
    #11 & 1 oclock
    if time1[-4] == "1":
            if time1[-2] == "0":
                currentmod = 8
            elif time1[-2] == "1" or time1[-2] == "2":
                currentmod = 9
            elif time1 [-2] == "3":
                if time1[-1] == "0" or time1[-1] == "1" or time1[-1] == "3" or time1[-1] == "2":
                    currentmod = 9 
                else:
                    currentmod = 10
            elif time1[-2] == "4":
                currentmod = 10
            elif time1[-2] == "5":
                if time1[-1]=="9":
                    currentmod = 11
                else:
                    currentmod = 10
            else:
                currentmod = "erroe, likely passing time"
        #1 oclock
    if time1[-4] == "3":
        if time1[-2] == "0":
            if time1[-1] == "8" or time1[-1] == "9":
                currentmod = 14
            else:
                    currentmod = 13
        elif time1[-2] == "1":
                currentmod = 14
        elif time1 [-2] == "2":
                currentmod = 14
        elif time1 [-2] == "3" or time1[-2]=="4":
                currentmod = 15
        elif time1[-2] == "5":
            if time1[-1]=="0" or time1[-1]=="1":
                currentmod = 15
            else:
                currentmod = 16
        else:
            currentmod = "erroe, likely passing time"
    #12 & 2 oclock 
    if time1[-4] == "2":
        if len(time1) == 5:
            if time1[-2] == "0":
                currentmod = 11
            elif time1[-2] == "1":
                currentmod = 11
            elif time1[-2] == "2":
                currentmod = 12
            elif time1 [-2] == "3":
                currentmod = 12
            elif time1[-2] == "4":
                if time1[-1]=="1" or time1[-1]=="2" or time1[-1] == "1":
                    currentmod = 12
                else:
                    currentmod = 13
            elif time1[-2] == "5":
                currentmod = 13
            else:
                currentmod = "erroe, likely passing time"
        #2 oclock 
    elif time1[-4] == "4":
            if time1[-2] == "0":
                currentmod = 16
            elif time1[-2] == "1":
                if time1[-1]=="7" or time1[-1]=="8" or time1[-1]=="9":
                    currentmod = 17
                else:
                    currentmod = 16
            elif time1 [-2] == "2":
                currentmod = 17
            elif time1 [-2] == "3":
                currentmod = 17
            elif time1[-2]=="4":
                currentmod = 18
            elif time1[-2] == "5":
                currentmod == 18
            else:
                currentmod = "erroe, likely passing time"
    return currentmod
#This function gets the time and converts it into the hour:minute format
def timestuff(): 
    unusabletime = time.ctime()
    unusabletime.split()
    currenttime = unusabletime[11:16]
    return currenttime
#function to open dialog box that you will choose file location and file
def choose_file():
    root = tk.Tk()
    root.withdraw() #hide the main window
    file_path = filedialog.askopenfilename(filetypes = [("CSV files", "*.csv")])
    return file_path
#this function reads the CSV file and creates lists of classes for each letter day
def read_csv(file_name):
        with open(file_name, mode="r", newline='', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                A.append(row['A'])
                B.append(row['B'])
                C.append(row['C'])
                D.append(row['D'])
                E.append(row['E'])
                F.append(row['F'])
#this class takes the day and searches the corrisponding list for the current mod
#for this function to work, the global variable currentmod must be declared
def whatclass(day):
    classmod=int(moddromtime(timestuff))
    return day[classmod-1]
#this function's goal is to take the users to do list and schedule free mods
def addtodo():
    todos.append(input("to do item:"))
#this function will keep running the addtodo function until the user tells it to stop 
def todoloop():
    addtodo()
    tf = input("do you have another to add, yes or no")
    if tf == "yes" or tf == "Yes":
        todoloop()
    
    return todos 
#this function will return what frees you have on a certian day
def findfrees(rday):
    frees = []
    for i in range(len(rday)):
        if rday[i] == "Free":
            frees.append(Mods[i])
    return frees
#this function will show your schedule on a specific day
def chooseday():
    typeofday = input("do you want to see your schedule from the monthday or letterday")
    if typeofday in ["monthday", "Monthday", "Month Day", "Month day", "month day"]:
        choosenday = int(input("what month day? "))
        for i in range(len(decmonthdays)):
            if choosenday == int(decmonthdays[i]):
                newchooosenday = (deccycledays[i])
        if newchooosenday == "A":
            choosenday = A
        elif newchooosenday == "B":
            choosenday = B
        elif newchooosenday == "C":
            choosenday = C
        elif newchooosenday == "D":
            choosenday = D
        elif newchooosenday == "E":
            choosenday = E
        elif newchooosenday == "F":
            choosenday = F
    else:
        choosenday = input("what letter day? ")
        if choosenday in ["A","a"]:
            choosenday = A
        elif choosenday in ["B","b"]:
            choosenday = B
        elif choosenday in ["C","c"]:
            choosenday = C
        elif choosenday in ["D","d"]:
            choosenday = D
        elif choosenday in ["E","e"]:
            choosenday = E
        elif choosenday in ["F","f"]:
            choosenday = F
    for i in range(len(choosenday)):
        print(choosenday[i])
#free mod scheduling 
def freescheduling(frees, thingstodo):
    print(" ")
    if len(frees)>len(thingstodo):
        for i in range(len(thingstodo)):
            print("durring mod", frees[i], "you will complete the task:", thingstodo[i])
        print("you will have free time for the rest of your frees")
    if len(frees)<len(thingstodo):
        for i in range(len(frees)):
            print("durring mod", frees[i], "you will complete the task:", thingstodo[i])
        print("you have more things to do than frees, you will have homework")
    if len(frees) == len(thingstodo):
        for i in range(len(frees)):
            print("durring mod", frees[i], "you will complete the task:", thingstodo[i])
#this function will calculate your GPA
def gpacalculator():
    Totalgrade = 0.0
    classnumber = 0
    #create a function that will prompt the user to imput the grade and level of a class and it will add to
    def gradeiteration():
        nonlocal Totalgrade, classnumber
        currentclassgrade = input("what was your letter grade in a class: ")
        currentclasslevel = input("what level was this class, Honors, AP, or Regular: ")
        #filtering class grade
        if currentclassgrade == "A" or currentclassgrade == "a" or currentclassgrade == "A+" or currentclassgrade == "a+":
            gradepoints = 4.0
        elif currentclassgrade == "A-" or currentclassgrade == "a-":
            gradepoints = 3.6
        elif currentclassgrade == "B+" or currentclassgrade == "b+":
            gradepoints = 3.3
        elif currentclassgrade == "B" or currentclassgrade == "b":
            gradepoints = 3.0
        elif currentclassgrade == "B-" or currentclassgrade == "b-":
            gradepoints = 2.6
        elif currentclassgrade == "C+" or currentclassgrade == "c+":
            gradepoints = 2.3
        elif currentclassgrade == "C" or currentclassgrade == "c":
            gradepoints = 2.0
        elif currentclassgrade == "C-" or currentclassgrade == "c-":
            gradepoints = 1.6
        elif currentclassgrade == "D+" or currentclassgrade == "d+":
            gradepoints = 1.3
        elif currentclassgrade == "D" or currentclassgrade == "d":
            gradepoints = 1.0
        elif currentclassgrade == "D-" or currentclassgrade == "d-":
            gradepoints = 0.6
        elif currentclassgrade == "F" or currentclassgrade == "f":
            gradepoints = 0
        #filtering class level
        if currentclasslevel == "Honors" or currentclasslevel == "honors":
            levelmultiply = 1.15
        elif currentclasslevel == "AP" or currentclasslevel == "ap" or currentclasslevel == "Ap":
            levelmultiply = 1.25
        else:
            levelmultiply = 1 
        #adding to overal average 
        Totalgrade += (float(gradepoints) * float(levelmultiply))
        classnumber+=1
        moregrades = input("do you have more classes to input? ")
        if moregrades == "Yes" or moregrades == "yes":
            gradeiteration()
    gradeiteration()
    newnewgrade = Totalgrade / classnumber
    print("your gpa is ", round(newnewgrade,2))
#with this function, you can input your extracurriculars and it will tell you what you have to do on a certian day
def extraccurricular():
    currentweekday = time.ctime()
    currentweekday = currentweekday.split()
    currentweekday = currentweekday[0]
    monschedule = []
    tueschedule = []
    wedschedule = []
    thuschedule = []
    frischedule = []
    satschedule = []
    sunschedule = []
    def extracurricularschedule():
        extracurricular = input("waht is your extracurricular? ")
        mons = input("do you have extracurricular this on monday? ")
        if mons == "yes" or mons == "Yes":
            monschedule.append(extracurricular)
        tues = input("do you have extracurricular this on tuesday? ")
        if tues == "yes" or tues == "Yes":
            tueschedule.append(extracurricular)
        weds = input("do you have extracurricular this on wednesday? ")
        if weds == "yes" or weds == "Yes":
            wedschedule.append(extracurricular)
        thus = input("do you have extracurricular this on thursday? ")
        if thus == "yes" or thus == "Yes":
            thuschedule.append(extracurricular)
        fris = input("do you have extracurricular this on friday? ")
        if fris == "yes" or fris == "Yes":
            frischedule.append(extracurricular)
        sats = input("do you have extracurricular this on saturday? ")
        if sats == "yes" or sats == "Yes":
            satschedule.append(extracurricular)
        suns = input("do you have extracurricular this on sunday? ")
        if suns == "yes" or suns == "Yes":
            sunschedule.append(extracurricular)
        more = input("do you have any more extracurriculars to add to your schedule? ")
        if more == "yes" or more =="Yes":
            extracurricularschedule()
    extracurricularschedule()
    print(" ")
    def displayscheduleitems(rschedule):
        if len(rschedule) < 1:
            print("you have no extracurriculars this day")  
        else:
            for i in range(len(rschedule)):
                print(rschedule[i])
    if currentweekday == "Sat":
            print("today is saturday")
            print("your extracurriculars to do today are:")
            displayscheduleitems(satschedule)
    elif currentweekday == "Sun":
        print("today is Sunday")
        print("yor extracurriculars tody are:")
        displayscheduleitems(sunschedule)
    elif currentweekday == "Mon":
        print("today is Monday")
        print("your extracurriculars to do today are:")
        displayscheduleitems(monschedule)
    elif currentweekday == "Tue":
        print("today is Tuesday")
        print("your extracurriculars to do today are:")
        displayscheduleitems(tueschedule)
    elif currentweekday == "Wed":
        print("today is Wednesday")
        print("your extracurriculars to do today are:")
        displayscheduleitems(wedschedule)
    elif currentweekday == "Thu":
        print("today is Thursday")
        print("your extracurriculars to do today are:")
        displayscheduleitems(thuschedule)
    elif currentweekday == "Fri":
        print("today is Friday")
        print("your extracurriculars to do today are:")
        displayscheduleitems(frischedule)
    else:
        print("error in determining day")
    def moreschedules():
        mores = input("do you want to see your schedule for another day?")
        print(" ")
        if mores == "Yes" or mores == "yes":
            extraday = input("what day?")
            if extraday == "Monday" or extraday == "monday":
                print("your extracurriculars on monday:")
                displayscheduleitems(monschedule)
            elif extraday == "Tuesday" or extraday == "tuesday":
                print("your extracurriculars on tuesday:")
                displayscheduleitems(tueschedule)
            elif extraday == "Wednesday" or extraday == "wednesday":
                print("your extracurriculars on wednesday:")
                displayscheduleitems(wedschedule)
            elif extraday == "Thursday" or extraday == "thursday":
                print("your extracurriculars on thursday:")
                displayscheduleitems(thuschedule)
            elif extraday == "Friday" or extraday == "friday":
                print("your extracurriculars on friday:")
                displayscheduleitems(frischedule)
            elif extraday == "Saturday" or extraday == "saturday":
                print("your extracurriculars on saturday:")
                displayscheduleitems(satschedule)
            elif extraday == "Sunday" or extraday == "sunday":
                print("your extracurriculars on sunday:")
                displayscheduleitems(sunschedule)
            moreschedules()
    moreschedules()
#this class will tell you what your next class is 
def whatnextclass(lday):
    cmod = moddromtime(timestuff())
    #this will look at the currentclass, then look at the next mod, if it is different, it will print the class and mod, if not it will keep trying
    cclass = lday[cmod-1]
    if cclass != lday[cmod]:
        try:
            print("your next class is: ", lday[cmod], "durring mod", cmod+1)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    elif cclass != lday[cmod+1]:
        try: 
            print ("your next class is: " ,lday[cmod+1], "durring mod", cmod+2)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    elif cclass != lday[cmod+2]:
        try:
            print ("your next class is: " ,lday[cmod+2], "durring mod", cmod+3)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    elif cclass != lday[cmod+3]:
        try:
            print ("your next class is: " ,lday[cmod+3], "durring mod", cmod+4)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    elif cclass != lday[cmod+4]:
        try:
            print ("your next class is:" ,lday[cmod+4], "durring mod", cmod+5)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    elif cclass != lday[cmod+5]:
        try:
            print ("your next class is:" ,lday[cmod+5], "durring mod", cmod+6)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    elif cclass != lday[cmod+6]:
        try:
            print ("your next class is:" ,lday[cmod+6], "durring mod", cmod+7)
            print(" ")
        except:
            print("error, it is most likely in your last class")
    print(" ")
#function to input a friends frees and it will tell you when you are compatable
def classwithsomeoneelse(lday):
    theirclasses = []
    theirclasses.append(input("what is their class mod 1"))
    theirclasses.append(input("what is their class mod 2"))
    theirclasses.append(input("what is their class mod 3"))
    theirclasses.append(input("what is their class mod 4"))
    theirclasses.append(input("what is their class mod 5"))
    theirclasses.append(input("what is their class mod 6"))
    theirclasses.append(input("what is their class mod 7"))
    theirclasses.append(input("what is their class mod 8"))
    theirclasses.append(input("what is their class mod 9"))
    theirclasses.append(input("what is their class mod 10"))
    theirclasses.append(input("what is their class mod 11"))
    theirclasses.append(input("what is their class mod 12"))
    theirclasses.append(input("what is their class mod 13"))
    theirclasses.append(input("what is their class mod 14"))
    theirclasses.append(input("what is their class mod 15"))
    theirclasses.append(input("what is their class mod 16"))
    theirclasses.append(input("what is their class mod 17"))
    theirclasses.append(input("what is their class mod 18"))
    print(" ")
    for i in range(len(lday)):
        yourday = theirclasses[i]
        yourday = yourday.lower()
        myday = lday[i]
        myday = myday.lower()
        if myday == yourday:
            print("you have mod", i+1, ",", lday[i], "together")
#this function will allow the user to input terms to practice with flashacard questions
def flashcards():
    terms = []
    definitions = []
    numberofterms = int(input("how many terms do you need to study?"))
    for i in range(numberofterms):
        print("for the", i+1, "term")
        terms.append(input("term:"))
        definitions.append(input("definition:"))
    typeofquestion = input("do you want to answer with the term or definition")
    print(" ")
    if typeofquestion == "term" or typeofquestion == "Term":
        #for i in range(len(terms)):
        while(len(terms)>0):
            item = random.randint(0,len(terms)-1)
            print("the definition is", definitions[item])
            givenanswer = input("what is the term")
            if givenanswer == terms[item]:
                print("correct")
                print(" ")
                terms.remove(terms[item])
                definitions.remove(definitions[item])
            else:
                print("inccorect, the correct answer was", terms[item])
                print(" ")
    else:
       #for i in range(len(terms)):
       while (len(terms) > 0):
            item = random.randint(0,len(terms)-1)
            print("the term is", terms[item])
            givenanswer = input("what is the term")
            if givenanswer == definitions[item]:
                print("correct")
                print(" ")
                terms.remove(terms[item])
                definitions.remove(definitions[item])
            else:
                terms.append(terms[item])
                print("incorect, the correct answer was", definitions[item])
                print(" ")
    print("you have covered all the items")
    print(" ")
# this function will take the current day, see if it is a special scedule, and if not, say when the next will be 
def specialschedules():
    t = time.localtime()
    monthday = t.tm_mday
    print("today is the", monthday, "of december")
    for i in range(len(decspecialschedulemonthdays)):
        if decspecialschedulemonthdays[i] < int(monthday):
            placeholder = "placeholder"
        elif decspecialschedulemonthdays[i] == int(monthday):
            print("there is an event today")
            print("the event is", decspecialscheduleevents[i])
            print("we will operate on a", decspecialschedules[i], "schedule")
            break
        elif decspecialschedulemonthdays[i] > int(monthday):
            print("today there are no events and there are no special schedules")
            print("the next event is on the", decspecialschedulemonthdays[i], "th")
            print("the event is", decspecialscheduleevents[i], "and we will be on a", decspecialschedules[i], "schedule")
            break
    print(" ")
#this is like the special schedule function but it is for a specific day
def spicificdayscheduleandevent():
    specificmonth = input("what month (only december works at the moment, stay tuned for more months)")
    specificday = int(input("what day of the month?"))
    if specificmonth =="Dec" or specificmonth == "december" or specificmonth == "December":
        for i in range(len(decspecialschedulemonthdays)):
            if decspecialschedulemonthdays[i] == specificday:
                print("on the", specificday, "there is event", decspecialscheduleevents[i], "and opperates on a", decspecialschedules[i], "schedule")
                break
            elif decspecialschedulemonthdays[i] > specificday:
                print("there was/are no events or special schedules on", specificday)
                break
#choose what you do with the info 
def choosetodo(lday):
    print("what do you want to do")
    print("input 1 to create a to do list with mods")
    print("input 2 to see what mods you are free")
    print("input 3 to calculate your GPA")
    print("input 4 to compare your schedule with someone else")
    print("input 5 to see your next class")
    print("input 6 to schedule your extracurriculars")
    print("input 7 to create flashcards")
    print("input 8 to see the special schedule and event for a specific day")
    print("input 9 to see your schedle on a specific day")
    choosefunction = input("selection:")
    if choosefunction == "1" or choosefunction == "1 ":
        print(" ")
        toodos = todoloop()
        freescheduling(findfrees(lday), toodos)
    elif choosefunction == "2"or choosefunction == "2 ":
        print(" ")
        print("you are free mods:")
        for i in range(len(findfrees(lday))):
            print(((findfrees(lday))[i]), ",", end = " ")
        print(" ")
    elif choosefunction == "3"or choosefunction == "3 ":
        print(" ")
        gpacalculator()
    elif choosefunction == "4"or choosefunction == "4 ":
        print(" ")
        classwithsomeoneelse(lday)
    elif choosefunction == "5"or choosefunction == "5 ":
        print(" ")
        whatnextclass(lday)
    elif choosefunction == "6"or choosefunction == "6 ":
        print(" ")
        extraccurricular()
    elif choosefunction == "7"or choosefunction == "7 ":
        print(" ")
        flashcards()
    elif choosefunction == "8"or choosefunction == "8 ":
        print(" ")
        spicificdayscheduleandevent()
    elif choosefunction in ["9","9 "]:
        print(" ")
        chooseday()
    more = input("do you have anything else you want to do?")
    if more == "yes" or more == "Yes":
        print(" ")
        choosetodo(lday)
    elif more in ["1", "2", "3", "4", "5", "6", "7", "8", "9","1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]:
        print(" ")
        choosetodo(lday)
#this is the main function that should always play
#it will also redirect to other functions
def main():
    file_path = choose_file()
    read_csv(file_path)
    LetterDay = whatday()
    print(" ")
    print("today's letter day is: ", whatletterday())
    print("the current time is: ", timestuff())
    print("we are in mod", moddromtime(timestuff()))
    if type(moddromtime(timestuff())) == int or type(moddromtime(timestuff())) == float:
        print("You are currently in: ", LetterDay[int(moddromtime(timestuff())-1)])
    else:
        print("You are not in a class right now, classes have either not started or it is passing time.")
    print(" ")
    specialschedules()
    choosetodo(LetterDay)
