import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Create an empty board
def create_board():
    return [" " for _ in range(9)]

# Display the current board
def display_board(board):
    print("\n")
    for i in range(3):
        row = ""
        for j in range(3):
            idx = i * 3 + j
            mark = board[idx]
            color = Fore.GREEN if mark == "X" else Fore.RED if mark == "O" else Fore.WHITE
            row += color + f"{mark}"
            if j < 2:
                row += Fore.WHITE + " | "
        print(row)
        if i < 2:
            print(Fore.WHITE + "--+---+--")
    print("\n")

# Check if a player has won
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

# Check if it's a draw
def is_draw(board):
    return all(cell != " " for cell in board)

# Player move
def player_move(board, player_name):
    while True:
        try:
            move = int(input(Fore.YELLOW + f"{player_name}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print(Fore.RED + "Invalid number. Choose between 1 and 9.")
            elif board[move] != " ":
                print(Fore.RED + "Spot already taken. Try another.")
            else:
                board[move] = "X"
                break
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

# Computer move
def computer_move(board):
    available = [i for i, cell in enumerate(board) if cell == " "]
    if available:
        move = random.choice(available)
        board[move] = "O"
    print(Fore.CYAN + f"Computer chose position {move + 1}")

# One full game
def play_single_game(player_name):
    board = create_board()
    display_board(board)

    while True:
        player_move(board, player_name)
        display_board(board)
        if check_winner(board, "X"):
            print(Fore.GREEN + f"🎉 {player_name} wins!")
            return
        if is_draw(board):
            print(Fore.MAGENTA + "It's a draw!")
            return

        computer_move(board)
        display_board(board)
        if check_winner(board, "O"):
            print(Fore.RED + "Computer wins!")
            return
        if is_draw(board):
            print(Fore.MAGENTA + "It's a draw!")
            return
        # Game loop with name input
def play_game():
    print(Fore.CYAN + "🎮 Welcome to Tic Tac Toe!")
    player_name = input(Fore.YELLOW + "What's your name? ").strip().title()
    print(Fore.GREEN + f"Hi {player_name}, you are 'X'. Let's play!")

    while True:
        play_single_game(player_name)
        again = input(Fore.YELLOW + "Do you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print(Fore.CYAN + f"Thanks for playing, {player_name}! Goodbye! 👋")
            break

# Run the game
if __name__ == "__main__":
    play_game()

