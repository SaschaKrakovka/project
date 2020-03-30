#!/bin/python

#  Plate_setup.py
#In this duplication I am using a simplified version.
#Update: Most likely unneeded to do panda


import numpy as np

A1 = 0
#Here I chose to implement one row at a time to make it more readable
#I will add more checks to make sure the data has the correct format
#use == for that
def createFrame(Data):
    global A1
    if hasattr(Data, "__len__"):
        A1,A2 = Data.iloc[0:2,0]
    return A1,A2
    

#  Created by Sascha Krakovka on --30032020.
#  
