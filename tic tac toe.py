#developed by aditya
import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game state variables
player = 'X'
board = ['' for _ in range(9)]

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    if '' not in board:
        return 'Draw'
    return None

# Function to handle button clicks
import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game state variables
player = 'X'
board = ['' for _ in range(9)]

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    if '' not in board:
        return 'Draw'
    return None

# Function to handle button clicks
def button_click(index):
    global player
    if board[index] == '':
        board[index] = player
        buttons[index].config(text=player, state='disabled')
        winner = check_winner()
        if winner:
            if winner == 'Draw':
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        else:
            player = 'O' if player == 'X' else 'X'

# Function to reset the game
def reset_game():
    global board, player
    player = 'X'
    board = ['' for _ in range(9)]
    for button in buttons:
        button.config(text='', state='normal')

# Create buttons for the board
buttons = []
for i in range(9):
    button = tk.Button(root, text='', font=('Arial', 24), width=5, height=2, 
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main event loop
root.mainloop()
