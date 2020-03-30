#!/bin/python

#  Plate_setup.py
#  This will be a module to implement the below given naming unto a data frame
#Update: most likely unneeded due to panda in its current version. Will see where I go with this.
import numpy as np


#Here I chose to implement one row at a time to make it more readable
#I will add more checks to make sure the data has the correct format
def createFrame(Data):
    if hasattr(Data, "__len__"):
        A1,B1,C1,D1,E1,F1,G1,H1 = Data.iloc[1:9,1]
        A2,B2,C2,D2,E2,F2,G2,H2 = Data.iloc[1:9,2]
        A3,B3,C3,D3,E3,F3,G3,H3 = Data.iloc[1:9,3]
        A4,B4,C4,D4,E4,F4,G4,H4 = Data.iloc[1:9,4]
        A5,B5,C5,D5,E5,F5,G5,H5 = Data.iloc[1:9,5]
        A6,B6,C6,D6,E6,F6,G6,H6 = Data.iloc[1:9,6]
        A7,B7,C7,D7,E7,F7,G7,H7 = Data.iloc[1:9,7]
        A8,B8,C8,D8,E8,F8,G8,H8 = Data.iloc[1:9,8]
        A9,B9,C9,D9,E9,F9,G9,H9 = Data.iloc[1:9,9]
        A10,B10,C10,D10,E10,F10,G10,H10 = Data.iloc[1:9,10]
        A11,B11,C11,D11,E11,F11,G11,H11 = Data.iloc[1:9,11]
        A12,B12,C12,D12,E12,F12,G12,H12 = Data.iloc[1:9,12]
    return Data


#  Created by Sascha Krakovka on --30032020.
#  
