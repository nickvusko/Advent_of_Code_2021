# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:31:10 2021

@author: Niky
"""
import numpy as np

def parse_input(fh):
    with open(f"{fh}.txt") as f:
        lines  = [x.strip("\n") for x in f.readlines()]
    array = np.zeros((len(lines), len(lines[0])))
    for i in range(0,len(lines)):
        for e in range(0, len(lines[0])):
            array[i][e] = int(lines[i][e])
    return array

def parse_matrix(array, steps):
    flash_total =0
    for nmr in range(0,steps):
        if sum(sum(array)) !=0.0:
            array_1 = add_step(array)
            array_1, flash = check(array)
            flash_total +=flash
        else:
            end = nmr
            break
    return array_1, flash_total, nmr
        
        
def add_step(array):
    for i in range(0,array.shape[0]):
            for e in range(0, array.shape[1]):
                array[i][e] += 1
    return array

def check(array):
    flash = 0
    flash_array = np.zeros((array.shape[0],array.shape[1]), dtype=bool)
    for i in range(0,array.shape[0]):
        for e in range(0, array.shape[1]):
            if array[i][e] >9:
                array, flash_array = flash_octopus(array, i, e, flash_array)
                flash+=1
        check_dec, check_coord = check_flash(array, flash_array)
    while len(check_coord) != 0:
        for element in check_coord:
            array, flash_array = flash_octopus(array, element[0], element[1], flash_array)
            flash +=1
            check_dec, check_coord = check_flash(array, flash_array)
    for i in range(0,array.shape[0]):
            for e in range(0, array.shape[1]):
                if array[i][e] >9:
                    array[i][e] =0
    return array, flash

def flash_octopus(array, i, e, flash_array):      
    if i ==0 and e ==0:
        array[1][0]+=1
        array[1][1]+=1
        array[0][1]+=1
        flash_array[i][e]=True
    elif i==0 and e ==(array.shape[1]-1):
        array[0][e-1]+=1
        array[1][e-1]+=1
        array[1][e]+=1
        flash_array[i][e]=True
    elif e==0 and i ==(array.shape[1]-1):
        array[i-1][0]+=1
        array[i-1][1]+=1
        array[i][1]+=1
        flash_array[i][e]=True
    elif i==array.shape[0]-1 and e ==array.shape[1]-1:
        array[i][e-1]+=1
        array[i-1][e-1]+=1
        array[i-1][e]+=1
        flash_array[i][e]=True
    elif i==0 and 0<e <array.shape[1]-1:
        array[0][e-1]+=1
        array[0][e+1]+=1
        array[1][e]+=1
        array[1][e-1]+=1
        array[1][e+1]+=1
        flash_array[i][e]=True
    elif i==array.shape[0]-1 and 0<e <array.shape[1]-1:
        array[i][e-1]+=1
        array[i][e+1]+=1
        array[i-1][e]+=1
        array[i-1][e-1]+=1
        array[i-1][e+1]+=1
        flash_array[i][e]=True
    elif 0<i<array.shape[0]-1 and e ==0:
        array[i-1][0]+=1
        array[i+1][0]+=1
        array[i-1][1]+=1
        array[i+1][1]+=1
        array[i][e+1]+=1
        flash_array[i][e]=True
    elif 0<i<array.shape[0]-1 and e ==array.shape[1]-1:
        array[i-1][e]+=1
        array[i+1][e]+=1
        array[i-1][e-1]+=1
        array[i+1][e-1]+=1
        array[i][e-1]+=1
        flash_array[i][e]=True
    else:
        array[i][e-1]+=1
        array[i-1][e-1]+=1
        array[i-1][e]+=1
        array[i-1][e+1]+=1
        array[i][e+1]+=1
        array[i+1][e+1]+=1
        array[i+1][e]+=1
        array[i+1][e-1]+=1
        flash_array[i][e]=True
    return array, flash_array

def check_flash(array, flash_array):
    check_opt = False
    check_coord = []
    for i in range(0,array.shape[0]):
        for e in range(0, array.shape[1]): 
            if array[i][e] >9 and flash_array[i][e] == False:
                check_opt = True
                check_coord.append((i,e))
    return check_opt, check_coord
x = parse_input("day_11")
y_1,z_1, nmr_1 =parse_matrix(np.array(x), 100)
print(f"Result one: {z_1}")
y_2,z_2, nmr_2 =parse_matrix(np.array(x), 1000)
print(f"Result two: {nmr_2}")