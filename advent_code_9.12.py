import numpy as np

def parse_input(fh:str):
    with open(f"{fh}.txt") as f:
        lines  = [x.strip("\n") for x in f.readlines()]
    array = np.zeros((len(lines), len(lines[0])))
    for i in range(0,len(lines)):
        for e in range(0, len(lines[0])):
            array[i][e] = int(lines[i][e])
    return array

def find_low_points(array):
    low_points = []
    low_points_coord = []
    for i in range(0,array.shape[0]):
        for e in range(0, array.shape[1]):
            values = get_values(array, i, e)
            low_point = True
            value = array[i,e]
            for nmr in range(0, len(values)):
                if value < values[nmr]:
                    continue
                else:
                    low_point = False
                    break
            if low_point == True:
                low_points.append(value+1)
                low_points_coord.append((i,e))
    return sum(low_points), low_points_coord
                
def get_values(array, i, e):
    if e-1 >=0:
        value_left=array[i][e-1]
    else:
        value_left = 9.0
    if i-1 >=0:
        value_up=array[i-1][e]
    else:
        value_up = 9.0
    try:
        value_right=array[i][e+1]
    except IndexError:
        value_right = 9.0
    try:
        value_down= array[i+1][e]
    except IndexError:
        value_down = 9.0
    array = np.array([value_left, value_up, value_right, value_down])
    return array

def find_basins(array,low_points_coord):
    basins = []
    array_basin = array <9.0
    for point in low_points_coord:
        visited = np.zeros((array.shape[0],array.shape[1]), dtype=bool)
        stop = False
        start = point
        visited[start[0]][start[1]] = True
        lst = []
        while stop == False:
            lst2,  visited = look_around(start,array_basin,visited)
            for el in lst2:
                if el not in lst:
                    lst.append(el)
            if len(lst) == 0:
                stop = True
                break
            start = lst[0]
            visited[start[0]][start[1]] = True
            lst.remove(start)
        basins.append(visited.sum())
    return basins
            
            
def look_around(start,array,visited):
    to_visit = []
    i,e = start
    if i == 0 and e == 0:
        if array[i][e+1] == True and visited[i][e+1] == False:
            to_visit.append((i,e+1))
        if array[i+1][e] == True and visited[i+1][e] == False:
            to_visit.append((i+1,e))
    elif i ==0 and 0< e < array.shape[1]-1: 
        if array[i][e+1] == True and visited[i][e+1] == False:
            to_visit.append((i,e+1))
        if array[i+1][e] == True and visited[i+1][e] == False:
            to_visit.append((i+1,e))
        if array[i][e-1] == True and visited[i][e-1] == False:
            to_visit.append((i,e-1))
    elif i ==0 and e == array.shape[1]-1: 
        if array[i][e-1] == True and visited[i][e-1] == False:
            to_visit.append((i,e-1))
        if array[i+1][e] == True and visited[i+1][e] == False:
            to_visit.append((i+1,e))
    elif e ==0 and i == array.shape[0]-1: 
        if array[i-1][e] == True and visited[i-1][e] == False:
            to_visit.append((i-1,e))
        if array[i][e+1] == True and visited[i][e+1] == False:
            to_visit.append((i,e+1))
    elif 0 < i <array.shape[0]-1 and e==0:
        if array[i][e+1] == True and visited[i][e+1] == False:
            to_visit.append((i,e+1))
        if array[i+1][e] == True and visited[i+1][e] == False:
            to_visit.append((i+1,e))
        if array[i-1][e] == True and visited[i-1][e] == False:
            to_visit.append((i-1,e))
    elif i == array.shape[0]-1 and e == array.shape[1]-1:
        if array[i][e-1] == True and visited[i][e-1] == False:
            to_visit.append((i,e-1))
        if array[i-1][e] == True and visited[i-1][e] == False:
            to_visit.append((i-1,e))
    elif i == array.shape[0]-1 and e>0: 
        if array[i][e+1] == True and visited[i][e+1] == False:
            to_visit.append((i,e+1))
        if array[i-1][e] == True and visited[i-1][e] == False:
            to_visit.append((i-1,e))
        if array[i][e-1] == True and visited[i][e-1] == False:
            to_visit.append((i,e-1))
    elif e == array.shape[1]-1 and i>0: 
        if array[i][e-1] == True and visited[i][e-1] == False:
            to_visit.append((i,e-1))
        if array[i+1][e] == True and visited[i+1][e] == False:
            to_visit.append((i+1,e))
        if array[i-1][e] == True and visited[i-1][e] == False:
            to_visit.append((i-1,e))
    elif 0<i< array.shape[0]-1 and 0<e< array.shape[1]-1:
        if array[i][e-1] == True and visited[i][e-1] == False:
            to_visit.append((i,e-1))
        if array[i+1][e] == True and visited[i+1][e] == False:
            to_visit.append((i+1,e))
        if array[i-1][e] == True and visited[i-1][e] == False:
            to_visit.append((i-1,e))
        if array[i][e+1] == True and visited[i][e+1] == False:
            to_visit.append((i,e+1))
    else:
        print("unknown trigger")
    return to_visit, visited
array = parse_input("day_9")
x, y = find_low_points(array)
z = find_basins(array,y)
r = 1
for i in sorted(z)[-3:]:
    r*=i
print(f"Result one: {x}, result two: {r}")
