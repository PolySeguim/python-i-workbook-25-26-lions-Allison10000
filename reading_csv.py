import tkinter as tk
from tkinter import filedialog
import csv

#function to open dialog box that you will choose file location and file
def choose_file():
    root = tk.Tk()
    root.withdraw() #hide the main window
    file_path = filedialog.askopenfilename(filetypes = [("CSV files", "*.csv")])
    return file_path



#function that reads the csv file
resteraunts = []
items = []
types = []
serving_size = []
calories = []
fats = []
sodium = []
sugars = []


def read_csv(file_name):
        with open(file_name, mode="r", newline='', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                resteraunts.append(row['restaurant'])
                items.append(row['item'])
                types.append(row['type'])
                serving_size.append(float(row['serving_size']))
                calories.append(float(row['calories']))
                fats.append(float(row['fat']))
                sodium.append(float(row['sodium']))
                sugars.append(float(row['sugars']))



#count items 
def countitems(resteraunt_name):
     itemsinresteraunt = 0
     for i in range(len(resteraunts)):
          if (resteraunts[i]==resteraunt_name):
               items +=1
     return itemsinresteraunt


#max value
def maxvalue(resteraunt_name, classification):
    values = []
    for i in resteraunts:
          if resteraunts[i]==resteraunt_name:
               values.append(classification[i])
    values.sort()
    return items[values[-1]]


#min value 
def minvalue(resteraunt_name, classification):
    values = []
    for i in resteraunts:
          if resteraunts[i]==resteraunt_name:
               values.append(classification[i])
    values.sort()
    return items[values[1]]

#sugars per restaurant
def sugarsperresteraunt(resteraunt_name):
    sugars_per = []
    for i in range(len(resteraunts)):
          if (resteraunts[i]==resteraunt_name):
               sugars_per.append(sugars[i])
    return sum(sugars_per)

#dictionary = {}
#list = []

def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)
    #sugers per 
    print("the total sugars for burgerking are", sugarsperresteraunt("Burger King"))
    print("the total sugars for McDonald's are", sugarsperresteraunt("McDonald's"))
    print("the total sugars for Chick-fil-A are", sugarsperresteraunt("Chick-fil-A"))
    #items per resteraunt 
    print("macdonals has", countitems("McDonald's"), "items")
    print("Jack in the Box  has", countitems("Jack in the Box "), "items")
    print("Sonic has", countitems("Sonic"), "items")
    print("Dairy Queen has", countitems("Dairy Quee"), "items")
    print("Carl's Jr. has", countitems("Carl's Jr."), "items")
    #max value for 
    print("the least caloric item at Dairy Queen is", minvalue('Dairy Queen', 'calories'))
    print("the least caloric item at White Castle is", minvalue('White Castle', 'calories'))
    print("the least caloric item at Carl's Jr. is", minvalue("Carl's Jr.", 'calories'))
    print("the item with the most sodium item at Carl's Jr. is", minvalue("Carl's Jr.", 'sodium'))
    print("the item with the most fat item at McDonald's is", minvalue("McDonald's", 'fat'))
    # min value 
    print("the item with the most calories at McDonald's is", maxvalue("McDonald's", 'calories'))
    print("the item with the most calories at Dairy Queen is", maxvalue("Dairy Queen", 'calories'))
    print("the item with the most sodium at Dairy Queen is", maxvalue("Dairy Queen", 'sodim'))


main()


