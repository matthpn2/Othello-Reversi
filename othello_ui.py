'''

Othello User Interface

---

A module that implements the console-mode user interface.

---

This program asks the user to specify the following options, in the order specified. When the user enters erroneous
input, the program informs the user that the input was invalid and asks the user for the input again.

    1. The number of rows on the board, which must be an even integer between 4 and 16.
    2. The number of columns on the board, which must be an even integer between 4 and 16.
    3. Which of the two players will move first, B [Black] or W [White].
    4. Which of the two colors will be in the top-left position of the four centered discs, two white and two black.

The game is then played by asking the two users to enter their moves directly into the console, continuing until the 
game is complete and at which point the program ends. Until the game is over, the following sequence of events is repeated.

    1. Display the board, the score (how many disks of each color are on the board) and whose turn it is to move.
    2. User is asked to make a move by specifying a cell on the board in which he would like to place a disk.
    3. If the move is invalid, inform the user and ask for another move. Otherwise, if valid, complete the move and change turns.
    4. All the corresponding disks are placed and flipped.
    5. If the game is not over, repeat back to step 1. Otherwise, if the game is over, display the board, the score, and the 
       winner of the game (or no winner at all).
    6. The game ends and the program closes.

'''

import othello_game_logic as ogl

def board_rows():
    '''
        User enters number of rows for the board, an even integer between 4 and 16.
    '''
    try:
        rows = int(input('Enter the number of rows [4-16]: '))
        assert rows > 3 and rows < 17 and rows%2 == 0
        return rows
    except:
        print('Invalid number of rows entered. Please try again.\n')
        return board_rows()

def board_columns():
    '''
        User enters number of columns for the board, an even integer between 4 and 16.
    '''
    try:
        columns = int(input('Enter the number of columns [4-16]: '))
        assert columns > 3 and columns < 17 and columns%2 == 0
        return columns
    except:
        print('Invalid number of columns entered. Please try again.\n')
        return board_columns()
        
def board_position():
    '''
        User selects which color will be placed in top-left position of the four centered disks.
    '''
    try:
        disk_color = str(input('Enter color to be placed in top-left position [W/B]: '))
        assert disk_color == 'W' or disk_color == 'B'
        return disk_color
    except:
        print('Invalid input of color. Please try again.\n')
        return board_position()

def board_turn():
    '''
        User selects which of the players will move first, black or white.
    '''
    try:
        turn = str(input('Enter which player will move first [W/B]: '))
        assert turn == 'W' or turn == 'B'
        return turn
    except:
        print('Invalid input of color. Please try again.\n')
        return board_turn()

def input_row(board_row):
    '''
        User inputs row for space to place a disk in.
    '''
    try:
        row = int(input('Enter row for space you want to place a disk in [1-{}]: '.format(board_row)))
        return row
    except:
        return input_row(board_row)

def input_column(board_column):
    '''
        User inputs column for space to place a disk in.
    '''
    try:
        column = int(input('Enter column for space you want to place a disk in [1-{}]: '.format(board_column)))
        return column
    except:
        return input_column(board_column)

if __name__ == '__main__':
    default_row = board_rows()
    default_column = board_columns()
    color_position = board_position()
    first_turn = board_turn()
    print()

    board = ogl.OthelloBoard(default_row, default_column, color_position, first_turn)
    board.default_board()

    game_over = False
    while game_over == False:
        board.print_board()
        print()

        board.print_score()
        board.print_turn()
        print()

        row = input_row(default_row) - 1
        column = input_column(default_column) - 1
        board.disk_color(row, column)
        print()

        if board.valid_move() == False:
            print('Invalid user move. Please try again.')
            continue
        
        board.make_move()
        board.change_turn()
        board.reset_moves()

        game_over = board.game_over()
        if game_over == True:
            board.print_score()
            board.print_board()
            print()

            board.print_winner()
            break