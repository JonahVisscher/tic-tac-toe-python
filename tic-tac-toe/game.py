from board import Board

class Game:
    player1:str = 'X'
    player2:str = 'O'
    in_progress = False
    current_player = player1

    board: Board

    def __init__(self, board:Board):
        self.board = board

    def switch_player(self, current_player)->None:
        if current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_move(self)->[]:
        column = int(input("Column: "))
        row = int(input("Row: "))
        return row, column

    def start(self)->None:
        self.in_progress = True

        while self.in_progress:
            move = self.get_move()

            if self.board.is_valid_move(move[0], move[1]):
                self.board.update(move[0], move[1], self.current_player)

                if self.board.has_win_condition(self.current_player):
                    self.end(tied=False)

                if self.board.is_full():
                    self.end(tied=True)

                self.switch_player(self.current_player)

            else:
                print("INVALID MODE\n")
                continue

    def end(self, tied:bool)->None:
        if self.in_progress:
            self.in_progress = False

        if tied:
            print("IT'S A TIE!")
        elif self.current_player == self.player1:
            print("PLAYER 1 HAS WON!")
        else:
            print("PLAYER 2 HAS WON!")

        input("PLAY AGAIN? (Y/N)")

    def restart(self)->None:
        pass