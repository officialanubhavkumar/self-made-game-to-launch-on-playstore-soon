import tkinter as tk
from game import Game

root = tk.Tk()

root.title("2048")
root.geometry("430x620")
root.configure(bg="#bbada0")
root.resizable(False, False)

Game(root)

root.mainloop()