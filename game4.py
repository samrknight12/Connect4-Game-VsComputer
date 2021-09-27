import numpy as np
import random
#InsertO spaceIsFree printBoard makeBoard isWinner playerMove Completed (may adjust later)
# need isBoardFull and a main while loop before testing playerMove
PLAYER = 1
COMP = 2
ROWS = 6
COLS = 7

def insertO(board, num, pos1, pos2):
    board[pos1][pos2] = num

def spaceIsFree(board, col):
    return board[ROWS-1][col] == 0

def printBoard(board):
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[5][0]}   |   {board[5][1]}   |   {board[5][2]}   |   {board[5][3]}   |  {board[5][4]}   |  {board[5][5]}   |   {board[5][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[4][0]}   |   {board[4][1]}   |   {board[4][2]}   |   {board[4][3]}   |  {board[4][4]}   |  {board[4][5]}   |   {board[4][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[3][0]}   |   {board[3][1]}   |   {board[3][2]}   |   {board[3][3]}   |  {board[3][4]}   |  {board[3][5]}   |   {board[3][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |   {board[2][3]}   |  {board[2][4]}   |  {board[2][5]}   |   {board[2][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |   {board[1][3]}   |  {board[1][4]}   |  {board[1][5]}   |   {board[1][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |   {board[0][3]}   |  {board[0][4]}   |  {board[0][5]}   |   {board[0][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')

def makeBoard():
    board = np.zeros((6,7)) # Board has 42 spaces
    return board

def isWinner(bo, num):
    #bo is board, num is number 1 = Player, 2 = comp
    #Check Verticals
    for c in range(COLS):
        for r in range(ROWS-3):
            if (bo[r][c] == num and bo[r+1][c] == num and bo[r+2][c] == num and bo[r+3][c] == num):
                return True
    #check rows
    for c in range(COLS-3):
        for r in range(ROWS):
            if (bo[r][c] == num and bo[r][c+1] == num and bo[r][c+2] == num and bo[r][c+3] == num):
                return True
    #check diagonal bottom left to top right
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if (bo[r][c] == num and bo[r+1][c+1] == num and bo[r+2][c+2] == num and bo[r+3][c+3] == num):
                return True
    #check diagonal top left to bottom right
    for c in range(COLS-3):
        for r in range(3,ROWS):
            if (bo[r][c] == num and bo[r-1][c+1] == num and bo[r-2][c+2] == num and bo[r-3][c+3] == num):
                return True

def playerMove(board):
    run = True
    while run:
        moveCol = input("Select a Column Position for an \'X\' (1-6)")

        try:
            moveCol = int(moveCol) - 1
            if  moveCol >= 0 and moveCol <= 5:
                if spaceIsFree(board, moveCol):
                    moveRow = getOpenRow(board, moveCol)
                    insertO(board, PLAYER, moveRow, moveCol)
                    run = False
                else:
                    print("This space is already full")
            else:
                print("Type number between 1 and 7 for Row and 1-6 for Column")
        except:
            print("Please type a number")


def isBoardFull(board):
        if board.count(0) > 1:
            return False
        else:
            return True

def compMove():
    pass

def playablePlaces(board):
    playPlace = []
    for column in range(7): #7 columns
        if board[5][column] == 0:
            playPlace.append(column)
    return playPlace

def windowScore(window, num):
    score = 0
    opnum = PLAYER #opponents piece
    if num == PLAYER:
        opnum = COMP

    if window.count(num) == 4:
        score +=100
    elif window.count(num) == 3 and window.count(0) == 1:
        score +=5
    elif window.count(num) == 2 and window.count(0) == 2:
        score +=2

    if window.count(opnum) == 3 and window.count(0) == 1:
        score -=7

    return score

def scorePos(board, num):

    # check window sizes of 4

    score = 0
    #center score
    center_array = [int(i) for i in list(board[:,COLS//2])]
    center_count = center_array.count(num)
    score += center_count * 3

    # horizontal score
    for r in range(ROWS):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLS-3):
            window = row_array[c:c+4]  #plus 4 is the window length
            score += windowScore(window, num)

    # vertical score
    for c in range(COLS):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROWS-3):
            window = col_array[r:r+4]
            score += windowScore(window, num)

    # positive diagonal score
    for r in range(ROWS-3):
        for c in range(COLS-3):
            window = [board[r+i][c+i] for i in range(4)] #move up and across board
            score += windowScore(window, num)

    # negative diagonal score
    for r in range(ROWS-3):
        for c in range(COLS-3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += windowScore(window, num)

    return score

def bestMove(board, num):
    bestScore = 0
    goodLocation = playablePlaces(board)
    bestCol = random.choice(goodLocation)
    for column in goodLocation:
        row = getOpenRow(board, column)
        copyBoard = board.copy() #numpy array will point to the same memory if just copyBoard = board
        insertO(copyBoard, num, row, column)
        score = scorePos(copyBoard, num)
        if score > bestScore:
            bestScore = score
            bestCol = column

    return bestCol

def getOpenRow(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def main():
    gameover = False
    board = makeBoard()
    printBoard(board)
    turn = random.randint(PLAYER,COMP) #random who goes first

    while (gameover == False):
        if turn == PLAYER:
            if (isWinner(board, COMP) == True):
                gameover = True
                print("You Lose :( )")
                break
            else:
                playerMove(board)
                turn = COMP
                # printBoard(board)

        if turn == COMP:
            if (isWinner(board, PLAYER) == True):
                gameover = True
                print("You Win!")
                break
            else:
                col = bestMove(board, COMP)
                row = getOpenRow(board, col)
                insertO(board, COMP, row, col)
                turn = PLAYER
                printBoard(board)

main()
