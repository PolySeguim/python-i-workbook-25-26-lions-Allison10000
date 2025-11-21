#for my exam project im going to do a planner that works with the mericci scedule 
#I would like to eventually add the ability to compare schedules with a teacher/other student and scheudle an appointment 
import time
import tkinter as tk
from tkinter import filedialog
import csv

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
#refines the letter day to account for any errors 
def whatday(day):
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
#determines the mod depending on the time using an annoying amount of conditionals 
def moddromtime(time1):
    #7 oclock
    if time1[-4] == "7":
        currentmod = "no mod"
    #8 oclock
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
        print(len(time1))
    #12 & 2 oclock 
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
    return day[currentmod-1]
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
#choose what you do with the info 
def choosetodo():
    choosefunction = input("what do you want to do, input 1 to create a to do list with mods")
    if choosefunction == "1":
        todoloop()
        more = input("do you have anything else you want to do?")
        if more == "yes" or more == "Yes":
            choosetodo() 
#this is the main function that will always play
#it will also redirect to other functions
def main():
    file_path = choose_file()
    read_csv(file_path)
    print("the current time is", timestuff())
    print("we are in mod", moddromtime(timestuff()))
    LetterDay = whatday(input("what letter day is it?"))
    if type(moddromtime(timestuff())) == int or type(moddromtime(timestuff())) == float:
        print("you are currently in", whatclass(LetterDay))
    else:
        print("you are not in a class right now, classes have either not started or it is passing time")
    choosetodo()

print(len(timestuff()))