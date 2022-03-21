import numpy as np

      
def day_2_1(fh:str)->int:
    with open(f"{fh}.txt") as f:
        lines = [x for x in f.readlines()]
    f,d = 0,0
    for x in lines:
        key, value = x.split(" ")
        if key =="forward":
            f+=int(value)
        elif key =="down":
            d+=int(value)
        else:
            d-=int(value)
    return f*d

def day_2_2(fh:str)->int:
    with open(f"{fh}.txt") as f:
        lines = [x for x in f.readlines()]
    f,d,a = 0,0,0
    for x in lines:
        key, value = x.split(" ")
        if key =="forward":
            f+=int(value)
            d +=(int(value)*a)
        elif key =="down":
            a+=int(value)
        else:
            a-=int(value)
    return f*d
            
x= day_2_1("day_2")
y= day_2_2("day_2")