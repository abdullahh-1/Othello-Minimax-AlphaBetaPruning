import Othello
import copy


def Pairing(array):
    li = list()
    for i in range(0, len(array), 2):
        c = Othello.Pair(array[i], array[i + 1])
        li.append(c)
        print("(", array[i], ",", array[i + 1], ")")
    return li


def SearchPair(_a, _b, _l):
    for _pair in _l:
        if _a == _pair.x and _b == _pair.y:
            return True
    return False


def MinMax(board, depth, maximize, alpha, beta):
    if depth == 0:
        return board.EvaluationFunction()

    if maximize:
        best_value = -9999
        moves = board.ValidMoves('X')
        for i in range(0, len(moves), 2):
            temp = copy.deepcopy(board)  # creating new temp board to apply temp moves
            temp.TakeTurn(moves[i], moves[i + 1], 'X')
            value = MinMax(temp, depth - 1, False, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value

    else:
        best_value = 9999
        moves = board.ValidMoves('O')
        for i in range(0, len(moves), 2):
            temp = copy.deepcopy(board)
            temp.TakeTurn(moves[i], moves[i + 1], 'O')
            value = MinMax(temp, depth - 1, True, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value


def Best_move(board):
    moves = board.ValidMoves('X')
    d = dict()
    for i in range(0, len(moves), 2):
        pair = Othello.Pair(moves[i], moves[i + 1])
        temp = copy.deepcopy(board)
        temp.TakeTurn(moves[i], moves[i + 1], 'X')
        d[pair] = MinMax(temp, 2, True, -9999, 9999)
    print(d)
    for i in d:
        print(": ", i.x, ", ", i.y)
    return max(d, key=d.get)  # returns pair with highest h(f) value


user = 'O'
computer = 'X'
p = Othello.Othello()
coord = Othello.Pair(0, 0)

while p.checkCompleted() == -1:
    p.Print()
    print("User's Turn: Valid Moves => ")
    pairs = Pairing(p.ValidMoves(user))  # returns valid list of moves (x,y)
    x = int(input("Input row = "))
    y = int(input("Input column = "))
    if not SearchPair(x, y, pairs):
        b = True
        while b:
            print("Invalid Move! Try Again.")
            x = int(input("Input row = "))
            y = int(input("Input column = "))
            if SearchPair(x, y, pairs):
                b = False

    p.TakeTurn(x, y, user)  # take turn and applies flip
    p.Print()
    input("Press any key to continue...\n")
    coord = Best_move(p)
    print("\nComputer's Turn:", coord.x, ", ", coord.y)
    p.TakeTurn(coord.x, coord.y, computer)

result = p.checkCompleted()
if result == 2:
    print("Computer Won!")
elif result == 0:
    print("Game Tied!")
else:
    print("User won!")
