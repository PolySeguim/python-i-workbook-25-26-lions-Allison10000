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
list_data = []
unique_resteraunts = set()


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
               itemsinresteraunt +=1
     return itemsinresteraunt


#max value
def maxvalue(resteraunt_name, classification):
    values = []
    for i in resteraunts:
          if resteraunts[i]==resteraunt_name:
               values.append(classification[i])
    values.sort()
    return items[values[-1]]

#average value
def averagevalue(reteraunt_name, classification):
    values = []
    average = 0 
    for i in resteraunts:
          if resteraunts[i] == reteraunt_name:
               values.append(classification[i])
    for i in range(len(values)):
         average += values[i]
    average = average / len(values)
    return average 

#min value 
def minvalue(resteraunt_name, classification):
    minvalue = float('inf')
    for i in range(len(resteraunts)):
          if resteraunts[i]==resteraunt_name:
               if classification[i] < minvalue:
                    minvalue=classification[i]
    #values.sort()
    return minvalue

#sugars per restaurant
def sugarsperresteraunt(sugars, resteraunt_name):
    sugars_per = []
    for i in range(len(resteraunts)):
          if (resteraunts[i]==resteraunt_name):
               sugars_per.append(sugars[i])
    return sum(sugars_per)
def resteraunts_sugar_report(myresteraunt):
     report = {}
     for resteraunt in unique_resteraunts:
          total_sugars = 0 
          for i in range(len(resteraunts)):
               if resteraunts[i] == myresteraunt:
                    total_sugars += sugars[i]
          report[resteraunt]=total_sugars
     return report
#dictionary = {}
#list = []

def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)

    #resteraunt calorie report 
    report = resteraunts_sugar_report("McDonald's")
    for result in report:
        print(result, ":", report[result])
    print(resteraunts_sugar_report("Dairy Queen"))
    print("n/")

    #sugers per 
    """
    print("the total sugars for burgerking are", sugarsperresteraunt("Burger King"))
    #items per resteraunt 
    print("macdonals has", countitems("McDonald's"), "items")
    #max value for 
    print("the least caloric item at Dairy Queen is", minvalue('Dairy Queen', 'calories'))
    print("the item with the most sodium item at Carl's Jr. is", minvalue("Carl's Jr.", 'sodium'))
    print("the item with the most fat item at McDonald's is", minvalue("McDonald's", 'fat'))
    # min value 
    print("the item with the most calories at McDonald's is", maxvalue("McDonald's", 'calories'))
"""

file_path = choose_file()
read_csv(file_path)
print(minvalue("Dairy Queen", calories))#does not work
#print(sugarsperresteraunt(sugars, 'Dairy Queen'))
#print(averagevalue('Dairy Queen', calories)) #does not work 
#print(maxvalue('Dairy Queen', calories))#does not work 
#print(countitems('Dairy Queen'))

