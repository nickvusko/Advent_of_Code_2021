# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:34:28 2021

@author: Niky
"""


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def parse_input(fh):
    with open(f"{fh}.txt") as f:
        folds = []
        lines = []
        for x in f.readlines():
            if x =="\n":
                continue
            elif x.startswith("fold"):
                x = x.strip("\n")
                x = x.split(" ")
                folds.append(x[2])
            else:
                x = x.strip("\n")
                lines.append(x)
    return lines, folds

def parse_folds(lines, folds):
    max_y, max_x = find_max(lines)
    array = np.zeros((max_y+1,max_x+1))
    for i in lines:
        i = i.split(",")
        array[int(i[1])][int(i[0])] = 1
    for e in folds:
        e = e.split("=")
        if e[0] == "y":
            up = int(e[1])
            array = fold_up(array, up)
        else:
            left = int(e[1])
            array = fold_left(array, left)
    visible_dots, array = count_dots(array)
    return array

def parse_first_fold(lines, folds):
    max_y, max_x = find_max(lines)
    array = np.zeros((max_y+1,max_x+1))
    for i in lines:
        i = i.split(",")
        array[int(i[1])][int(i[0])] = 1
    e = folds[0]
    e = e.split("=")
    if e[0] == "y":
        up = int(e[1])
        array = fold_up(array, up)
    else:
        left = int(e[1])
        array = fold_left(array, left)
    visible_dots, array = count_dots(array)
    return visible_dots

def find_max(lines):
    max_y, max_x = (0,0)
    for i in lines:
        i = i.split(",")
        if int(i[1])> max_y:
            max_y = int(i[1])
        if int(i[0])> max_x:
            max_x = int(i[0])
    return max_y, max_x

def fold_up(array, up):
    for i in range (0,up):
        for e in range (0, array.shape[1]):
            array[i][e]+=array[array.shape[0]-1-i][e]
    array_fold_up = array[:up]
    return array_fold_up
    
def fold_left(array, left):
    for i in range (0,array.shape[0]):
        for e in range (0, left):
            array[i][e]+=array[i][array.shape[1]-1-e]
    array_fold_left = array[:,:left]
    return array_fold_left

def count_dots(array):
    count = 0
    for i in range (0, array.shape[0]):
        for e in range (0, array.shape[1]):
            if array[i][e] >0:
                array[i][e] =1
                count +=1
    return count, array
x,y = parse_input("test")
z= parse_folds(x,y)
z_1 = parse_first_fold(x,y)
print(f"Result one: {z_1}")
ax = sns.heatmap(z, linewidth=0.5, square=True, cmap= "Greys")
plt.show()