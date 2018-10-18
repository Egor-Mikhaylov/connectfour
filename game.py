from board import Board
from player import Player

class Game:
    def __init__(self):
        self.players = []
        self.players.append(Player('x')) #player 1
        self.players.append(Player('o')) #player 2
        self.board = Board(7,6)
        self.turn = 0
        self.game = self.play_game()
        
    def play_game(self):
        print()
        print('Welcome to Connect Four')
        while True:
            try:
                self.board.disp_board()
                self.choice = self.players[self.turn].get_choice()
                self.board.add_piece(self.choice, self.players[self.turn].piece)            
                
                self.board.check_win()
                if self.board.check_win() == True:
                    self.board.disp_board()
                    print('Game Over')
                    break
                if self.board.check_win() == False:
                    self.turn += 1
#                if self.board.is_full() == False:
#                    pass
                    
                if self.board.is_full() == True:
                    self.board.disp_board()
                    print('Game Over')
                    
                    
                self.turn = self.turn % 2
                
            except Exception as e:
                print()
                print('That was not valid! {}'.format(str(e)))
                print()
    
if __name__ == "__main__":
    Game()
    