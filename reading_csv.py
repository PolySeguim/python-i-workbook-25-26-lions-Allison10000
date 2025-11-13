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
                fats.append(float(row['fats']))
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
def minvalue(resteraunt_name, classification):
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

#sugars per resteraunt
def sugarsperresteraunt(resteraunt_name):
    sugars_per = {}
    for i in range(len(resteraunts)):
          if (resteraunts[i]==resteraunt_name):
               sugars_per.append(sugars[i])
    return sum(sugars_per)



def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)
    #sugers per 
    print("sugars for burgerking ", sugarsperresteraunt(sugars, "Burger King"))
    #items per resteraunt 
    print("macdonals has", countitems("Macdonalds"), "items")
    #max value for 

file_path = choose_file()
read_csv(file_path)
print(sugarsperresteraunt('Burger King'))



