# Othello-Reversi

A two-player strategy game played on a square board with black and white disks.

### Othello Game Logic
The game starts out with two black disks and two white disks placed in the center of the grid, diagonally from each other. </br>

The players take turns placing disks on the board with their assigned color, black or white. During a play, if any of the disks
of the opponent's color that are in a straight line & bounded by the disk just place and another disk of the current player's
color, they are all turned over to the current player's color. </br>

A valid play exists if in that position there exists at least one straight (horizontal, vertical or diagonal) occupied line 
between the placed piece and another piece of the current player's color, with one or more opposing player's pieces between 
them. If the play is valid, the opposing player's pieces lying in a straight line between the new placed piece and the 
anchoring piece are flipped. If one player cannot make a valid move, the play passes back to the other player. </br>

The game concludes when every square on the grid contains a disk, or when neither player is able to make a legal move. The 
winning player is generally the one who has the most discs on the board at the end of the game.

### Othello User Interface
This program asks the user to specify the following options, in the order specified. When the user enters erroneous
input, the program informs the user that the input was invalid and asks the user for the input again. </br>

    1. The number of rows on the board, which must be an even integer between 4 and 16.
    2. The number of columns on the board, which must be an even integer between 4 and 16.
    3. Which of the two players will move first, B [Black] or W [White].
    4. Which of the two colors will be in the top-left position of the four centered discs, two white and two black.

The game is then played by asking the two users to enter their moves directly into the console, continuing until the 
game is complete and at which point the program ends. Until the game is over, the following sequence of events is repeated.</br>

    1. Display the board, the score (how many disks of each color are on the board) and whose turn it is to move.
    2. User is asked to make a move by specifying a cell on the board in which he would like to place a disk.
    3. If the move is invalid, inform the user and ask for another move. Otherwise, if valid, complete the move and change 
       turns.
    4. All the corresponding disks are placed and flipped.
    5. If the game is not over, repeat back to step 1. Otherwise, if the game is over, display the board, the score, and the 
       winner of the game (or no winner at all).
    6. The game ends and the program closes.
    
![program execution](https://i.imgur.com/w9fMCXf.png)
![program execution](https://i.imgur.com/0gOfy0c.png)
 
