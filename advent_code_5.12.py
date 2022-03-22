import numpy as np

def create_board()->np.array:
    board = np.zeros((1000,1000))
    return board

def parse_input(fh:str)->list:
    with open(f"{fh}.txt") as f:
        com = []
        lines = [x.strip("\n") for x in f.readlines()]
    for line in lines:
        line = line.split(" ")
        com.append((line[0], line[2]))
    return com

def form_lines(board:np.array, lines:list, all_lines:bool)->int:
    straight, diagonal = check_shape(lines)
    board = draw_line(straight,diagonal, board, all_lines)
    count = 0
    for e in range(0, board.shape[0]):
        for i in range(0, board.shape[1]):
            if board[e][i] >= 2:
                count+=1
    print(count)
    return count, straight, diagonal
            
def check_shape(lines:list)->[list,list]:
    straight = []
    diagonal = []
    for i in range(0, len(lines)):
        line = lines[i]
        start = (line[0]).split(",")
        end = line[1].split(",")
        if start[0] == end[0] or start[1] == end[1]:
            straight.append(line)
        else:
            diagonal.append(line)
    return straight, diagonal

def draw_line(straight:list,diagonal:list, board:np.array, all_lines:bool)->np.array:
    for el in straight:
        cx = sorted([int(el[0].split(",")[0]), int(el[1].split(",")[0])])
        cy = sorted([int(el[0].split(",")[1]), int(el[1].split(",")[1])])
        if cx[0] == cx[1]:
            for i in range(cy[0],cy[1]+1):
                board[i][cx[0]] +=1
        else:
            for e in range(cx[0],cx[1]+1):
                    board[cy[0]][e] +=1
    if all_lines ==True:
        for il in diagonal:
            cx = [int(il[0].split(",")[0]), int(il[1].split(",")[0])]
            cy = [int(il[0].split(",")[1]), int(il[1].split(",")[1])]
            if cx[0]<cx[1] and cy[0]<cy[1]:
                rng = cx[1]-cx[0]+1
                rng_x = [x for x in range(cx[0], cx[1]+1)]
                rng_y = [x for x in range(cy[0], cy[1]+1)]
            elif cx[0]>cx[1] and cy[0]<cy[1]:
                rng = cy[1]-cy[0]+1
                rng_x = [x for x in range(cx[0], cx[1]-1,-1)]
                rng_y = [x for x in range(cy[0], cy[1]+1)]
            elif cx[0]<cx[1] and cy[0]>cy[1]:
                rng = cx[1]-cx[0]+1
                rng_x = [x for x in range(cx[0], cx[1]+1)]
                rng_y = [x for x in range(cy[0], cy[1]-1,-1)]
            else:
                rng = cy[0]-cy[1]+1
                rng_x = [x for x in range(cx[0], cx[1]-1,-1)]
                rng_y = [x for x in range(cy[0], cy[1]-1,-1)]
            for al in range(0, rng):
                board[rng_y[al]][rng_x[al]] +=1
        else:pass
    return board

if __name__ == "__main__":
    board = create_board()
    lines = parse_input("day_5")
    x, y, z  = form_lines(board, lines, False) ### False: consider only straight lines, True: consider all lines