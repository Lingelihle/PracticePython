from player import HumanPlayer, RandomComputerPlayer

#import player from player so the computer can interpret 



class TicTacToe:
    def _init_(self):
        self.board = ['' for _ in range(9)] # we will use single list
        self.current_winner = None # keeping track of winner 

        def print_board(self):
            # getting the rows 
            for row in [self.board[i*3:(i+3)*3] for i in range(3)]:
                print('| '+'| '.join(row) + ' |')

                @staticmethod
                def print_board_nums():
                       number_board :[[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
                       for row in number_board:
                            print('| '+'| '.join(row) + ' |')


                def available_moves(self):
                   # return[]
                 moves = []
                 for (i, spot) in enumerate(self.board):
                      if spot == '':
                           moves.append(i)
                           return moves
                      


                      def empty_squares(self):
                          return '' in self.board
                      
                      def num_empty_squares(self):
                          return self.board.count(' ')
                      
                      def make_move(self, square, letter):
                          if self.board[square] == ' ':
                              self.board[square] = letter
                              if self.winner(square, letter):
                                  self.current_winner = letter
                              return True 
                          return False
                      
                      def winner(self, square, letter):
                          #winner if 3 in any row 
                          row_ind = square // 3
                          row = self.board[row_ind*3 : (row_ind + 1) * 3]
                          if all([spot == letter for spot in row]):
                              return True
                          
                          #column
                          col_ind = square % 3
                          column = [self.board[col_ind+i*3] for i in range(3)]
                          if all([spot == letter for spot in column]):
                              return True
                          
                          #diagonals 
                          if square % 2 == 0:
                              diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal 
                              if all([spot == letter for spot in diagonal1]):
                               return True
                          
                              diagonal2  = [self.board[i] for i in [2, 4, 6]] # right to left  diagonal 
                              if all([spot == letter for spot in diagonal2]):
                                return True
                              
                              # if all fail 
                              return False
                          
                          if __name__== '__main__': 
                              x_player = HumanPlayer('X')
                              o_player = RandomComputerPlayer('O')
                              t = TicTacToe()
                              play(t, x_player, o_player, print_game=True)

                              

                          

                              
                              
                          

                                            
                      
                      def play(game, x_player, o_player, print_game=True):
                          # returns wimer 
                          if print_game:
                              game.print_board_nums()


                              letter = 'X' 
                              # iterate while game has empty sqaures 
                              while game.empty_squares():
                                  
                                  if letter == 'O':
                                      square = o_player.get_move(game)
                                  else:
                                       square = x_player.get_move(game)

                                       # define function to make moves 
                                       if game.make_move(square, letter):
                                           if print_game:
                                               print(letter + f' makes a move to sqaure {square}') 
                                               game.print_board()
                                               print('') # empty line 

                                               if game.current_winner:
                                                   if print_game:
                                                       print(letter + ' wins!')
                                                       return letter


                                               # after move , we alternate letters 
                                               letters = 'O' if letter == 'X' else 'X'

                                               if print_game:
                                                   print('It\s a tie')





