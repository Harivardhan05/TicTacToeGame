class TicTacToe:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "X"

    def initialize_board(self):
        
        return [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def display_board(self):
        
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def get_player_input(self):
        
        while True:
            try:
                position = int(input("Enter a number between 1 and 9 to place your symbol: "))
                if 1 <= position <= 9:
                    # Map the position to row and column indices
                    row = (position - 1) // 3
                    col = (position - 1) % 3

                    if self.board[row][col] == " ":
                        return row, col
                    else:
                        print("Cell already occupied. Choose an empty cell.")
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def make_move(self, row, col):
        
        self.board[row][col] = self.current_player

    def switch_player(self):
       
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        
        # Check rows, columns, and diagonals for three consecutive symbols
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
                    all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
                all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_draw(self):
        
        return all(cell != " " for row in self.board for cell in row)

    def play_game(self):
        
        while True:
            self.display_board()
            row, col = self.get_player_input()

            if self.board[row][col] == " ":
                self.make_move(row, col)

                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} is the winner!")
                    break

                if self.is_draw():
                    self.display_board()
                    print("The game is a draw!")
                    break

                self.switch_player()
            else:
                print("Invalid move. Please choose an empty cell.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
