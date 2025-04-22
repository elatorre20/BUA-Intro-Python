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
        
    def check_win(self):
        for i in self.board:
            if(i[0] != ' ' and i[0] == i[1] and i[1] == i[2]):
                return True
        for j in range(2):
            if(self.board[0][j] != ' ' and self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j]):
                return True
        if(self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]):
            return True
        if(self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]):
            return True
        return False
    
    def check_2(self, player):
        for i in range(len(self.board)):
            count_player = 0
            space_location = [-1,-1]
            
            for j in range(len(self.board[i])):
                if(self.board[i][j] == player):
                    count_player = count_player + 1
                if(self.board[i][j] == ' '):
                    space_location = [i,j]
            if(count_player == 2 and space_location[0] != -1):
                return(space_location)
        return([-1,-1])
    
    def next_move(self):
        if self.currentPlayer == 'x':
            print("next player enter a move: ")
            move = input()
            move = move.split(',')
            for i in range(len(move)):
                    move[i] = int(move[i])
            self.make_move(self.currentPlayer, move)
            self.currentPlayer = 'o'
        else:
            self.make_move_computer();
            self.currentPlayer = 'x'
        
    def make_move_computer(self):
        
            
        
        
game = ticTacToeGame()
game.next_move()