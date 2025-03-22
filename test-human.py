from random import choice as r
from bot import move
from time import process_time as tc

board = [[0 for cell in range(8)] for row in range(8)] # 8x8 empty
board[3][3], board[4][4], board[3][4], board[4][3] = -1, -1, 1, 1 # starting cells

bc = r((-1,1))
hc = -bc
print(f"\n\nbot plays as {['white','black'][[-1,1].index(bc)]}")
print(f"human plays as {['white','black'][[-1,1].index(hc)]}")

def fill(cell, clr):
    row, col = cell
    for d in ((-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)):
        if row+d[0] in range(8) and col+d[1] in range(8) and board[row+d[0]][col+d[1]] == -clr:
            rcst = list(cell)
            travelled = 0
            while 1: # raycast
                rcst[0] += d[0]
                rcst[1] += d[1]
                rcstate = board [rcst[0]] [rcst[1]]
                if rcstate == -clr: travelled += 1
                else: # ray hit
                    if rcstate == clr and travelled:
                        rcst = list(cell) # recast
                        for i in range(travelled):
                            rcst[0] += d[0]
                            rcst[1] += d[1]
                            board [rcst[0]] [rcst[1]] = clr
                    break

asd = 0

while 1:
    print('\n\n'+'\n'.join([' '.join([['\u25A1','\u25A0','O'][[0,1,-1].index(cell)] for cell in row])for row in board]))
    command = input("-> ")
    if command=='b': # bot move, must be triggered by human
        try:
            start = tc()
            m = move(board,bc)
            print(f"move {m} made in {tc()-start}s")
            board[m[0]][m[1]] = bc
            asd = 1
        except:
            print('bot forfeits')
            asd = 0
        if asd:
            fill(list(m), bc)
            asd = 0
    else:
        try:
            h = [int(u) for u in command.split()]
            board[h[0]][h[1]] = hc
            fill(list(h), hc)
        except:
            print('write it right')