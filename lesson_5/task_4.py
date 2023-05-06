# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.

def print_board(board):
    for row in board:
        print(row)

def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if '' in row:
            return False
    return True

def play_game(board, player):
    winner = get_winner(board)
    if winner is not None:
        print(f'{winner} wins!')
        return
    elif is_full(board):
        print('Draw!')
        return
    else:
        row = int(input(f'Player {player}, enter row (0-2): '))
        col = int(input(f'Player {player}, enter col (0-2): '))
        if board[row][col] == '':
            board[row][col] = player
            player = 'O' if player == 'X' else 'X'
        else:
            print('This position is already occupied. Try again.')
        print_board(board)
        play_game(board, player)

board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'
print_board(board)
play_game(board, player)
