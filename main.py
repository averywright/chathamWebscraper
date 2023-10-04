import numpy as np
import time
import random


def new_game():
    import numpy as np
    board = np.zeros((4, 4))

    board = new_number(board)
    board = new_number(board)

    return board


def sig(z):
    import numpy as np
    return 1.0/(1.0+np.exp(-z))


def new_number(board):
    import numpy as np

    board_list = np.reshape(board, 16)
    index = np.arange(16)
    empty_squares = index[np.where(board_list == 0)]
    number_loc = np.random.choice(empty_squares)

    two_or_four = np.random.rand()
    if two_or_four <= 0.9:
        board_list[number_loc] = 2
    else:
        board_list[number_loc] = 4

    board = np.reshape(board_list, (4, 4))
    return board


def move_left(board):
    import numpy as np
    for row_ind in np.arange(4):
        row = board[row_ind,]

        # "Slide" numbers left and fill in with zeros
        non_zeros = row[np.where(row != 0)]
        row = np.append(non_zeros, [0, 0, 0, 0])
        row = row[:4]

        # Combine matching numbers
        for i in np.arange(len(non_zeros) - 1):
            if row[i] == row[i + 1]:
                row[i] = 2 * row[i]
                row[i + 1] = 0

        # "Slide" numbers left and fill in with zeros
        non_zeros = row[np.where(row != 0)]
        row = np.append(non_zeros, [0, 0, 0, 0])
        row = row[:4]

        board[row_ind,] = row

    return board


def move_right(board):
    import numpy as np
    board = np.fliplr(board)
    board = move_left(board)
    board = np.fliplr(board)
    return board


def move_up(board):
    import numpy as np
    board = np.rot90(board)
    board = move_left(board)
    board = np.rot90(board, 3)
    return board


def move_down(board):
    import numpy as np
    board = np.rot90(board, 3)
    board = move_left(board)
    board = np.rot90(board)
    return board


def can_play(board):
    import numpy as np
    play = True
    if np.all(board.copy() == move_left(board.copy())):
        if np.all(board.copy() == move_up(board.copy())):
            if np.all(board.copy() == move_right(board.copy())):
                if np.all(board.copy() == move_down(board.copy())):
                    play = False
    return play


def evaluation(z, score, board):
    score -= .5

    for i in z:
        for j in i:
            score += (j ** 2) / 1000
            if j != 0:
                score -= 5

    if not can_play(z):
        score -= 100

    return score


tab = []
finalTab = []


def finalGame(tab):
    board = new_game()
    tab = []
    keep_going = True
    score = 0
    board_old = []
    move = ''
    while keep_going:
        oldscore = score
        tab.append(board_old)
        tab.append(move)
        tab.append(evaluation(board, oldscore, board))

        board_old = board.copy()
        playboard1 = board
        playboard2 = board
        playboard3 = board
        playboard4 = board

        print(board_old)

        evaluatedList = np.array([evaluation(move_up(playboard1), oldscore, board), evaluation(move_down(playboard2), oldscore, board), evaluation(move_left(playboard3), oldscore, board), evaluation(move_right(playboard4), oldscore, board)])
        if np.max(evaluatedList) == evaluatedList[0]:
            move = 'u'
        elif np.max(evaluatedList) == evaluatedList[1]:
            move = 'd'
        elif np.max(evaluatedList) == evaluatedList[2]:
            move = 'l'
        elif np.max(evaluatedList) == evaluatedList[3]:
            move = 'r'

        print(evaluatedList)

        counter = 0
        count = 0
        if finalTab != []:
            for i in finalTab:
                count += 1
                try:
                    for j in i:
                        counter += 1
                        try:
                            if np.all(j) == np.all(board):
                                if finalTab[count] < 4000:
                                    g = random.randint(1, 3)
                                    if i[counter] == 'l':
                                        if g == 1:
                                            move = 'u'
                                        if g == 2:
                                            move = 'r'
                                        if g == 3:
                                            move = 'd'
                                    if i[counter] == 'r':
                                        if g == 1:
                                            move = 'u'
                                        if g == 2:
                                            move = 'l'
                                        if g == 3:
                                            move = 'd'
                                    if i[counter] == 'u':
                                        if g == 1:
                                            move = 'l'
                                        if g == 2:
                                            move = 'r'
                                        if g == 3:
                                            move = 'd'
                                    if i[counter] == 'd':
                                        if g == 1:
                                            move = 'u'
                                        if g == 2:
                                            move = 'r'
                                        if g == 3:
                                            move = 'l'
                        except:
                            error = True
                except:
                    error = True

        stoppedgame = random.randint(0, 1000)
        if stoppedgame == 5:
            move = 'l'
        if stoppedgame == 50:
            move = 'r'
        if stoppedgame == 75:
            move = 'd'
        if stoppedgame == 80:
            move = 'u'

        if np.all(board_old) == np.all(board):
            stoppedgame = random.randint(5, 10)
            if stoppedgame == 5:
                move = 'l'
            if stoppedgame == 6:
                move = 'r'
            if stoppedgame == 7:
                move = 'd'
            if stoppedgame == 8:
                move = 'u'

        if move == 'l':
            board = move_left(board)
        elif move == 'u':
            board = move_up(board)
        elif move == 'r':
            board = move_right(board)
        elif move == 'd':
            board = move_down(board)

        if not np.all(board_old == board):
            board = new_number(board)

        if not can_play(board):
            keep_going = False

        if np.max(board) == 2048:
            input('Woohoo! You won!')
            print(board_old)
            keep_going = False

    return tab


for i in range(1000):
    tab = []
    finalTab.append(finalGame(tab))
    for i in finalTab:
        try:
            for j in i:
                if j == i[len(i)-1]:
                    finalTab.append(j)
        except:
            print('e')






