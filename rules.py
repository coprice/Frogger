"""
rules.py creates all supporting functions needed for the graphics of the game
"""
#-----------------------------------------------------------------------------#

from random import randint

"""
initializes new game display
"""

def new():
    return [['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','_','_','_'],\
            ['_','_','f','_','_']]

"""
returns true if you are not going to get run over, and false if you are going
to get run over (i.e. a c is one spot above an f)
"""

def check(board):

    # transpose of game_board (columns now rows)
    board_T = list(map(list, zip(*board)))

    for column in board_T:
        for i in range(len(column) - 1):
            # if a c is above an f, return False
            if column[i] == 'c' and column[i+1] == 'f':
                return False

    # frog isn't squashed!
    return True

"""
updates board by moving o's down one row and adding one or (usually) two new
o's on first row
"""

def update(board, num_ticks):

    # transpose of game_board
    board_T = list(map(list, zip(*board)))

    # move existing o's down one spot in board
    for column in board_T:
        l = len(column)
        # for last element
        if column[l-1] == 'c':
            # remove any cars
            if column[l-2] != 'c':
                column[l-1] = '_'
        # for elements above the last
        for i in range(l-2, -1, -1):
            # move each car down one level
            if column[i] == 'c':
                column[i+1] = 'c'
                # clear top row
                if i == 0:
                    column[i] = '_'
                # clear previous cars
                elif column[i-1] != 'c':
                    column[i] = '_'

    # transpose back to normal
    new_board = list(map(list, zip(*board_T)))

    new_c1 = randint(0,4)

    # add new c's on first row, every 5 ticks
    if num_ticks % 5 == 1:
        # add 1 c
        new_board[0][new_c1] = 'c'

        if num_ticks > 100:

            # add 2 c's with probability 1/3
            if num_ticks < 300:
                if randint(0,2) == 0:

                    # get c2 unique to c1
                    new_c2 = randint(0,4)
                    while new_c2 == new_c1:
                        new_c2 = randint(0,4)

                    new_board[0][new_c2] = 'c'

            # add 2 c's with probability 1/2
            elif num_ticks < 600:
                if randint(0,1) == 0:

                    # get c2 unique to c1
                    new_c2 = randint(0,4)
                    while new_c2 == new_c1:
                        new_c2 = randint(0,4)

                    new_board[0][new_c2] = 'c'

            # add 2 c's with probability 2/3
            elif num_ticks < 1000:
                if randint(0,2) == 0 or 1:

                    # get c2 unique to c1
                    new_c2 = randint(0,4)
                    while new_c2 == new_c1:
                        new_c2 = randint(0,4)

                    new_board[0][new_c2] = 'c'

            # always add 2 c's
            else:
                # get c2 unique to c1
                new_c2 = randint(0,4)
                while new_c2 == new_c1:
                    new_c2 = randint(0,4)

                new_board[0][new_c2] = 'c'

    return new_board

"""
the following functions move the frog left, right, up, or down
"""

def move_left(board):
    for row in board:
        for i in range(len(row)):
            if row[i] == 'f':
                # frog cannot leave left extreme
                if i != 0:
                    # if there is no car, swap frog with element on left
                    if row[i-1] != 'c':
                        row[i-1] = 'f'
                        row[i] = '_'
    return board

def move_right(board):
    for row in board:
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 'f':
                # frog cannot leave right extreme
                if i != len(row) - 1:
                    # if there is no car, swap frog with element on right
                    if row[i+1] != 'c':
                        row[i+1] = 'f'
                        row[i] = '_'
    return board

def move_up(board):

    # transpose matrix (columns are now rows)
    board_T = list(map(list, zip(*board)))
    for column in board_T:
        for i in range(len(column)):
            if column[i] == 'f':
                # dont let frog go to top row (that is where cars spawn)
                if i != 1:
                    # if there is no car, swap frog with element above
                    if column[i-1] != 'c':
                        column[i-1] = 'f'
                        column[i] = '_'

    new_board = list(map(list, zip(*board_T)))
    return new_board

def move_down(board):

    # transpose matrix (columns are now rows)
    board_T = list(map(list, zip(*board)))
    for column in board_T:
        for i in range(len(column) - 1, -1, -1):
            if column[i] == 'f':
                # frog cannot leave bottom extreme
                if i != len(column) - 1:
                    # if there is no car, swap frog with element below
                    if column[i+1] != 'c':
                        column[i+1] = 'f'
                        column[i] = '_'

    new_board = list(map(list, zip(*board_T)))
    return new_board

"""
the following functions check if a car is directly to the left, to the right,
up, or down
"""

def check_left(board):
    for row in board:
        for i in range(len(row)):
            # find the frog
            if row[i] == 'f':
                # if there is a car to the left, return False, else True
                if i != 0:
                    if row[i-1] == 'c':
                        return False
                    else:
                        return True
                # return true if on left border
                else:
                    return True

def check_right(board):

    for row in board:
        for i in range(len(row) - 1, -1, -1):
            # find the frog
            if row[i] == 'f':
                # if there is a car to the right, return False, else True
                if i != len(row) - 1:
                    if row[i+1] == 'c':
                        return False
                    else:
                        return True
                # return True if on right border
                else:
                    return True

def check_up(board):

    # transpose matrix (columns are now rows)
    board_T = list(map(list, zip(*board)))
    for column in board_T:
        for i in range(len(column)):
            # find the frog
            if column[i] == 'f':
                # if there is a car above, return False, else True
                if i != 0:
                    if column[i-1] == 'c':
                        return False
                    else:
                        return True
                # if at top of the board, return False
                else:
                    return False

def check_down(board):

    # transpose matrix (columns are now rows)
    board_T = list(map(list, zip(*board)))
    for column in board_T:
        for i in range(len(column) - 1, -1, -1):
            # find the frog
            if column[i] == 'f':
                # if there is a car below, return False, else True
                if i != len(column) - 1:
                    if column[i+1] == 'c':
                        return False
                    else:
                        return True
                # return true if on bottom border
                else:
                    return True

"""
sorts a list containing (string, integer) by the size of the integer in
decreasing order
"""

def sort_scores(scores):

    sorted_scores = []

    for i in range(len(scores)):

        # trivial starting points
        current_score = -1
        current_initial = ""

        # find largest score in scores
        for initial, score in scores:
            if score > current_score:
                current_score = score
                current_initial = initial

        # add largest score/initial tuple in scores into sorted scores list
        sorted_scores.append((current_initial, current_score))

        # pop off largest score from scores list
        scores.pop(scores.index((current_initial, current_score)))

    return sorted_scores
