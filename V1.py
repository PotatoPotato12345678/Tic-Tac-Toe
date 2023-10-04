import cv2
import numpy as np
import random

# Constants
EMPTY = "?"
PLAYER_X = "X"
PLAYER_O = "O"
PLAYERS = [PLAYER_X, PLAYER_O]

class TicTacToe:
    def __init__(self):
        self.board = [EMPTY] * 9
        self.current_player = random.choice(PLAYERS)

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def make_move(self, position):
        if self.board[position] == EMPTY:
            self.board[position] = self.current_player
            self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O
            return True
        else:
            return False

    def check_winner(self):
        for player in PLAYERS:
            for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
                if all(self.board[i] == player for i in combo):
                    return player
        if EMPTY not in self.board:
            return "Tie"
        return None

def main():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")

    while True:
        game.display_board()

        if game.current_player == PLAYER_X:
            position = int(input("Player X, enter your move (1-9): ")) - 1
        else:
            # Implement AI move here (replace this line)
            position = random.choice([i for i, v in enumerate(game.board) if v == EMPTY])

        if 0 <= position < 9:
            if game.make_move(position):
                winner = game.check_winner()
                if winner:
                    game.display_board()
                    if winner == "Tie":
                        print("It's a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    break
        else:
            print("Invalid input. Enter a number between 1 and 9.")

if __name__ == "__main__":
    main()