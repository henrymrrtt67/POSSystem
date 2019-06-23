# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:36:55 2019

@author: Henry
"""

#start of the program
def start():
	#Categories for those 
	items = []
	categories = {1:"Wine",
				2:"Beer",
				3:"Spirits",
				4:"Food"}
	#program on an infinite loop
	dont_touch = 0
	while(dont_touch == 0):
		print("hello")
		item = catSelection(categories)
		items.append(item)
		selection =0
		while(selection == 0):
			print("Was that all you needed to put through?")
			userInput = input()
			if(userInput == "n" or userInput == "N"):
				item = catSelection(categories)
				items.append(item)
			elif(userInput == "y" or userInput == "Y"):
				final_payment(items)
				selection =1
			else:
				print("Sorry that did not register correctly, please try again")
		
#allows the user to select the categories        
def catSelection(categories):
	selection = 0
	for i in categories:
		print("{} : {}".format(i,categories.get(i)))
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
			selection = 1

def final_payment(items):
	return 0


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
start()
