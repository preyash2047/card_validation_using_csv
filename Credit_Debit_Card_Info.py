# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:55:30 2019

@author: Preyash2047@gmail.com
"""


import csv
import numpy as np

#csv file imported and storf in reader
reader = csv.DictReader(open("card_data.csv"))

#input card number
card_number = input("Enter the card No: ")

#global variable declaration
min_digits=0
max_digits=0
card_number_list = list(card_number)
card_number_list_reverse=card_number_list[::-1]
card_number_length=len(card_number_list)
first_digit = int(card_number_list[0])

#global variable for final output
card_provider_list_number = 0
result_found = False
card_number_digits = 0
mit_name=""

#list
start=[]
end=[]
name=[]
c_d=[]
number_length=[]
min_max_digits_list=[]

#append the list from csv
for raw in reader:
    start.append(raw['start'])
    end.append(raw['end'])
    name.append(raw['name'])
    c_d.append(raw['c_d'])
    number_length.append(raw['number_length'])

#initialize the value of min_digits & max_digits
def min_max_digits():
    global min_digits
    global max_digits
    for i in range(len(start)):
        available_length=number_length[i].split(',')
        for j in range(len(available_length)):
            min_max_digits_list.append(available_length[j])
    min_max_digits_array = np.array(min_max_digits_list) 
    np.unique(min_max_digits_array)
    min_digits=int(min(min_max_digits_array))
    max_digits=int(max(min_max_digits_array))

#list to int
def list_to_int(noofdigits): 
    str1 = ""
    return int(str1.join(noofdigits))

#card validation
def iin_identifier():
    first_six_digit = list_to_int(card_number_list[0:6])
    for i in range(len(start)):
        if(first_six_digit >= int(start[i]) and first_six_digit <= int(end[i])):
            available_length=number_length[i].split(',')
            for j in range(len(available_length)):
                if(card_number_length == int(available_length[j])):
                    global card_provider_list_number
                    card_provider_list_number = i
                    global card_number_digits
                    card_number_digits = available_length[j]
                    global result_found
                    result_found = True
                    
#Major Industry Identifier (MII) identification
def mit_identifier():
    global first_digit
    global mit_name
    switcher = { 
         1: "Airlines",
         2: "Airlines",
         3: "Travel and Entertainment",
         4: "Banking and Financial Services",
         5: "Banking and Financial Services",
         6: "Merchandising and Banking",
         7: "Petroleum",
         8: "Health care, Telecommunications",
         9: "National Assignment"
    }
    mit_name=switcher.get(first_digit, "MIT Identifier Not Found") 

#Luhn Algorithm or modulo-10 Algorithm
def luhn_algorithm():
    for i in range(card_number_length):
        if(i%2!=0 and i!=0):
            card_number_list_reverse[i]=int(card_number_list_reverse[i])*2
            #print(str(i)+" "+ str(card_number_list_reverse[i]))
            if(len(str(card_number_list_reverse[i]))==2):
                even_number_2=list(str(card_number_list_reverse[i]))
                card_number_list_reverse[i] = int(even_number_2[0])+int(even_number_2[1])
                #print("\tsubsum "+str(i)+" "+str(card_number_list_reverse[i]))
        else:
            card_number_list_reverse[i]=int(card_number_list_reverse[i])
    division_int = int(sum(card_number_list_reverse)/10)
    division_float=sum(card_number_list_reverse)/10
    if(division_int-division_float==0):
        return True
        
#initial level number length validation
def card_number_validation():
    min_max_digits()
    if(card_number_length>= min_digits and card_number_length <= max_digits and first_digit != 0):
        iin_identifier()
        mit_identifier()
        if(result_found and luhn_algorithm()):
            print("\nEntered Details are Correct\n")
            print("\nHere are the some details we know about you card")
            print("\nNo: "+card_number)
            print("\nIssuing Network: "+name[card_provider_list_number])
            print("\nType: "+c_d[card_provider_list_number]+" Card")
            print("\nCategory of the entity which issued the Card: "+mit_name)
        else:
            print("\nCard Number is Invalid\nPlease renter the number!\n")
    else:
        print("\nCard Number is Invalid\n")

#method called to run program
card_number_validation()