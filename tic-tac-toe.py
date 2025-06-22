
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 36), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        b = self.buttons
        # Check rows, columns, and diagonals
        return any(
            all(b[i][j]["text"] == player for j in range(3)) or
            all(b[j][i]["text"] == player for j in range(3)) for i in range(3)
        ) or all(b[i][i]["text"] == player for i in range(3)) or \
               all(b[i][2 - i]["text"] == player for i in range(3))

    def is_draw(self):
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = "X"

# Create window and run game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()

