# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:42:18 2019

@author: acer
"""
"""############################################################################
                            Assignment 5
##############################################################################
1. Write a function to compute 5/0 and use try/except to catch the exceptions. 
"""    
    
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print( 'division by zero')

"""
2. Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
Hint: Subject,Verb and Object should be declared in the program as shown below. 
subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"] 



subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)
 """