import math

from board import Board

class Player:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit


    def heuristic(self, board):
        return 0


class PlayerMM(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        score, move = 0, 0
        print(self.isPlayerOne, "move made", move)
        return move

    def miniMax(self, board, depth, player):
        return 0, 0



class PlayerAB(Player):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        score, move = 0, 0
        print(self.isPlayerOne, "move made", move)
        return move

    def alphaBeta(self, board, depth, player, alpha, beta):
        return 0, 0

class PlayerMC(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        score, move = 0, 0
        print(self.isPlayerOne, "move made", move)
        return move

    def monteCarlo():
        return 0,0

class PlayerNM(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        score, move = 0, 0
        print(self.isPlayerOne, "move made", move)
        return move
    
    def negaMax(Player):
        return 0, 0



class ManualPlayer(Player):
    def findMove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " " + (str(c + 1) if len(board.board[c]) < 6 else ' ') + "  "
        print(opts)

        col = input("Select a column to place an" + (' O' if self.isPlayerOne else ' X') + ": ")
        col = int(col) - 1
        return col


