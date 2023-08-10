import tkinter as tk
from tkinter import messagebox


def is_valid(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_button_callback():
    board = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            value = entry_grid[i][j].get()
            if value.isdigit():
                board[i][j] = int(value)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entry_grid[i][j].delete(0, tk.END)
                entry_grid[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists!")


# Create the GUI window
root = tk.Tk()
root.title("Sudoku Solver")

entry_grid = [[None for _ in range(9)] for _ in range(9)]

# Create entry widgets for the Sudoku grid
for i in range(9):
    for j in range(9):
        entry_grid[i][j] = tk.Entry(root, font=("Helvetica", 20), width=2, justify="center")
        entry_grid[i][j].grid(row=i, column=j, padx=1, pady=1)

solve_button = tk.Button(root, text="Solve", command=solve_button_callback, font=("Helvetica", 16))
solve_button.grid(row=9, columnspan=9, padx=10, pady=10)

root.mainloop()
