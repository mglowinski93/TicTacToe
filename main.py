import random

def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def load_game_letter():
    letter = ''
    while not (letter=='X' or letter=='O'):
        print("Choose your letter. O or X")
        letter = input().upper()
    if letter == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def who_starts():
    if random.randint(0,1) ==0:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, move):
    board[move] = letter

def check_if_won(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))

def make_board_copy(board):
    return board[:]

def check_if_field_is_untaken(board, move):
    return board[move] == ' '

def load_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_if_field_is_untaken(board, int(move)):
        move = input()
    return int(move)

def get_a_move_from_list(board, move_list):
    possible_moves = []
    for i in move_list:
        if check_if_field_is_untaken(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def define_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    #Check if there is possibility to finish a game
    for i in range(1, 10):
        board_copy = make_board_copy(board)
        if check_if_field_is_untaken(board, i):
            make_move(board_copy, computer_letter, i)
            if check_if_won(board_copy, computer_letter):
                return i

    #Block player
    for i in range(1, 10):
        board_copy = make_board_copy(board)
        if check_if_field_is_untaken(board, i):
            make_move(board_copy, player_letter, i)
            if check_if_won(board_copy, player_letter):
                return i

    #Try to take corner
    move = get_a_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    #Take central place
    if check_if_field_is_untaken(board, 5):
        return 5

    #Make a move that is possible
    return get_a_move_from_list(move, [2, 4, 6, 8])

def check_if_board_full(board):
    for i in range(1, 10):
        if check_if_field_is_untaken(board, i):
            return False
    return True

print("Welcome in Tic Tac Toe Game!")

while True:
    main_board = [' '] * 10
    player_letter, computer_letter = load_game_letter()
    print("Your letter is: {}. Computer will be playing with letter: {}".format(player_letter, computer_letter))
    round = who_starts()
    print("{} is starting game".format(round))
    game_over = False

    while not game_over:
        if round == 'player':
            draw_board(main_board)
            move = load_player_move(main_board)
            make_move(main_board, player_letter, move)

            if check_if_won(main_board, player_letter):
                draw_board(main_board)
                print('YOU WON!')
                game_over = True
            else:
                if check_if_board_full(main_board):
                    draw_board(main_board)
                    print("GAME OVER - DRAW")
                    break
                else:
                    round = 'computer'
        else:
            move = define_computer_move(main_board, computer_letter)
            make_move(main_board, computer_letter, move)
            if check_if_won(main_board, computer_letter):
                draw_board(main_board)
                print("Computer won!")
                game_over = True
            else:
                if check_if_board_full(main_board):
                    draw_board(main_board)
                    print("GAME OVER - DRAW")
                    break
                else:
                    round = 'player'

    print("Play one more time? (yes/no)")
    if not input().lower().startswith('y'):
        break