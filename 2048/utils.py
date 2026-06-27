import random

# Board settings
BOARD_SIZE = 4
CELL_SIZE = 100
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE

# Colors
BACKGROUND = "#bbada0"
EMPTY_CELL = "#cdc1b4"

COLORS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}

TEXT_COLORS = {
    2: "#776e65",
    4: "#776e65",
    8: "#ffffff",
    16: "#ffffff",
    32: "#ffffff",
    64: "#ffffff",
    128: "#ffffff",
    256: "#ffffff",
    512: "#ffffff",
    1024: "#ffffff",
    2048: "#ffffff",
}

FONT = ("Segoe UI", 28, "bold")


def random_tile():
    """Return 2 (90%) or 4 (10%)."""
    return 2 if random.random() < 0.9 else 4