import numpy as np

def parse_input(fh:str):
    with open(f"{fh}.txt") as f:
        lines  = [x.strip("\n") for x in f.readlines()]
    return lines

def parse_lines(lines):
    lst_left = []
    dict_lines = {")":0, "]":0, "}":0, ">":0}
    lst_corrupted = []
    for nmr in range(0,len(lines)):
        line = lines[nmr]
        corrupt_symbol = 0
        for e in line:
            if e in ["(", "[", "{", "<"]:
                lst_left.append(e)
            elif e == ")":
                if lst_left[-1] == "(":
                    del lst_left[-1]
                    continue
                else:
                    lst_corrupted.append(nmr)
                    corrupt_symbol = e
                    dict_lines[e]+=1
                    break
            elif e == "]":
                if lst_left[-1] == "[":
                    del lst_left[-1]
                    continue
                else:
                    lst_corrupted.append(nmr)
                    corrupt_symbol = e
                    dict_lines[e]+=1
                    break
            elif e == "}":
                if lst_left[-1] == "{":
                    del lst_left[-1]
                    continue
                else:
                    lst_corrupted.append(nmr)
                    corrupt_symbol = e
                    dict_lines[e]+=1
                    break
            else:
                if lst_left[-1] == "<":
                    del lst_left[-1]
                    continue
                else:
                    lst_corrupted.append(nmr)
                    corrupt_symbol = e
                    dict_lines[e]+=1
                    break
    return dict_lines, lst_corrupted

def parse_incomplete(lines, lst_corrupted):
    total_count_lst = []
    total_count = 0
    for nmr in range(0, len(lines)):
        if nmr in lst_corrupted:
            continue
        else:
            line = lines[nmr]
            lst_left = []
            dict_lines = {")":0, "(":0, "[":0, "]":0, "{":0, "}":0,"<":0, ">":0}
            for e in line:
                if e in ["(", "[", "{", "<"]:
                    lst_left.append(e)
                elif e == ")":
                    if lst_left[-1] == "(":
                        del lst_left[-1]
                        continue
                    else:
                        lst_corrupted.append(nmr)
                        corrupt_symbol = e
                        dict_lines[e]+=1
                        break
                elif e == "]":
                    if lst_left[-1] == "[":
                        del lst_left[-1]
                        continue
                    else:
                        lst_corrupted.append(nmr)
                        corrupt_symbol = e
                        dict_lines[e]+=1
                        break
                elif e == "}":
                    if lst_left[-1] == "{":
                        del lst_left[-1]
                        continue
                    else:
                        lst_corrupted.append(nmr)
                        corrupt_symbol = e
                        dict_lines[e]+=1
                        break
                else:
                    if lst_left[-1] == "<":
                        del lst_left[-1]
                        continue
                    else:
                        lst_corrupted.append(nmr)
                        corrupt_symbol = e
                        dict_lines[e]+=1
                        break
            for i in range(len(lst_left)-1,-1,-1):
                if lst_left[i] == "(":
                    total_count = 5*total_count+1
                elif lst_left[i] == "[":
                    total_count = 5*total_count+2
                elif lst_left[i] == "{":
                    total_count = 5*total_count+3
                else:
                    total_count = 5*total_count+4
            total_count_lst.append(total_count)
            total_count=0
    return total_count_lst
x = parse_input("day_10")
y, z = parse_lines(x)
a = parse_incomplete(x, z)
t = y[")"]*3+y["]"]*57+y["}"]*1197+y[">"]*25137
b = int((len(a))/2)
print(f"Result one: {t} , Result two: {sorted(a)[b]}")