
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:03:19 2018

@author: ameanasad
"""
import numpy as np
import math

def system_initialization():
     n = int(input("How many variables is in the system?" + " "))     
     matrix = np.zeros((1,n+1), dtype= float)     
     tot_functions = []     
     for func in range(0,n):         
         function = [float(x) for x in input("Enter Coefficients for function " + str(func + 1) + ": ").split(",")]
         tot_functions.append(function)    
     for row in tot_functions:
         matrix = np.vstack([matrix, row])        
     matrix = np.delete(matrix, (0), axis = 0)   
     return matrix 
     
def augmented_matrix_formation():
    matrix = system_initialization()
    n = len(matrix)
    row_index = 0
    augmented_list = []  
    augmented_matrix = np.zeros((1, n+1), dtype = float)
    for r in range(n):
        row_index = row_index + 1
        for z in range(n):
            if all(coeff == 0 for coeff in matrix[z][0:row_index]):
               pass
            else:
                temp=  matrix[z].tolist() 
                if temp not in augmented_list:
                    augmented_list.append(temp)
    for row in augmented_list:
        augmented_matrix = np.vstack([augmented_matrix, row])      
    augmented_matrix = np.delete(augmented_matrix, (0), axis = 0)           
    return augmented_matrix

def row_echelon_form():  
    print("Transfering Matrix into Row Echelon Form\n")
    array = augmented_matrix_formation()
    length = len(array)
    n = 1
    for index in range(length-1):    
        for r in range(n,length):
                if array[n-1][index] == 0:
                    print('Swap row'+ ' '  + str(r)  + "with row"  + " " + str(r-1))
                    print(" ")
                    temp = array[r].copy()
                    array[r]= array[r-1].copy()
                    array[r-1] = temp
                    print(np.round(array,2))
                    
                if array[r][index] != 0:
                    mult = array[r][index]/array[index][index]
                    print(str(mult) +  " " + " times Row" + " " + str(r) + " " + "added to Row" + " " + str(index))
                    print(" ")
                    array[r] = -mult*array[index] + array[r]
                    print(np.round(array,2))
        n = n + 1
    return array

def back_substitution():
    print("Performing Back Substitution\n")
    array = row_echelon_form()
    n = len(array)
    c = 2
    x_values = []
    idx = 3
    x1 = array[n-1][n]/array[n-1][n-1]
    x_values.append(x1)
    for x in range(2,n+1):
        c = c+1
        coefficients = array[-x][-c:]
        num = 0
        idx = 0
        for x in reversed(coefficients[1:-1]):
            num = num + x*x_values[idx]
            idx = idx +1
        new_x = (coefficients[-1] - num)/coefficients[0]
        x_values.append(new_x)
        
    for num in reversed(x_values):
        print("x" + str(x_values.index(num) + 1) + " " + "=" + " " + str(round(num,3)))
    return x_values

back_substitution()        
        
        
        
    

"""


Enter Coefficients for function 1: 2,-7,3,5,-7,11,8,114

Enter Coefficients for function 2: 13,11,8,7,4,2,1,-25

Enter Coefficients for function 3: 12,1,6,5,9,3,11,-37

Enter Coefficients for function 4: 5,7,-1,9,-6,3,-5,-11

Enter Coefficients for function 5: 1,-4,7,-3,9,-2,6,4

Enter Coefficients for function 6: -7,-2,5,1,9,3,-4,-50

Enter Coefficients for function 7:  4,1,-6,-3,8,-7,-4,-91

"""

