import numpy as np
import math
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



weights = np.random.rand(4, 16)
bias = np.zeros(4)

def play_game(weights, bias):
    import numpy as np
    board = new_game()

    keep_going = True
    while keep_going:
        board_old = board.copy()
        print(board_old)

        """This section is to evaluate the board. Sum of board is divided by tiles occupied."""

        counter = 0
        score1 = 0
        hypothetical1 = move_left(board)
        for i in hypothetical1 != 0:
            if i == 'True':
                counter += 1
        score1 = (np.sum(hypothetical1) - np.sum(board)) / counter

        counter = 0
        score2 = 0
        hypothetical2 = move_up(board)
        for i in hypothetical2 != 0:
            if i == 'True':
                counter += 1
        score2 = (np.sum(hypothetical2) - np.sum(board)) / counter

        score3 = 0
        hypothetical3 = move_right(board)
        for i in hypothetical3 != 0:
            if i == 'True':
                counter += 1
        score3 = (np.sum(hypothetical3) - np.sum(board)) / counter

        score4 = 0
        hypothetical4 = move_down(board)
        for i in hypothetical4 != 0:
            if i == 'True':
                counter += 1
        score4 = (np.sum(hypothetical4) - np.sum(board)) / counter

        juxtaposed = np.array([score1, score2, score3, score4])

        if score1 == np.max(juxtaposed):
            bias[0] += 1
            biases2[0] += 1
            biases3[0] += 1
            bias[1] -= 1
            biases2[1] -= 1
            biases3[1] -= 1
            bias[3] -= 1
            biases2[3] -= 1
            biases3[3] -= 1
            bias[2] -= 1
            biases2[2] -= 1
            biases3[2] -= 1
        if score2 == np.max(juxtaposed):
            bias[1] += 1
            biases2[1] += 1
            biases3[1] += 1
            bias[0] -= 1
            biases2[0] -= 1
            biases3[0] -= 1
            bias[3] -= 1
            biases2[3] -= 1
            biases3[3] -= 1
            bias[2] -= 1
            biases2[2] -= 1
            biases3[2] -= 1
        if score3 == np.max(juxtaposed):
            bias[2] += 1
            biases2[2] += 1
            biases3[2] += 1
            bias[0] -= 1
            biases2[0] -= 1
            biases3[0] -= 1
            bias[3] -= 1
            biases2[3] -= 1
            biases3[3] -= 1
            bias[2] -= 1
            biases2[2] -= 1
            biases3[2] -= 1
        if score4 == np.max(juxtaposed):
            bias[3] += 1
            biases2[3] += 1
            biases3[3] += 1
            bias[0] -= 1
            biases2[0] -= 1
            biases3[0] -= 1
            bias[1] -= 1
            biases2[1] -= 1
            biases3[1] -= 1
            bias[2] -= 1
            biases2[2] -= 1
            biases3[2] -= 1


        inputs = board.reshape(16, 1)

        firstLayer1 = sig(np.sum(np.dot(weights[0], inputs)) + bias[0])
        firstLayer2 = sig(np.sum(np.dot(weights[1], inputs)) + bias[1])
        firstLayer3 = sig(np.sum(np.dot(weights[2], inputs)) + bias[2])
        firstLayer4 = sig(np.sum(np.dot(weights[3], inputs)) + bias[3])

        firstLayer = sig(np.array([[firstLayer1],
                                   [firstLayer2],
                                   [firstLayer3],
                                   [firstLayer4]]))

        inputs2 = firstLayer.reshape(4, 1)

        secondLayer1 = sig(np.sum(np.dot(weights2[0], inputs2)) - biases2[0])
        secondLayer2 = sig(np.sum(np.dot(weights2[1], inputs2)) - biases2[1])
        secondLayer3 = sig(np.sum(np.dot(weights2[2], inputs2)) - biases2[2])
        secondLayer4 = sig(np.sum(np.dot(weights2[3], inputs2)) - biases2[3])

        secondLayer = sig(np.array([[secondLayer1],
                                    [secondLayer2],
                                    [secondLayer3],
                                    [secondLayer4]]))

        inputs3 = secondLayer.reshape(4, 1)

        thirdLayer1 = sig(np.sum(np.dot(weights3[0], inputs3)) - biases3[0])
        thirdLayer2 = sig(np.sum(np.dot(weights3[1], inputs3)) - biases3[1])
        thirdLayer3 = sig(np.sum(np.dot(weights3[2], inputs3)) - biases3[2])
        thirdLayer4 = sig(np.sum(np.dot(weights3[3], inputs3)) - biases3[3])

        thirdLayer = np.array([[thirdLayer1],
                                   [thirdLayer2],
                                   [thirdLayer3],
                                   [thirdLayer4]])

        if thirdLayer1 > thirdLayer2 and thirdLayer1 > thirdLayer3 and thirdLayer1 > thirdLayer4:
            move = 'l'

        elif thirdLayer2 > thirdLayer1 and thirdLayer2 > thirdLayer3 and thirdLayer2 > thirdLayer4:
            move = 'u'

        elif thirdLayer3 > thirdLayer2 and thirdLayer3 > thirdLayer2 and thirdLayer3 > thirdLayer4:
            move = 'r'

        elif thirdLayer4 > thirdLayer2 and thirdLayer4 > thirdLayer3 and thirdLayer4 > thirdLayer1:
            move = 'd'

        l = 0
        u = 0
        r = 0
        d = 0

        if move == 'l':
            board = move_left(board)
            l += 1
        elif move == 'u':
            board = move_up(board)
            u += 1
        elif move == 'r':
            board = move_right(board)
            r += 1
        elif move == 'd':
            board = move_down(board)
            d += 1
        else:
            print('Oops!! This input is not recognized')
        # verify that board changed before adding new random number
        if not np.all(board_old == board):
            board = new_number(board)
        print(l, r, u, d)
        if np.all(board_old == board):
            if move == 'l':
                weights[0] = np.random.randn(1, 16)
                weights2[0] = np.random.randn(1, 4)
                weights3[0] = np.random.randn(1, 4)
                bias[0] += .01
                biases2[0] += .01
                biases3[0] += .01
            elif move == 'u':
                weights[1] = np.random.randn(1, 16)
                weights2[1] = np.random.randn(1, 4)
                weights3[1] = np.random.randn(1, 4)
                bias[1] += .01
                biases2[1] += .01
                biases3[1] += .01
            elif move == 'r':
                weights[2] = np.random.randn(1, 16)
                weights2[2] = np.random.randn(1, 4)
                weights3[2] = np.random.randn(1, 4)
                bias[2] += .01
                biases2[2] += .01
                biases3[2] += .01
            elif move == 'd':
                weights[3] = np.random.randn(1, 16)
                weights2[3] = np.random.randn(1, 4)
                weights3[3] = np.random.randn(1, 4)
                bias[3] += .01
                biases2[3] += .01
                biases3[3] += .01
        if not can_play(board):
            keep_going = False
            print(board)
        if np.max(board) == 2048:
            print(board_old)
            keep_going = False

    return weights, biases
