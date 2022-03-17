class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y


def isValid(i, j):
    if 0 <= i < 8 and 0 <= j < 8:
        return True
    return False


class Othello:
    Board = [[], [], [], [], [], [], [], []]

    def __init__(self):
        self.Board = [[" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", "X", "O", " ", " ", " "],
                      [" ", " ", " ", "O", "X", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "]]

    def Print(self):
        u_score = 0
        c_score = 0
        print("-------------------------------------------------")
        for i in range(8):
            print("|", end="  ")
            for j in range(8):
                print(self.Board[i][j], end="  |  ")
                if self.Board[i][j] == 'O':
                    u_score += 1
                if self.Board[i][j] == 'X':
                    c_score += 1
            print("\n-------------------------------------------------")
        print("User's Score = ", u_score)
        print("Computer's Score = ", c_score)

    def counter(self):
        c = [0, 0]  # index 0 for User, index 1 for AI
        for i in range(8):
            for j in range(8):
                if self.Board[i][j] == 'O':
                    c[0] += 1
                elif self.Board[i][j] == 'X':
                    c[1] += 1
        return c

    def checkCompleted(self):
        for i in range(len(self.Board)):
            for j in range(len(self.Board[i])):
                if self.Board[i][j] == ' ':
                    return -1

        count = self.counter()
        user = count[0]
        comp = count[1]
        if comp > user:
            return 2
        elif comp == user:
            return 0
        elif comp < user:
            return 1

    def ValidMoves(self, turn):  # returns list as x1, y1, x2, y2
        pair = []
        if turn == 'X':
            opp = 'O'
        else:
            opp = 'X'

        # check Vertically
        for j in range(len(self.Board[0])):
            var = False
            va2 = False
            for i in range(len(self.Board)):
                if self.Board[i][j] == turn:
                    var = True
                    var2 = False
                    continue

                if var and self.Board[i][j] == opp:
                    va2 = True
                    continue

                if var and va2 and self.Board[i][j] == " ":
                    pair.append(i)
                    pair.append(j)
                var = False
                va2 = False

        # check Vertically Reversed
        for j in range(len(self.Board[0]) - 1, 0, -1):
            var = False
            va2 = False
            for i in range(len(self.Board) - 1, 0, -1):
                if self.Board[i][j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[i][j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    pair.append(i)
                    pair.append(j)
                var = False
                va2 = False

        # check Horizontally
        for i in range(len(self.Board)):
            var = False
            va2 = False
            for j in range(len(self.Board[0])):
                if self.Board[i][j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[i][j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    pair.append(i)
                    pair.append(j)
                var = False
                va2 = False

        # check Horizontally Reversed
        for i in range(len(self.Board) - 1, 0, -1):
            var = False
            va2 = False
            for j in range(len(self.Board[0]) - 1, 0, -1):
                if self.Board[i][j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[i][j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    pair.append(i)
                    pair.append(j)
                var = False
                va2 = False

        # Diagonals
        for i in range(8):  # left top to right bottom (upper half)
            var = False
            va2 = False
            for j in range(8):
                if (j + i) > 7:
                    break
                if self.Board[j][j + i] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[j][j + i] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[j][j + i] == " ":
                    pair.append(j)
                    pair.append(j + i)
                var = False
                va2 = False

        for i in range(1, 8):  # left top to right bottom (bottom half)
            var = False
            va2 = False
            for j in range(8):
                if (j + i) > 7:
                    break
                if self.Board[j + i][j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[j + i][j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[j + i][j] == " ":
                    pair.append(j + i)
                    pair.append(j)
                var = False
                va2 = False

        for i in range(0, 8):
            var = False
            va2 = False
            for j in range(7, -1, -1):
                if (j - i) < 0:
                    break
                if self.Board[j - i][j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[j - i][j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[j - i][j] == " ":
                    pair.append(j - i)
                    pair.append(j)
                var = False
                va2 = False

        for i in range(1, 8):
            var = False
            va2 = False
            for j in range(7, -1, -1):
                if (j - i) < 0:
                    break
                if self.Board[j][j - i] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[j][j - i] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[j][j - i] == " ":
                    pair.append(j)
                    pair.append(j - i)
                var = False
                va2 = False

        for i in range(8):  # right top to left bottom - upper half
            var = False
            va2 = False
            for j in range(8):
                if (7 - j - i) < 0:
                    break
                if self.Board[j][7 - j - i] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[j][7 - j - i] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[j][7 - j - i] == " ":
                    pair.append(j)
                    pair.append(7 - j - i)
                var = False
                va2 = False

        for i in range(1, 8):  # right top to left bottom - bottom half
            var = False
            va2 = False
            for j in range(8):
                if (j + i) < 8:
                    break
                if self.Board[j + i][7 - j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[j + i][7 - j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[j + i][7 - j] == " ":
                    pair.append(j + i)
                    pair.append(7 - j)
                var = False
                va2 = False

        for i in range(8):  # left bottom to right top- upper half
            var = False
            va2 = False
            for j in range(8):
                if (7 - j - i) < 0:
                    break
                if self.Board[7 - j - i][j] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[7 - j - i][j] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[7 - j - i][j] == " ":
                    pair.append(7 - j - i)
                    pair.append(j)
                var = False
                va2 = False

        for i in range(1, 8):  # left bottom to right top - bottom half
            var = False
            va2 = False
            for j in range(8):
                if (j + i) < 8:
                    break
                if self.Board[7 - j][j + i] == turn:
                    var = True
                    var2 = False
                    continue
                if var and self.Board[7 - j][j + i] == opp:
                    va2 = True
                    continue
                if var and va2 and self.Board[7 - j][j + i] == " ":
                    pair.append(7 - j)
                    pair.append(j + i)
                var = False
                va2 = False

        return pair

    def TakeTurn(self, row, col, turn):
        valid = False
        moves = self.ValidMoves(turn)
        for i in range(0, len(moves), 2):
            if row == moves[i] and col == moves[i+1]:
                valid = True
        if not valid:
            return False

        self.Board[row][col] = turn

        for i in range(row + 1, 8):  # down
            if self.Board[i][col] == ' ':
                break
            if self.Board[i][col] == turn:
                for j in range(i - 1, row, -1):
                    self.Board[j][col] = turn
                break

        for i in range(row - 1, 0, -1):  # up
            if self.Board[i][col] == ' ':
                break
            if self.Board[i][col] == turn:
                for j in range(i + 1, row, 1):
                    self.Board[j][col] = turn
                break

        for i in range(col + 1, 8):  # right
            if self.Board[row][i] == ' ':
                break
            if self.Board[row][i] == turn:
                for j in range(i - 1, col, -1):
                    self.Board[row][j] = turn
                break

        for i in range(col - 1, 0, -1):  # left
            if self.Board[row][i] == ' ':
                break
            if self.Board[row][i] == turn:
                for j in range(i + 1, col, 1):
                    self.Board[row][j] = turn
                break

        for i in range(1, 8):  # diagonal
            if (row + i) > 7 or (col + i) > 7:
                break
            if self.Board[row + i][col + i] == ' ':
                break
            if self.Board[row + i][col + i] == turn:
                for j in range(i, 0, -1):
                    self.Board[row + j][col + j] = turn
                break

        for i in range(1, 8):  # r_diagonal
            if (row - i) < 0 or (col - i) < 0:
                break
            if self.Board[row - i][col - i] == ' ':
                break
            if self.Board[row - i][col - i] == turn:
                for j in range(i, 0, -1):
                    self.Board[row - j][col - j] = turn
                break

        for i in range(1, 8):  # bl to t_r
            if (row - i) < 0 or (col + i) > 7:
                break
            if self.Board[row - i][col + i] == ' ':
                break
            if self.Board[row - i][col + i] == turn:
                for j in range(i, 0, -1):
                    self.Board[row - j][col + j] = turn

        for i in range(1, 8):  # br to tl
            if (row + i) > 7 or (col - i) < 0:
                break
            if self.Board[row + i][col - i] == ' ':
                break
            if self.Board[row + i][col - i] == turn:
                for j in range(i, 0, -1):
                    self.Board[row + j][col - j] = turn

        return True

    def EvaluationFunction(self):
        count = self.counter()
        re = self.checkCompleted()
        if re == 1:
            return -9999  # if user is winning
        if re == 2:
            return 9999   # if user is losing
        return 10 * (count[1] - count[0])  # computer's score - user's score
