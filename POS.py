# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:36:55 2019

@author: Henry
"""

#start of the program
def start():
    #Categories for those 
    categories = {1:"Wine",
                  2:"Beer",
                  3:"Spirits",
                  4:"Food"}
    #program on an infinite loop
    while(0):
        item = catSelection(categories)

#allows the user to select the categories        
def catSelection(categories):
    selection = 0
    print(categories)
    print("Input your selection.")
    #Loop until a category has been selected
    while(selection==0):
        userInput = input()
        userInput = int(userInput)
            #if the user input is out of bounds
        if(userInput-1>0):
            print("That input does not exist; please try again.")
            #if the items are correct it goes through else
        else:
            genItems(userInput, categories)

#splitting between the categories available.                
def genItems(userInput, categories):
    #checking each category for the right one
    for cat in categories:
        if(cat == userInput):
            if(cat == "Wine"):
                wineSele()
            if(cat == "Beer"):
                beerSele()
            if(cat == "Spirits"):
                spiritSele()
            if(cat == "Food"):
                foodSele()