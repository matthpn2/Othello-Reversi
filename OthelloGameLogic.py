'''

Othello Game Logic

---

A module that implements Othello game logic with a class whose objects represent the current state of the game and methods
that manipulate that state..

---

Othello is a two-player strategy game played on a square board with four disks placed in a square in the center of the grid.

The players take turns placing disks on the board with their assigned color, black or white. During a play, if any of the disks
of the opponent's color that are in a straight line & bounded by the disk just place and another disk of the current player's color,
they are all turned over to the current player's color.

A valid play exists if in that position there exists at least one straight (horizontal, vertical or diagonal) occupied line between
the placed piece and another piece of the current player's color, with one or more opposing player's pieces between them. If the play
is valid, the opposing player's pieces lying in a straight line between the new placed piece and the anchoring piece are flipped. If
one player cannot make a valid move, the play passes back to the other player. 

The game concludes when every square on the grid contains a disk, or when neither player is able to make a legal move. The winning 
player is generally the one who has the most discs on the board at the end of the game.

'''

class InvalidOthelloMove(Exception):
    '''
        Raised whenever an invalid move is made.
    '''
    pass

class OthelloGameOver(Exception):
    '''
        Raised whenever an attempt to make a move after the game is already over.
    '''
    pass

class OthelloBoard:
    def __init__(self, rows, columns, color, turn):
        self._row = rows
        self._column = columns

        self._input_row = 0
        self._input_column = 0
        self._input_disc = ''

        self._board = []
        self._flipped_discs = []

        self._position_color = color
        self._current_turn = turn
        self._opposing_turn = ''

        self._black_score = 0
        self._white_score = 0
        self._winner = ''

    def default_board(self):
        '''
            Initializes an Othello game board with four discs on the board, two white and two black that are
            separated diagonally & arranged on the four center spaces of the grid. By default, the board has
            size rows x columns and is comprised of empty strings for easy readability.
        '''
        for row in range(self._row):
            self._board.append([' '] * self._column)
        
        if self._position_color == 'W':
            self._board[int((self._row/2) - 1)][int((self._column/2) - 1)] = 'W'
            self._board[int(self._row/2)][int(self._column/2)] = 'W'
            self._board[int((self._row/2) - 1)][int(self._column/2)] = 'B'
            self._board[int(self._row/2)][int((self._column/2) - 1)] = 'B'

        elif self._position_color == 'B':
            self._board[int((self._row/2) - 1)][int((self._column/2) - 1)] = 'B'
            self._board[int(self._row/2)][int(self._column/2)] = 'B'
            self._board[int((self._row/2) - 1)][int(self._column/2)] = 'W'
            self._board[int(self._row/2)][int((self._column/2) - 1)] = 'W'

    def print_score(self):
        '''
            Checks all the spaces on the game board and prints the count of each color disk, black and white.
        '''
        self._black_score = 0
        self._white_score = 0

        for row in self._board:
            for column in row:
                if column == 'B':
                    self._black_score += 1
                elif column == 'W':
                    self._white_score += 1
        
        print('B: ' + str(self._black_score) + ' | ' + 'W: ' + str(self._white_score))

    def print_board(self):
        '''
            Processes the board, row by row, and prints out each value; if empty, periods are printed instead.
        '''
        print('  ', end = '')
        for row in range(self._row):
            print(str(row + 1), end = ' ')
        print()

        column_num = 1
        for row in self._board:
            print(str(column_num), end = ' ')
            column_num += 1

            for column in row:
                if column == ' ':
                    print('.', end = " ")
                else:
                    print(column, end = " ")

            print()
    
    def print_turn(self):
        '''
            Print out the current player's turn.
        '''
        print(self._current_turn + " player's turn.")
    
    def disk_color(self, row, column):
        '''
            Sets opposing player's color and determines whether a disk is in some space on the board; if so, 
            determine its color.
        '''
        self._input_row = row
        self._input_column = column
        self._input_disc = self._board[row][column]

        if self._current_turn == 'B':
            self._opposing_turn = 'W'
        
        elif self._current_turn == 'W':
            self._opposing_turn = 'B'

    def valid_move(self):
        '''
            Returns False if move is invalid; otherwise, if move is valid, returns a list of spaces that 
            would be flipped to the current player's color.
        '''
        if self._input_disc != ' ' or not _valid_row_number(self._input_row, self._row) or not _valid_column_number(self._input_column, self._column):
            return False

        for x_row, y_column in ( [1,1], [1,-1], [-1,-1], [-1,1], [0,1], [0,-1], [1,0], [-1,0] ):
            x, y = self._input_row, self._input_column
            x += x_row
            y += y_column

            if _valid_row_number(x, self._row) and _valid_column_number(y, self._column) and self._board[x][y] == self._opposing_turn:
                x += x_row
                y += y_column

                if not _valid_row_number(x, self._row) or not _valid_column_number(y, self._row):
                    continue

                while self._board[x][y] == self._opposing_turn:
                    x += x_row
                    y += y_column

                    if not _valid_row_number(x, self._row) or not _valid_column_number(y, self._column):
                        break
                    
                if not _valid_row_number(x, self._row) or not _valid_column_number(y, self._column):
                    continue
                
                if self._board[x][y] == self._current_turn:
                    while True:
                        x -= x_row
                        y -= y_column

                        if (x, y) == (self._input_row, self._input_column):
                            break
                        
                        self._flipped_discs.append([x, y])
        
        if len(self._flipped_discs) == 0:
            return False

    def require_valid_move(self):
        '''
            Raises InvalidOthelloMove Error if its parameters does not result in a valid move.
        '''
        if self.valid_move() == False:
            raise InvalidOthelloMove('Your move is not a valid move.')

    def make_move(self):
        '''
            Make a move by placing a disk of the current player's color at the input row & column space and flips
            the opposing player's valid disks.
        '''
        self.require_valid_move()

        for row, column in self._flipped_discs:
            self._board[row][column] = self._current_turn
        self._board[self._input_row][self._input_column] = self._current_turn
    
    def change_turn(self):
        '''
            Given the current player's turn, change to the opposing player's turn.
        '''
        if self._current_turn == 'B':
            self._current_turn = 'W'
        else:
            self._current_turn = 'B'

    def reset_moves(self):
        '''
            Resets list of possible disks that can be flipped by a certain move.
        '''
        self._flipped_discs = []
    
    def game_over(self):
        '''
            Checks all the spaces on the baord for any more valid moves. If there are no more valid moves available,
            return True and game is over. Otherwise, if there are more valid moves available, return False and game
            continues. If one player cannot make a move, the play passes back to the other player. When neither player
            can move, the game truly ends.
        '''
        flipped_discs = []

        for row in range(self._row):
            for column in range(self._column): 
                self.disk_color(row, column)
                if self.valid_move() != False:
                    flipped_discs.append([row, column])
        
        if len(flipped_discs) == 0:
            self.change_turn()

            for row in range(self._row):
                for column in range(self._column): 
                    self.disk_color(row, column)
                    if self.valid_move() != False:
                        flipped_discs.append([row, column])

            return len(flipped_discs) == 0
    
        return False
    
    def require_game_not_over(self):
        '''
            Raises OthelloGameOver Error if user attempts to make a move after the game is over.
        '''
        if self.game_over() == True:
            raise OthelloGameOver('Game is over. There are no more valid moves.')

    def get_winner(self):
        '''
            The player with the most disks on the board at the end of the game is the winner.
        '''
        if self._black_score > self._white_score:
            self._winner = 'B'
        elif self._black_score < self._white_score:
            self._winner = 'W'
        else:
            self._winner = 'NONE'

    def print_winner(self):
        '''
            Print out the winner of the game.
        '''
        self.get_winner()
        if self._winner == 'None':
            print('The game has ended in a tie.')
        else:
            print('Congratulations, ' + self._winner + ' is the game winner!')

def _valid_row_number(inputRow, row):
    '''
        Returns True if the given input row number is valid, false otherwise.
    '''
    return 0 <= inputRow < row

def _valid_column_number(inputColumn, column):
    '''
        Returns True if the given input column number is valid, false otherwise.
    '''
    return 0 <= inputColumn < column