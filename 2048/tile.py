from utils import COLORS, TEXT_COLORS, FONT

class Tile:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def draw(self, canvas, cell_size):
        x1 = self.col * cell_size
        y1 = self.row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        color = COLORS.get(self.value, "#3c3a32")
        text_color = TEXT_COLORS.get(self.value, "#ffffff")

        canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill=color,
            outline="#bbada0",
            width=2
        )

        if self.value != 0:
            canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                text=str(self.value),
                fill=text_color,
                font=FONT
            )