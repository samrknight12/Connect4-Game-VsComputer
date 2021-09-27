import numpy as np
#InsertO spaceIsFree printBoard makeBoard isWinner playerMove Completed (may adjust later)
# need isBoardFull and a main while loop before testing playerMove


def insertO(letter, pos1, pos2):
    board[pos1][pos2] = letter

def spaceIsFree(pos1, pos2):
    return board[pos1][pos2] == '0'

def printBoard(board):
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |   {board[0][3]}   |  {board[0][4]}   |  {board[0][5]}   |   {board[0][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[1][0]}   |   {board[1][1]}   |   {board[2][2]}   |   {board[2][3]}   |  {board[3][4]}   |  {board[3][5]}   |   {board[4][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |   {board[2][3]}   |  {board[2][4]}   |  {board[2][5]}   |   {board[2][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[3][0]}   |   {board[3][1]}   |   {board[3][2]}   |   {board[3][3]}   |  {board[3][4]}   |  {board[3][5]}   |   {board[3][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[4][0]}   |   {board[4][1]}   |   {board[4][2]}   |   {board[4][3]}   |  {board[4][4]}   |  {board[4][5]}   |   {board[4][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')
    print('|        |         |         |         |        |        |         |')
    print(f'|  {board[5][0]}   |   {board[5][1]}   |   {board[5][2]}   |   {board[5][3]}   |  {board[5][4]}   |  {board[5][5]}   |   {board[5][6]}   |')
    print('|        |         |         |         |        |        |         |')
    print('--------------------------------------------------------------------')

def makeBoard():
    board = np.zeros((6,7)) # Board has 42 spaces
    return board

def isWinner(bo, le):
    #bo is board, le is letter
    row = 6 # rows
    cols = 7 # columns
    #Check Verticals
    for c in range(cols):
        for r in range(rows-3):
            return (bo[r][c] == le and bo[r+1][c] == le and bo[r+2][c] and bo[r+3][c])

    #check rows
    for c in range(cols-3):
        for r in range(rows):
            return (bo[r][c] == le and bo[r][c+1] == le and bo[r][c+2] and bo[r][c+3])

    #check diagonal bottom left to top right
    for c in range(cols-3):
        for r in range(rows-3):
            return (bo[r][c] == le and bo[r+1][c+1] == le and bo[r+2][c+2] and bo[r+3][c+3])

    #check diagonal top left to bottom right
    for c in range(cols-3):
        for r in range(3,rows):
            return (bo[r][c] == le and bo[r-1][c+1] == le and bo[r-2][c+2] and bo[r-3][c+3])

def playerMove():
    run = True
    while run:
        moveRow = input("Select a Row Position for an \'X\' (1-7)")
        moveCol = input("Select a Column Position for an \'X\' (1-6)")
        try:
            moveRow = int(moveRow) - 1
            moveCol = int(moveCol) - 1
            if moveRow >= 0 and moveRow <= 6 and moveCol >= 0 and moveCol <= 5:
                if spaceIsFree(moveRow, moveCol):
                    run = False
                    insertLetter('X', moveRow, moveCol)
                else:
                    print("This space is already full")
            else:
                print("Type number between 1 and 7 for Row and 1-6 for Column")
        except:
            print("Please type a number")

def main():
    board = makeBoard()
    printBoard(board)
    playerMove()
    printBoard(board)

main()
