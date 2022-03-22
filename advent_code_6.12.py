import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def parse_input(fh:str)->list:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
        lst = [int(x) for x in lines[0].split(",")]
    return lst

def let_them_multiply(herd:list, days:int)->dict:
    dict_herd = {x:0 for x in range(0,9)}
    for fish in herd:
        if fish in dict_herd:
            dict_herd[fish] +=1
    for day in range(0, days):
        dict_herd = fish_age(dict_herd)
    return dict_herd
    
def fish_age(herd:dict)->dict:
    new_herd = {x:0 for x in range(0,9)}
    for i in herd.keys():
        if i !=0:
            new_herd[i-1]=herd[i]
    new_herd[6]=herd[0]+herd[7]
    new_herd[8]=herd[0]
    return new_herd
herd = parse_input("day_6")
aproxx = let_them_multiply(herd, 256)
res = sum(aproxx.values())