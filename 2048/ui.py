import tkinter as tk
from utils import CELL_SIZE, BOARD_SIZE, BACKGROUND, EMPTY_CELL
from tile import Tile


class UI:
    def __init__(self, root, board):
        self.root = root
        self.board = board

        # ==========================
        # Top Panel
        # ==========================
        self.top_frame = tk.Frame(root, bg=BACKGROUND)
        self.top_frame.pack(fill="x", pady=8)

        self.title_label = tk.Label(
            self.top_frame,
            text="2048",
            font=("Segoe UI", 24, "bold"),
            bg=BACKGROUND,
            fg="white"
        )
        self.title_label.pack(side="left", padx=15)

        self.score_label = tk.Label(
            self.top_frame,
            text="Score: 0\nBest: 0",
            font=("Segoe UI", 12, "bold"),
            bg=BACKGROUND,
            fg="white",
            justify="right"
        )
        self.score_label.pack(side="right", padx=15)

        # ==========================
        # Game Board
        # ==========================
        self.canvas = tk.Canvas(
            root,
            width=CELL_SIZE * BOARD_SIZE,
            height=CELL_SIZE * BOARD_SIZE,
            bg=BACKGROUND,
            highlightthickness=0
        )
        self.canvas.pack(pady=5)

        # ==========================
        # Buttons
        # ==========================
        button_frame = tk.Frame(root, bg=BACKGROUND)
        button_frame.pack(pady=10)

        self.restart_button = tk.Button(
            button_frame,
            text="🔄 Restart",
            font=("Segoe UI", 11, "bold"),
            bg="#8f7a66",
            fg="white",
            width=12,
            relief="flat",
            command=self.restart_game
        )
        self.restart_button.pack(side="left", padx=5)

        self.new_button = tk.Button(
            button_frame,
            text="🆕 New Game",
            font=("Segoe UI", 11, "bold"),
            bg="#f59563",
            fg="white",
            width=12,
            relief="flat",
            command=self.restart_game
        )
        self.new_button.pack(side="left", padx=5)

        # ==========================
        # Status
        # ==========================
        self.status = tk.Label(
            root,
            text="Use Arrow Keys ← ↑ ↓ →",
            font=("Segoe UI", 10),
            bg=BACKGROUND,
            fg="white"
        )
        self.status.pack(pady=5)

        # ==========================
        # Footer
        # ==========================
        self.footer = tk.Label(
            root,
            text="Developed by Anubhav Kumar",
            font=("Segoe UI", 15),
            bg=BACKGROUND,
            fg="white"
        )
        self.footer.pack(pady=5)

    def restart_game(self):
        self.board.reset()
        self.draw()

    def draw(self):
        self.canvas.delete("all")

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=EMPTY_CELL,
                    outline=BACKGROUND,
                    width=4
                )

                value = self.board.grid[r][c]

                if value != 0:
                    tile = Tile(value, r, c)
                    tile.draw(self.canvas, CELL_SIZE)

        self.score_label.config(
            text=f"Score: {self.board.score}\nBest: {self.board.best_score}"
        )

        if self.board.has_won():
            self.status.config(text="🎉 Congratulations! You reached 2048!")

        elif not self.board.has_moves():
            self.status.config(text="💀 Game Over!")

        else:
            self.status.config(text="Use Arrow Keys ← ↑ ↓ →")