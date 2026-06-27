import tkinter as tk
from tkinter import messagebox

from board import Board
from ui import UI


class Game:
    def __init__(self, root):
        self.root = root

        self.board = Board()
        self.ui = UI(root, self.board)

        self.ui.draw()

        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Up>", self.up)
        self.root.bind("<Down>", self.down)

        # Press R to restart
        self.root.bind("r", lambda e: self.restart())
        self.root.bind("R", lambda e: self.restart())

    def restart(self):
        self.board.reset()
        self.ui.draw()

    def update(self):
        self.ui.draw()

        # Update status label if it exists
        if hasattr(self.ui, "status"):
            if self.board.has_won():
                self.ui.status.config(text="🎉 You reached 2048!")
            elif not self.board.has_moves():
                self.ui.status.config(text="💀 Game Over!")
            else:
                self.ui.status.config(text="Use Arrow Keys to Play")

        if self.board.has_won():
            continue_game = messagebox.askyesno(
                "Congratulations!",
                f"🎉 You reached 2048!\n\nScore: {self.board.score}\n\nStart a new game?"
            )

            if continue_game:
                self.board.reset()
                self.ui.draw()

        elif not self.board.has_moves():
            play_again = messagebox.askyesno(
                "Game Over",
                f"Game Over!\n\nScore: {self.board.score}\n\nDo you want to play again?"
            )

            if play_again:
                self.board.reset()
                self.ui.draw()
            else:
                self.root.destroy()

    def left(self, event):
        self.board.move_left()
        self.update()

    def right(self, event):
        self.board.move_right()
        self.update()

    def up(self, event):
        self.board.move_up()
        self.update()

    def down(self, event):
        self.board.move_down()
        self.update()