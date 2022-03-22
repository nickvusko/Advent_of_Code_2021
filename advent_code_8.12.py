import numpy as np

def parse_input(fh:str):
    with open(f"{fh}.txt") as f:
        lines  = [x.strip("\n").split("|") for x in f.readlines()]
        lines_digit = [x[0] for x in lines]
        lines_output = [x[1] for x in lines]
    return lines_digit, lines_output

def decode(lines_digit, lines_output):
    lst_to_sum = []
    for eks in range(0, len(lines_digit)):
        linex = lines_digit[eks]
        codes =  read_line(linex)
        line = lines_output[eks]
        digits = line.split(" ")
        digits.remove("")
        string = ""
        for digit in digits:
            for key, value in codes.items():
                if len(digit) == len(value) and check_key(digit,value) == True:
                    string = string+str(key)
                    break
        lst_to_sum.append(int(string))
    suma = sum(lst_to_sum)
    return suma

def check_key(digit,value):
    for i in value:
        bo = True
        if i in digit:
            continue
        else:
            bo = False
            break
    return bo

def read_line(line):
    line = line.split(" ")
    line.remove("")
    codes = {}
    to_decode = []
    for el in line:
        if len(el) == 2:
            codes[1] = el
        elif len(el) == 3:
            codes[7] = el
        elif len(el) == 4:
            codes[4] = el
        elif len(el) == 7:
            codes[8] = el
        else:
            to_decode.append(el)
    codes = guess_number(codes, to_decode)
    return codes
    
def guess_number(codes,to_decode):
    for ele in range(0, len(to_decode)):
        el = to_decode[ele]
        if len(el) == 6:
            codes, to_decode, found = check_6(el, codes, to_decode)
            if found == True:
                continue
            codes, to_decode = check_9(el, codes, to_decode)
    to_decode.remove(codes[6])
    to_decode.remove(codes[9])
    to_decode.remove(codes[0])
    for ele in range(0, len(to_decode)):
        el = to_decode[ele]
        codes, to_decode, found = check_3_5(el, codes, to_decode)
    to_decode.remove(codes[3])
    to_decode.remove(codes[5])
    codes[2] = to_decode[0]
    to_decode.remove(codes[2])
    return codes
                        
def check_6(el,codes, to_decode):
    found = False
    for l in codes[1]:
        if l in el:
            continue
        else:
            codes[6] = el
            found = True
            break
    return codes, to_decode, found
                            
def check_9(el,codes, to_decode):
    found = True
    for l in codes[4]:
        if l in el:
            pass
        else:
            found = False
            break
    if found == True:
        codes[9] = el
    else:
        codes[0] = el
    return codes, to_decode            

def check_3_5(el,codes, to_decode):
    found = True
    for l in el:
        if l in codes[9]:
            pass
        else:
            found = False
            break
    if found == True:
        found_1 = True
        for ax in codes[1]:
            if ax in el:
                pass
            else:
                found_1 = False
                break
        if found_1 == True:
            codes[3] = el
        else:
            codes[5] = el
    return codes, to_decode , found
    
def part_one(lines):
    count = 0
    for line in lines:
        digits = line.split(" ")
        try:
            digits.remove("")
        except ValueError:
            pass
        for digit in digits:
            if len(digit) in [2,3,4,7]:
                count +=1
    return count

lines_digit, lines_output= parse_input("day_8")
result_1 = part_one(lines_output)
result_2 = decode(lines_digit, lines_output)