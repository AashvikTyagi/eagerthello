def move(board_state, player_color: int):
    maxf = 0 # own color, max flanked
    for row in range(8):
        for col in range(8):
            if board_state[row][col]==0: # empty cell
                dirs = [
                    d for d in ((-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1))
                    if row+d[0] in range(8) and col+d[1] in range(8) # exists
                    and board_state [row+d[0]] [col+d[1]] == -player_color # oppo color
                ] # potentially flankable directions
                flanked = 0
                for d in dirs:
                    rcst, travelled = [row,col], 0
                    while 1: # raycast
                        rcst[0] += d[0]
                        rcst[1] += d[1]
                        try: rcstate = board_state [rcst[0]] [rcst[1]]
                        except IndexError: break # ray hit border
                        if rcstate == -player_color: travelled += 1 # carry on
                        else: # ray hit own color
                            if rcstate == player_color and travelled:
                                flanked = travelled + (row in (0, 7) and col in (0,7)) # prefer corners
                            break
                if flanked>maxf: best, maxf = (row, col), flanked
    try: return best
    except UnboundLocalError: pass # forfeit
