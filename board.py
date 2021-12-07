class Board(object):

    HEIGHT = 6
    WIDTH = 7

    def __init__(self, orig=None, hash=None):

        if(orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return

        else:
            #board starts as an array of empty lists
            self.board = [[] for x in range(self.WIDTH)]
            self.numMoves = 0
            self.lastMove = None
            return


    def makeMove(self, column):
        piece = self.numMoves % 2
        self.lastMove = (piece, column)
        self.numMoves += 1
        self.board[column].append(piece)


    #input: column (as an integer)
    # output: boolean value
    def isValidMove(self, column):
        return len(self.board[column]) < 6

    # return all non-full columns (columns whose length is < 6)
    def getAllValidMoves(self):
        results = []
        for i in range(7):
            if len(self.board[i]) < 6:
                results.append(i)
        return results        


    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = Board(self)
                child.makeMove(i)
                children.append((i, child))
        return children


    def isTerminal(self):
        for i in range(0,self.WIDTH):
            for j in range(0,self.HEIGHT):
                try:
                    if self.board[i][j]  == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if self.board[i][j]  == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j + 3 > self.HEIGHT and self.board[i][j] == self.board[i+1][j + 1] == self.board[i+2][j + 2] == self.board[i+3][j + 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j - 3 < 0 and self.board[i][j] == self.board[i+1][j - 1] == self.board[i+2][j - 2] == self.board[i+3][j - 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass
        if self.isFull():
            return 0
        return -1


    def isFull(self):
        return self.numMoves == 42

    def print(self):
        print("")
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)
        print(self.lastMove[1])
        print(self.numMoves)
