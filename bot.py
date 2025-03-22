def move(board_state, player_color: int):
    b, maxf = player_color, 0 # own color, max flanked
    for row in range(8):
        for col in range(8):
            if board_state[row][col]==0:
                dirs = [
                    d for d in ((-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1))
                    if row+d[0] in range(8) and col+d[1] in range(8) # exists
                    and board_state [row+d[0]] [col+d[1]] == -b # oppo color
                ] # potentially flankable directions
                flanked = 0
                for d in dirs:
                    rcst, travelled = [row,col], 0
                    while 1: # raycast
                        rcst[0] += d[0]
                        rcst[1] += d[1]
                        try: rcstate = board_state [rcst[0]] [rcst[1]]
                        except IndexError: break # ray hit border
                        if rcstate == -b: travelled += 1
                        else: # ray hit
                            if rcstate == b and travelled: flanked += travelled
                            break
                if flanked>maxf: best, maxf = (row, col), flanked
    try: return best
    except UnboundLocalError: pass # forfeit
