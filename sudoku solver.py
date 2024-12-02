import tkinter as tk
from tkinter import messagebox

class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        # Create Sudoku grid
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(
                    self.root, 
                    textvariable=self.grid[row][col], 
                    width=2, 
                    font=("Helvetica", 18), 
                    justify="center"
                )
                entry.grid(row=row, column=col, padx=5, pady=5)
                
                # Add thicker borders for 3x3 subgrids
                if row % 3 == 0 and row != 0:
                    entry.grid(pady=(15, 5))
                if col % 3 == 0 and col != 0:
                    entry.grid(padx=(15, 5))

        # Solve button
        solve_btn = tk.Button(self.root, text="Solve", command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=4, pady=10, sticky="ew")

        # Clear button
        clear_btn = tk.Button(self.root, text="Clear", command=self.clear)
        clear_btn.grid(row=9, column=5, columnspan=4, pady=10, sticky="ew")

    def is_valid(self, grid, row, col, num):
        # Check if number is valid in row, column, and 3x3 subgrid
        if num in grid[row]:
            return False
        if num in [grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def get_grid(self):
        # Convert the input from the tkinter grid to a 2D list of integers
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.grid[row][col].get()
                current_row.append(int(value) if value.isdigit() else 0)
            grid.append(current_row)
        return grid

    def set_grid(self, grid):
        # Update the tkinter grid with the solved Sudoku grid
        for row in range(9):
            for col in range(9):
                self.grid[row][col].set(grid[row][col])

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists!")

    def clear(self):
        # Clear the grid
        for row in range(9):
            for col in range(9):
                self.grid[row][col].set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
