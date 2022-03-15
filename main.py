import Othello
import copy

best_move = dict()


def MinMax(board, depth, maximize):
    if depth == 0:
        return board.EvaluationFunction()

    if maximize:
        best_value = -9999
        moves = board.ValidMoves()
        for move in moves:
            temp = copy.deepcopy(board)
            temp.TakeMove(move)
            v = MinMax(temp, depth - 1, not maximize)
            if v > best_value:
                best_value = v
                global best_move
                best_move = move
        return best_value

    else:
        best_value = 9999
        moves = board.ValidMoves()
        for move in moves:
            temp = copy.deepcopy(board)
            temp.TakeMove(move)
            v = MinMax(temp, depth - 1, not maximize)
            if v < best_value:
                best_value = v
                global best_move
                best_move = move
        return best_value


p = Othello.Othello()
p.Print()
p.Move()
