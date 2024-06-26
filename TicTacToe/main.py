import os


def printBoard(board):
    for index, row in enumerate(board):
        for _index, cell in enumerate(row):
            _cell = " " if _index == 0 else ""
            _cell += (
                str(index * 3 + _index) if cell == -1 else ("X" if cell == 1 else "O")
            )
            _end = " | " if _index != 2 else "\n"
            print(_cell, end=_end)
        if index != 2:
            print("-" * 11)
    print()


def getWinner(board):
    for i in range(len(board)):
        if board[i][0] != -1 and (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]

        if board[0][i] != -1 and (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]

    if board[0][0] != -1 and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != -1 and board[0][2] == board[1][1] == board[2][0]:
        return board[0][0]

    return -1


def isTie(board):
    for row in board:
        for cell in row:
            if cell == -1:
                return False

    return True


def clearScreen():
    os.system("clear")


def displayWelcomeMessage():
    print("Welcome to Tic-Tac-Toe!\n")


def moveIsValid(move, board):
    if move == -1 or not move.isnumeric():
        return False

    move = int(move)

    row = move // 3
    cell = move % 3

    return (0 <= move and move <= 8) and (board[row][cell] == -1)


def getMove(currPlayer, board):
    move = ""
    valid = False

    while not valid:
        move = input(f"Player {currPlayer} Move: ")
        valid = moveIsValid(move, board)

        if not valid:
            print("Move not valid!")

    return int(move)


def placePiece(currPlayer, move, board):
    row = move // 3
    cell = move % 3
    board[row][cell] = currPlayer


def main():
    quit = False

    while not quit:
        currPlayer = 0
        board = [[-1 for _ in range(3)] for _ in range(3)]

        tie = False
        winner = -1

        clearScreen()
        displayWelcomeMessage()

        printBoard(board)

        while not tie and winner == -1:
            move = getMove(currPlayer, board)
            placePiece(currPlayer, move, board)

            currPlayer = (currPlayer + 1) % 2

            clearScreen()
            displayWelcomeMessage()
            printBoard(board)

            tie = isTie(board)
            winner = getWinner(board)

        if tie:
            print("Tie Game!")
        else:
            print(f"Player {winner} Wins!")

        playAgain = input("\nPlay again? (y / n):")

        if not playAgain == "y":
            quit = True


if __name__ == "__main__":
    main()
