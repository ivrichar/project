from board import Board
from player import PlayerMM, PlayerAB, PlayerMC, PlayerNM, ManualPlayer

class Game:


    def __init__(self, startBoard, player1, player2):
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2

    def simulateLocalGame(self):

        board = Board(orig=self.startBoard)
        isPlayer1 = True

        while(True):

            if isPlayer1:
                move = self.player1.findMove(board)
            else:
                move = self.player2.findMove(board)

            board.makeMove(move)
            board.print()

            isOver = board.isTerminal()
            if isOver == 0:
                print("Draw!")
                break
            elif isOver == 1:
                print("Player 1 wins!")
                break
            elif isOver == 2:
                print("Player 2 wins!")
                break
            else:
                isPlayer1 = not isPlayer1



if __name__ == "__main__":
    alg = input("Welcome to Connect 4! To start, Choose an algorithm! Type A for AlphaBeta, M for Minimax, C for Monte Carlo, N for Negamax, or T for Two Player!")
    if (alg == "A"):
        print("AlphaBeta selected!")
        level = input("Select difficulty (1 - 5): ")
        game = Game(Board(), ManualPlayer(5, True), PlayerAB(level, False))
    if (alg == "M"):
        print("Minimax selected!")
        level = input("Select difficulty (1 - 5): ")
        game = Game(Board(), ManualPlayer(5, True), PlayerMM(level, False))
    if (alg == "C"):
        print("Monte Carlo selected!")
        level = input("Select difficulty (1 - 5): ")
        game = Game(Board(), ManualPlayer(5, True), PlayerMC(level, False))
    if (alg == "N"):
        print("Negamax selected!")
        level = input("Select difficulty (1 - 5): ")
        game = Game(Board(), ManualPlayer(5, True), PlayerNM(level, False))
    if (alg == "T"):
        game = Game(Board(), ManualPlayer(5, True), ManualPlayer(5, False))
    else:
        print("Invalid input")
    game.simulateLocalGame()