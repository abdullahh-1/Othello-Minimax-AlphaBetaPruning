class Othello:
    Board = [[], [], [], [], [], [], [], []]
    Turn = ""

    def __init__(self):
        self.Board = [[" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", "O", " ", " ", " ", " ", " "],
                      [" ", " ", " ", "X", "O", " ", " ", " "],
                      [" ", " ", " ", "O", "X", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "]]

    def Print(self):
        for i in range(len(self.Board)):
            print(self.Board[i])

    def counter(self):
        c = [0, 0] # index 0 for User, index 1 for AI
        for i in range(len(self.Board)):
            for j in range(len(self.Board[i])):
                if self.Board[i][j] != 'X':
                    c[0] += 1
                elif self.Board[i][j] != 'O':
                    c[1] += 1
        return c

    def checkCompleted(self):
        for i in range(len(self.Board)):
            for j in range(len(self.Board[i])):
                if self.Board[i][j] != ' ':
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

    def isValid(self, i, j):
        if i < 0 or i >= len(self.Board) or j >= len(self.Board) or j < 0:
            return False
        return True

    def Move(self):
        row = []
        col = []

        # check Vertically
        for j in range(len(self.Board[0])):
            var = False
            va2 = False
            for i in range(len(self.Board)):
                if self.Board[i][j] == "O":
                    var = True
                    continue
                if var and self.Board[i][j] == "X":
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    row.append(i)
                    col.append(j)
                var = False
                va2 = False

        # check Vertically Reversed
        for j in range(len(self.Board[0]) - 1, 0, -1):
            var = False
            va2 = False
            for i in range(len(self.Board) - 1, 0, -1):
                if self.Board[i][j] == "O":
                    var = True
                    continue
                if var and self.Board[i][j] == "X":
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    row.append(i)
                    col.append(j)
                var = False
                va2 = False

        # check Horizontally
        for i in range(len(self.Board)):
            var = False
            va2 = False
            for j in range(len(self.Board[0])):
                if self.Board[i][j] == "O":
                    var = True
                    continue
                if var and self.Board[i][j] == "X":
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    row.append(i)
                    col.append(j)
                var = False
                va2 = False

        # check Horizontally Reversed
        for i in range(len(self.Board) - 1, 0, -1):
            var = False
            va2 = False
            for j in range(len(self.Board[0]) - 1, 0, -1):
                if self.Board[i][j] == "O":
                    var = True
                    continue
                if var and self.Board[i][j] == "X":
                    va2 = True
                    continue
                if var and va2 and self.Board[i][j] == " ":
                    row.append(i)
                    col.append(j)
                var = False
                va2 = False

        # Diagonals
        for i in range(8):
            var = False
            va2 = False
            for j in range(8):
                if j + i >= 7:
                    break
                if self.Board[j][j + i] == "O":
                    var = True
                    continue
                if var and self.Board[j][j + i] == "X":
                    va2 = True
                    continue
                if var and va2 and self.Board[j][j + i] == " ":
                    row.append(j)
                    col.append(j + i)
                var = False
                va2 = False

        print(row, col)

    def EvaluationFunction(self):
        count = self.counter()
        return count[1] - count[0]  # return computer's score - user's score

