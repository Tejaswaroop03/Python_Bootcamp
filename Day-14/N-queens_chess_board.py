def printBoard(board):
    print("-")
    for i in board:
        print(i)
def isSafe(board,row,col):
    i=row-1
    while i>=0:
        if board[i][col]=='Q':
            return False
        i-=1
    #left diagonal
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    #right diagonal
    i=row-1
    j=col+1
    while i>=0 and j<len(board):
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1
    return True
def nQueen(board,row):
    global c
    if row==len(board):
        c+=1
        printBoard(board)
        return
    for j in range(len(board)):
        if isSafe(board,row,j):
            board[row][j]='Q'
            nQueen(board,row+1)
            board[row][j]='.'
    
n=int(input())
c=0
board =[['.']*n for _ in range(n)]
nQueen(board,0)
print(c)