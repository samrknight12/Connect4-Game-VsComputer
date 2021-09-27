import numpy as np
import random
# This game is a basic python console connect 4 against a computer that has a simple weighted decision function to try to beat you. It
# Prioritizes: 1) connect 4 to win 2) stop you from connecting 4 3) connecting 3 4) connecting 2.
# I hope to learn about pygame to make the play more user friendly.

#Global static variables
PLAYER = 1
COMP = 2
ROWS = 6
COLS = 7

# Inserts choice by user or computer to the board, num = PLAYER or COMP
def insertO(board, num, pos1, pos2):
    board[pos1][pos2] = num

#Returns true or false if a spcae in the numpy array is 0
def spaceIsFree(board, col):
    return board[ROWS-1][col] == 0

#Creates the game board as a 6x7 numpy array of zeros
def makeBoard():
    board = np.zeros((6,7)) # Board has 42 spaces
    return board

#Prints The board to the console (Gross to look at, currently learning how to change to something less gross)
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

# Checks horizontal, vertical, positive slope, and negative slope for a win (4 computer or player pieces in a row )
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

#How the player interacts with the game
def playerMove(board):
    run = True
    while run:
        moveCol = input("Select a Column Position for an (1-7): ")

        try:
            # try to convert input to int so we know its a number
            moveCol = int(moveCol) - 1
            # Check if the number is valid
            if  moveCol >= 0 and moveCol <= 6:
                # Check if the column still has room
                if spaceIsFree(board, moveCol):
                    # Get the row that is lowest on the board in that column
                    moveRow = getOpenRow(board, moveCol)
                    #insert the players number into that spot
                    insertO(board, PLAYER, moveRow, moveCol)
                    #exit input loop
                    run = False
                else:
                    print("This space is already full")
            else:
                print("Type number between 1 and 7 for Row and 1-6 for Column")
        except:
            print("Please type a number")

# Find the columns on the board that can be played in
def playablePlaces(board):
    playPlace = []
    for column in range(7): #7 columns
        if board[5][column] == 0:
            playPlace.append(column)
    return playPlace

#Weighted score for computer to make best choice
def windowScore(window, num):
    score = 0
    opnum = PLAYER #opponents piece
    if num == PLAYER:
        opnum = COMP

    # if 4 in a row is possible then do it -> high weight 100
    if window.count(num) == 4:
        score +=100

    # if computer can get 3 in a row -> mid weight 5
    elif window.count(num) == 3 and window.count(0) == 1:
        score +=5

    # if computer can get 2 in a row -> low weight 2
    elif window.count(num) == 2 and window.count(0) == 2:
        score +=2

    # if player has 3 in a row computer will lose points for not blocking the players win
    if window.count(opnum) == 3 and window.count(0) == 1:
        score -=7

    return score

def scorePos(board, num):

    # check window sizes of 4

    score = 0

    #center score so computer takes center more often
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

# Base function for computers location choice
def bestMove(board, num):
    bestScore = -1000
    # find all playable columns
    goodLocation = playablePlaces(board)
    #randomly choose one for initalization of bestCol
    bestCol = random.choice(goodLocation)
    # for each playable column
    for column in goodLocation:
        # find the lowest open row
        row = getOpenRow(board, column)
        #numpy array will point to the same memory if just copyBoard = board, use the copy to test all scenarios
        copyBoard = board.copy()
        # insert computer choice
        insertO(copyBoard, num, row, column)
        # find the score of that choice
        score = scorePos(copyBoard, num)
        # Compare score to previous choices score, if better update to have the current best choice
        if score > bestScore:
            bestScore = score
            bestCol = column

    return bestCol

# finds the lowest open row for a column
def getOpenRow(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def main():
    # initalized game stop variable
    gameover = False
    #make and print board to screen
    board = makeBoard()
    printBoard(board)
    #random who goes first
    turn = random.randint(PLAYER,COMP) #random who goes first

    #while the game is running
    while (gameover == False):
        # for the players turn
        if turn == PLAYER:
            #check to see if the player has lost
            if (isWinner(board, COMP) == True):
                # if they lost game over varible changed to end loop
                gameover = True
                print("You Lose :( )")
                break
            else:
                # if they didnt lose, go to player move function for input and place their move
                playerMove(board)
                # Computers turn now
                turn = COMP

        # for computers turn
        if turn == COMP:
            # Check if user has won
            if (isWinner(board, PLAYER) == True):
                gameover = True
                print("You Win!")
                break
            else:
                # get computer column choice
                col = bestMove(board, COMP)
                # get computer row choice
                row = getOpenRow(board, col)
                # insert to board
                insertO(board, COMP, row, col)
                # change turns
                turn = PLAYER
                #show user the board
                printBoard(board)

main()
