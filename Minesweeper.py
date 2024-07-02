import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root, rows=10, cols=10, mines=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.board = []
        self.create_widgets()

    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                button = tk.Button(self.root, width=2, height=1, command=lambda r=r, c=c: self.reveal_cell(r, c))
                button.bind("<Button-3>", lambda event, r=r, c=c: self.flag_cell(r, c))
                button.grid(row=r, column=c)
                row.append(button)
            self.buttons.append(row)
        
        self.create_board()
        self.place_mines()

    def create_board(self):
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def place_mines(self):
        count = 0
        while count < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] == 0:
                self.board[r][c] = 'M'
                count += 1
                self.update_numbers(r, c)

    def update_numbers(self, row, col):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] != 'M':
                    self.board[r][c] += 1

    def reveal_cell(self, row, col):
        if self.buttons[row][col]['text'] == 'F':
            return
        if self.board[row][col] == 'M':
            self.buttons[row][col].config(text='M', bg='red')
            self.game_over()
        else:
            self.buttons[row][col].config(text=str(self.board[row][col]), state='disabled')
            if self.board[row][col] == 0:
                self.reveal_adjacent_cells(row, col)

    def reveal_adjacent_cells(self, row, col):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < self.rows and 0 <= c < self.cols and self.buttons[r][c]['state'] == 'normal':
                    self.reveal_cell(r, c)

    def flag_cell(self, row, col):
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col].config(text='F', bg='yellow')
        elif self.buttons[row][col]['text'] == 'F':
            self.buttons[row][col].config(text='', bg='SystemButtonFace')

    def game_over(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 'M':
                    self.buttons[r][c].config(text='M', bg='red')
                self.buttons[r][c].config(state='disabled')
        print("Game Over!")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
