import numpy as np


def day_1_1(fh:str):
    with open(f"{fh}.txt") as f:
        lines = f.readlines()
    np_array = np.asarray([int(x) for x in lines])
    loops = len (np_array)
    count = 0
    for i in range(0,loops-1,):
        x,y = np_array[i],np_array[i+1]
        if y> x:
            count+=1
    return count

def day_1_2(fh:str):
    with open(f"{fh}.txt") as f:
        lines = f.readlines()
    np_array = np.asarray([int(x) for x in lines])
    loops = len (np_array)
    count = 0
    for i in range(0,loops-1,):
        x,y = sum(np_array[i:i+3]),sum(np_array[i+1:i+4])
        if y> x:
            count+=1
    return count
            
x=day_1_1("day_1")
y = day_1_2("day_1")