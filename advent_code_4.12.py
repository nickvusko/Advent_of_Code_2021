import numpy as np
def get_tables(fh:str)->[list, list, list]:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    draw_line = ([x for x in lines[0].split(",")])
    lst_tables = []
    lst_scores = [np.zeros((5,5)) for x in range(0,100)]
    for i in range(2,600,6):
        meta = lines[i:i+5]
        A = np.empty([5,5])
        for x in range(0, len(meta)):
            line = meta[x].split(" ")
            parse = False
            while parse == False:
                try:
                    line.remove("")
                    parse = False
                    pass
                except ValueError:
                    parse = True
                    pass
                B = np.asarray(line)
            A[x] = B
        lst_tables.append(A)
    return lst_tables, lst_scores, draw_line


def draw_and_search(tables:list, scores:list, draw:list)->[list, list]:
    lst_of_bingos =[]
    bingos = []
    for bingo_number in draw:
        idx =0
        while idx < len(tables):
            table = tables[idx]
            found, table = is_value_in(bingo_number, table)
            bingo = check_bingo(table)
            if bingo == True:
                lst_of_bingos.append(table)
                bingos.append(bingo_number)
                del tables[idx]
            else:
                idx+=1
    return lst_of_bingos, bingos

def is_value_in(bingo_number:str, table:np.array)->[bool, np.array]:
    found = False
    for r in range(0,5):
        for c in range(0,5):
            if float(bingo_number) == float(table[r][c]):
                table[r][c] = np.nan
                found = True
                break
            else:continue
        if found == True:
            break
        else:continue
    return found, table

def check_bingo(table:np.array)->bool:
    bingo = False
    for r in range(0,5):
        if np.all(np.isnan(table[r]))== True:
            bingo = True
            break
        else:pass
    if bingo == True:
        pass
    else:
        for c in range(0,5):
            if np.all(np.isnan(table[:,c]))== True:
                bingo = True
                break
            else:continue
    return bingo
            
def count_score(lst_of_bingos:list, bingos:list)->float:
    table = lst_of_bingos[0] ###change to position -1 for the second part if the assignment
    bingo = bingos[0] ###change to position -1 for the second part if the assignment
    unmarked_sum = 0
    table = np.nan_to_num(table)
    print(table)
    for r in range(0,5):
        unmarked_sum += np.sum(table[r])
    print(unmarked_sum, bingo)
    return int(bingo)*unmarked_sum

tables, scores, draw = get_tables("day_4")
lst_of_bingos, bingos = draw_and_search(tables, scores, draw)
print(count_score(lst_of_bingos, bingos))