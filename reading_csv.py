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
    maxvalue = 0
    for i in range(len(resteraunts)):
          if resteraunts[i]==resteraunt_name:
               if classification[i] > maxvalue:
                    maxvalue=classification[i]
    #values.sort()
    return maxvalue
#average value
def averagevalue(reteraunt_name, classification):
    values = []
    average = 0 
    for i in range(len(resteraunts)):
          if resteraunts[i] == reteraunt_name:
               values.append(classification[i])
    for i in range(len(values)):
         average += values[i]
    average = average / len(values)
    return round(average,1)
#min value 
def minvalue(resteraunt_name, classification):
    minvalue = 10000000
    for i in range(len(resteraunts)):
          if resteraunts[i]==resteraunt_name:
               if classification[i] < minvalue:
                    minvalue=classification[i]
    #values.sort()
    if minvalue == 10000000:
         return "error"
    else:
         return minvalue
#sugars per restaurant
def sugarsperresteraunt(sugars, resteraunt_name):
    sugars_per = []
    for i in range(len(resteraunts)):
          if (resteraunts[i]==resteraunt_name):
               sugars_per.append(sugars[i])
    return sum(sugars_per)
def resteraunts_sugar_report(myresteraunt):
     report = []
     for i in range(len(resteraunts)):
          if resteraunts[i] == myresteraunt:
               report.append(sugars[i])
     return report



def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)
    #sugers per 
    print("the total sugars for burgerking are", sugarsperresteraunt(sugars, "Burger King"))
    #items per resteraunt 
    print("macdonals has", countitems("Dairy Queen"), "items")
    print("Hardee's has", countitems("Hardee's"), "items")
    #max value for 
    print("the least caloric item at Dairy Queen is", minvalue('Dairy Queen', calories))
    print("the item with the most sodium item at Carl's Jr. is", minvalue("Carl's Jr.", sodium))
    print("the item with the most fat item at McDonald's is", minvalue("McDonald's", fats))
    # min value 
    print("the item with the most calories at McDonald's is", maxvalue("McDonald's", calories))
    print("the item with the most fat at Wendy's is", maxvalue("Wendy's", calories))
    #sugar report 
    print("the sugars of the items at White Castle are", resteraunts_sugar_report("White Castle"))


main()