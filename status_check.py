def win_check(board_state,win):
    if board_state[0] == board_state[1] == board_state[2] != 0:
        return True
    elif board_state[3] == board_state[4] == board_state[5] != 0:
        return True
    elif board_state[6] == board_state[7] == board_state[8] != 0:
        return True
    elif board_state[0] == board_state[3] == board_state[6] != 0:
        return True
    elif board_state[1] == board_state[4] == board_state[7] != 0:
        return True
    elif board_state[2] == board_state[5] == board_state[8] != 0:
        return True
    elif board_state[0] == board_state[4] == board_state[8] != 0:
        return True
    elif board_state[2] == board_state[4] == board_state[6] != 0:
        return True

def draw_check(board_state,win):
    if board_state.count(0) == 0 and not win:
        print("It's a draw!")
        return True