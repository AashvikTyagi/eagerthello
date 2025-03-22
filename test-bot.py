from bot import move

board = [[0 for cell in range(8)] for row in range(8)]
board[3][3], board[4][4], board[3][4], board[4][3] = -1, -1, 1, 1
forfeit = {-1:0, 1:0}

show = lambda: print('\n'.join([' '.join([['\u25A1','\u25A0','O'][[0,1,-1].index(cell)] for cell in row])for row in board]))

def fill(cell):
    row, col = cell
    clr = board[row][col]
    for d in ((-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)):
        if row+d[0] in range(8) and col+d[1] in range(8) and board[row+d[0]][col+d[1]] == -clr:
            rcst = list(cell)
            travelled = 0
            while 1: # raycast
                rcst[0] += d[0]
                rcst[1] += d[1]
                try: rcstate = board [rcst[0]] [rcst[1]]
                except IndexError: break
                if rcstate == -clr: travelled += 1
                else: # ray hit
                    if rcstate == clr and travelled:
                        rcst = list(cell) # recast
                        for i in range(travelled):
                            rcst[0] += d[0]
                            rcst[1] += d[1]
                            board [rcst[0]] [rcst[1]] = clr
                    break

print('\n\n')
show()

while 1:
    for side in (1, -1):
        color = ['black','white'][[1, -1].index(side)]
        cell = move(board,side)
        print(f"\n{color} plays {cell}:")
        if cell is None:
            forfeit[side] = 1
            print(f'({color} forfeits)')
        else:
            forfeit[side] = 0
            board[cell[0]][cell[1]] = side
            fill(cell)
        show()
    if all(forfeit.values()):
        print('game over')
        cells = [cell for row in board for cell in row]
        print(f"\n\nb: {cells.count(1)}\nw: {cells.count(-1)}")
        break