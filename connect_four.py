import tkinter as tk
from ttkbootstrap import Style
from tkinter import messagebox

ROWS, COLS = 6, 7

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.style = Style(theme="darkly")
        self.current_player = "X"
        self.board = [["" for _ in range(COLS)] for _ in range(ROWS)]
        self.buttons = []

        self.create_ui()

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Create column
        for c in range(COLS):
            btn = tk.Button(frame, text=f"↓", font=("Arial", 14),
                            command=lambda col=c: self.drop_piece(col))
            btn.grid(row=0, column=c, padx=5)
            self.buttons.append(btn)

        # Create board boxes
        self.cells = [[tk.Label(frame, text="", width=4, height=2,
                                font=("Arial", 20), relief="ridge", borderwidth=2)
                       for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c].grid(row=r+1, column=c, padx=2, pady=2)

        # Restart the
        restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 12), command=self.restart_game)
        restart_btn.pack(pady=10)

    def drop_piece(self, col):
        # Find the lowest empty row in the column
        row = -1
        for r in reversed(range(ROWS)):
            if self.board[r][col] == "":
                row = r
                break

        if row == -1:
            messagebox.showwarning("Invalid Move", "This column is full!")
            return

        # Place the piece
        self.board[row][col] = self.current_player
        self.cells[row][col]["text"] = self.current_player
        self.cells[row][col]["fg"] = "red" if self.current_player == "X" else "yellow"

        # Check for win
        if self.check_win(row, col):
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            return

        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, row, col):
        def count_dir(dx, dy):
            count = 0
            r, c = row, col
            while 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == self.current_player:
                count += 1
                r += dy
                c += dx
            return count - 1  # subtract the starting cell

        directions = [(1,0), (0,1), (1,1), (1,-1)]  # horizontal, vertical, diagonal
        for dx, dy in directions:
            total = 1 + count_dir(dx, dy) + count_dir(-dx, -dy)
            if total >= 4:
                return True
        return False

    def restart_game(self):
        self.board = [["" for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c]["text"] = ""
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
