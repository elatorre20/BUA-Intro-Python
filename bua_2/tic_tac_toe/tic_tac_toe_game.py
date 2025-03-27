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
        
    def __repr__(self):
        #turn the board into a string in a code-readable way
        return(str(self.board))
    
    def make_move(self, player, cell):
        #put a move into the board
        self.board[cell[0]][cell[1]] = player #note that cell is a list because we have an x and y coordinate, so we index into it to get those coordinates
        
    def check_win(self):
        #check whether someone has won the game
        #check horizontals
        for i in range(len(self.board)): #iterate through the rows
            win = True #start by assuming they have won
            for j in range(len(self.board[0])): #iterate through the columns
                if self.board[i][j] != self.currentPlayer: #if we find any empty or opposite player spaces, they have not won
                    win = False
            if win == True: #we went through a whole row and only found this player, so they won
                print("Player " + self.currentPlayer + ' wins!')
                return(True)
        #check verticals
        for i in range(len(self.board[0])): #iterate through the columns
            win = True #start by assuming they have won
            for j in range(len(self.board)): #iterate through the rows
                if self.board[j][i] != self.currentPlayer: #if we find any empty or opposite player spaces, they have not won
                    win = False
            if win == True: #we went through a whole column and only found this player, so they won
                print("Player " + self.currentPlayer + ' wins!')
                return(True)
        #check forward diagonal
        win = True #start by assuming they have won
        for i in range(len(self.board)):#iterate through the rows
            if self.board[i][i] != self.currentPlayer: #if we find any empty or opposite player spaces, they have not won
                win = False
        if win == True: #we went through the whole diagonal and only found this player, so they won
            print("Player " + self.currentPlayer + ' wins!')
            return(True)
        #check backward diagonal
        win = True #start by assuming they have won
        for i in range(len(self.board)): #iterate through the rows
            if self.board[i][(len(self.board)-1)-i] != self.currentPlayer: #if we find any empty or opposite player spaces, they have not won
                win = False
        if win == True: #we went through the whole diagonal and only found this player, so they won
            print("Player " + self.currentPlayer + ' wins!')
            return(True)
        return(False) #if none of the win conditions turned out to be true they player did not win
        
    def next_move(self):
        #ask the player for input for the next move
        print('Player ' + self.currentPlayer + '\'s turn, enter a move:') #ask the player for input
        move = input().split(',') #turn the input from a string to a list
        for i in range(len(move)): #turn the list from strings to ints
            move[i] = int(move[i])
        self.make_move(self.currentPlayer, move) #make the move on the board
        self.check_win() #check whether the player won
        if(self.currentPlayer == 'x'): #swap the player
            self.currentPlayer = 'o'
        else:
            self.currentPlayer = 'x'
        print(self)
        
x = ticTacToeGame()
y = ticTacToeGame()
