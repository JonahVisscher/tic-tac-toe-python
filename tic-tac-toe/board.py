class Board:

    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

    def update(self, column:int, row:int, player:str)->None:
        self.board[row][column] = player

    def reset(self)->None:
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ''

    def is_full(self)->bool:
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True

    def is_valid_move(self, column:int, row:int)->bool:
        return self.board[row][column] == ''

    def has_win_condition(self, player:str)->bool:
        # Horizontal checks
        for row in self.board:
            if row[0] == player and row[1] == player and row[2] == player:
                return True

        # Vertical checks
        for column in range(3):
            if (self.board[0][column] == player
                and self.board[1][column] == player
                and self.board[2][column] == player):
                    return True

        # Diagonal checks
        if (self.board[0][0] == player
            and self.board[1][1] == player
            and self.board[2][2] == player):
                return True

        if (self.board[0][2] == player
            and self.board[1][1] == player
            and self.board[2][0] == player):
                return True

        return False