class ticTacToeGame():
    
    def __init__(self):
        #constructor
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #set up an empty board
        self.currentPlayer = 'x' #set the player making the first move to x
        
    def __str__(self):
        # a nice representation of the board for printing
        ret = '' #start with an empty string
        ret = ret + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2] #add each line one at a time
        ret = ret + '\n---------\n' #\n is the newline character, analogous to hitting enter in the terminal
        ret = ret + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2]
        ret = ret + '\n---------\n'
        ret = ret + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2]
        return(ret) #return the finished string
    
    def make_move(self, player, cell):
        #put a move into the board
        self.board[cell[0]][cell[1]] = player #note that cell is a list because we have an x and y coordinate, so we index into it to get those coordinates