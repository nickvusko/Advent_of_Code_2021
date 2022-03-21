import numpy as np


def day3_1(fh:str)->int:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    mr_cahr = len(lines[0])
    condition_oxy = str()
    condition_co = str()
    lst_of = [x for x in lines]
    for i in range(0,mr_cahr):
        ones = 0
        ous = 0
        for e in range(0,len(lst_of)):
            if lst_of[e][i] == "1":
                ones+=1
            else:
                ous +=1
        if ones >= ous:
            condition_oxy += "1"
            condition_co+="0"
        else:
            condition_oxy += "0"
            condition_co +="1"
        if len(lst_of) != 1:
            continue
        else:
            break
    return int(condition_oxy,2)* int(condition_co,2)


def day3_2(fh)->int:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    mr_cahr = len(lines[0])
    lst_of = [x for x in lines]
    starts_with=str()
    for i in range(0,mr_cahr):
        ones = 0
        ous = 0
        for e in range(0,len(lst_of)):
            if lst_of[e][i] == "1":
                ones+=1
            else:
                ous +=1
        if ones >= ous:
            starts_with += "1"
            lst_of = [x for x in lst_of if x.startswith(starts_with)]
        else:
            starts_with += "0"
            lst_of = [x for x in lst_of if x.startswith(starts_with)]
        if len(lst_of) != 1:
            continue
        else:
            condition_oxy=lst_of[0]
            break
    lst_of = [x for x in lines]
    starts_with=str()
    for i in range(0,mr_cahr):
        ones = 0
        ous = 0
        for e in range(0,len(lst_of)):
            if lst_of[e][i] == "1":
                ones+=1
            else:
                ous +=1
        if ones >= ous:
            starts_with += "0"
            lst_of = [x for x in lst_of if x.startswith(starts_with)]
        else:
            starts_with += "1"
            lst_of = [x for x in lst_of if x.startswith(starts_with)]
        if len(lst_of) != 1:
            continue
        else:
            condition_co=lst_of[0]
            break
    return int(condition_oxy,2)* int(condition_co,2)
    
result_day_3_1=day3_1("day_3")
result_day_3_2= day3_2("day_3")
