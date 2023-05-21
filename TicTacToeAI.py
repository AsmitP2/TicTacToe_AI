import random
board = {1: " ", 2: " ", 3: " ", 
         4: " ", 5: " ", 6: " ", 
         7: " ", 8: " ", 9: " "}

def printBoard(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[7]+"|"+board[8]+"|"+board[9])

def checkWin(board, player):
    if board[1] == board[2] and board[1]==board[3] and board[1]==player:
        return True
    elif board[1] == board[5] and board[1]==board[9] and board[1]==player:
        return True
    elif board[1] == board[4] and board[1]==board[7] and board[1]==player:
        return True
    elif board[2] == board[5] and board[2]==board[8] and board[2]==player:
        return True
    elif board[3] == board[6] and board[3]==board[9] and board[3]==player:
        return True
    elif board[4] == board[6] and board[4]==board[5] and board[4]==player:
        return True
    elif board[3] == board[5] and board[3]==board[7] and board[3]==player:
        return True
    elif board[7] == board[8] and board[7]==board[9] and board[7]==player:
        return True
    else:
        return False
def checkDraw(board):
    for i in board:
        if board[i] == " ":
            return False
    return True

def minimax(board, player):
    if checkWin(board, "X"):
        return 1
    elif checkWin(board, "O"):
        return -1
    elif checkDraw(board):
        return 0
    if player == "computer":
        bestScore = -10
        for i in board.keys():
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, "user")
                board[i] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 3
        for i in board.keys():
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, "computer")
                board[i] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore

def getBestPos(board):
    bestScore = -10
    bestPosition = 0
    for i in board.keys():
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, "user")
            board[i] = " "
            if score > bestScore:
                bestScore = score
                bestPosition = i
    return bestPosition


printBoard(board)
players = ("X", "O")
turn = random.choice(players)
if turn == "X":
    position = random.randint(1, 9)
    board[position]=turn
    printBoard(board)
    turn = "O"
if turn == "O":
    position = int(input(f"Enter position for {turn} (1-9): "))
    board[position]=turn
    printBoard(board)
    turn = "X"
    move = random.randint(1, 9)
    while move == position:
        move = random.randint(1, 9)
    board[move]=turn
    printBoard(board)
    turn = "O"


while True:
    if turn == "X":
        position = getBestPos(board)
    else:
        position = int(input(f"Enter position for {turn} (1-9): "))
    if board[position] == " ":
        board[position]=turn
    else:
        print("Invalid position")
        continue
    printBoard(board)
    if(checkWin(board, turn)):
        print(turn + " has won the game")
        break
    if(checkDraw(board)):
        print("The game is a draw")
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"