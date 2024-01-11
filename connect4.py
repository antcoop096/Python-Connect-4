#without index looses info
from os import system

def make_empty_board(nrows, ncols): #makes new board
    return ["." * ncols] * nrows

def print_board(board): #prints the board
    for n in range(len(board[0])): print(f' {n + 1}  ', end = '')
    print()
    for row in range(len(board)):
        row_copy = list(board[row])
        for column in range(len(row_copy)):
            if row_copy[column] == '.': row_copy[column] = ' '
            row_copy[column] = f' {row_copy[column]} '
        print('|'.join(row_copy))
        if row < (len(board) - 1): print(f'{"---+" * (len(row_copy) - 1)}---')

def verify_move(board, column): #validates move
    return (1 <= column <= len(board[0])) and ('.' in [board[row][column - 1] for row in range(len(board))])

def update_board(board, column, disc): #puts disk in board
    col_lis = [board[row][column] for row in range(len(board))]
    for row in range(len(col_lis) - 1, -1, -1):
        if col_lis[row] == '.': 
            board[row] = list(board[row])
            board[row][column] = disc
            board[row] = ''.join(board[row])
            return board
        
def has_won(board, column): #checks if someone has won
    col_lis, row = [board[row][column] for row in range(len(board))], 0
    while col_lis[row] == '.': row += 1
    if board[row][column] * 4 in ''.join(col_lis): return True #checks vertically
    if board[row][column] * 4 in board[row]: return True #checks horizontally
    
    ullr, llur = [], []  
    for i in range(1,4): #diagonally \
        if row - i < 0 or column - i < 0: break   
        ullr.insert(0, board[row - i][column - i])
    ullr.append(board[row][column])
    for i in range(1,4): 
        if row + i >= len(board) or column + i >= len(board[0]): break
        ullr.append(board[row + i][column + i])
    if board[row][column] * 4 in ''.join(ullr): return True
    
    for i in range(1,4): #diagonally /
        if row + i >= len(board) or column - i < 0: break   
        llur.insert(0, board[row + i][column - i])
    llur.append(board[row][column])
    for i in range(1,4): 
        if row - i < 0 or column + i >= len(board[0]): break
        llur.append(board[row - i][column + i])
    if board[row][column] * 4 in ''.join(llur): return True
    
    return False

def rc_input(s): #takes in user input for amount of rows and columns
    while True:
        n = input(f'Enter number of {s} (4-10): ')
        if n.isdecimal() and (4 <= int(n) <= 10): return int(n)
        print(f'You must enter a number between 4 and 10, try again.\n')

######################################################################################

print(f'\n{"*"*12}\nCONNECT FOUR\n{"*"*12}\n')
r, c = rc_input('rows'), rc_input('columns')
board, win, tie = make_empty_board(r,c), False, False

def turn(disk):
    global board, win, tie, c
    if '.' not in board[0]: 
        print('\nTie game!')
        tie = True
   
    while not tie:
        column = input(f"\n{disk}'s turn\nEnter column (1-{c}): ")
        print()
        if column.isdecimal() and verify_move(board, int(column)):
            system('cls')
            column = int(column) - 1
            board = update_board(board, column, disk)
            print_board(board)
            win = has_won(board, column)
            if win: print(f'\n{disk} wins!')
            break
        system('cls')
        print_board(board)
        print("\nCannot do that move, try again.")

system('cls')
print_board(board)

while not win and not tie:
    turn('X')
    if win or tie: break
    turn('O')


