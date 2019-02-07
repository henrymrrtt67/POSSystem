# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:36:55 2019

@author: Henry
"""

def start():
    categories = {1:"Wine",
                  2:"Beer",
                  3:"Spirits",
                  4:"Food"}
    while(0):
        item = catSelection(categories)
        
def catSelection(categories):
    selection = 0
    print("Input your selection.")
    while(selection==0):
        userInput = input()
        userInput = int(userInput)
            if(userInput-1<0 && userInput-1>3):
                print("That input does not exist; please try again.")
            else:
                items(userInput, categories)
                
def genItems(userInput, categories):
    for(i in categories):
        if(i == userInput):