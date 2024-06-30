"""
projekt2.py: Tic-tac-toe

author: Vasyl Burov
email: vasylburov@gmail.com
discord: vasylburov
"""

# Constants
BOARD_SIZE = 3
EMPTY_CELL = " "
HEADER_FOOTER = "+---+---+---+"
LINE_SEPARATOR = "=" * 44
LINE_SEPARATOR_SINGLE = "-" * 44

# Groups all the user-facing messages in a dictionary
msg = {
    "cell_occupied": "Cell already occupied. Try again.",
    "index_error": "Please enter a number between 1 and 9.",
    "its_a_draw": "The game is a draw!",
    "make_move": "Player {player} | Please enter your move number:",
    "player_wins": "Congratulations, the player {player} WON!",
    "uvodni_text": "Welcome to Tic Tac Toe",
    "uvodni_text_rules": """GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""",
    "uvodni_text_lets_start": "Let's start the game",
    "value_error": "Please enter a valid number."
}

def display_board(board: list):
    """
    Displays the current state of the game board.

    Parameters:
    board (list): A 2D list representing the game board.
    """
    for col in range(BOARD_SIZE):
        print(HEADER_FOOTER)
        print("| ", end="")
        print(*board[col], sep=" | ", end=" |\n")
    
    print(HEADER_FOOTER)

def make_move(board: list, player: str):
    """
    Prompts the player to make a move and updates the game board.

    Parameters:
    board (list): A 2D list representing the game board.
    player (str): The current player ('X' or 'O').
    """
    while True:
        try:
            move = int(input(msg["make_move"].format(player=player.lower())))
            rows, columns = divmod(move - 1, BOARD_SIZE)
            if board[rows][columns] == EMPTY_CELL:
                board[rows][columns] = player.upper()
                print(LINE_SEPARATOR)
                break
            else:
                print_message("cell_occupied")
        except (IndexError):
            print_message("index_error")
        except (ValueError):
            print_message("value_error")

def check_win(board: list, player: str):
    """
    Checks if the specified player has won the game.

    Parameters:
    board (list): A 2D list representing the game board.
    player (str): The player to check for a win ('X' or 'O').

    Returns:
    bool: True if the player has won, False otherwise.
    """
    for i in range(BOARD_SIZE):
        if all(board[i][col] == player for col in range(BOARD_SIZE)) or \
           all(board[row][i] == player for row in range(BOARD_SIZE)):
            return True

    if all(board[i][i] == player for i in range(BOARD_SIZE)) or \
       all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False

def print_message(key, **kwargs):
    """
    Prints a formatted message from the msg dictionary.
    """
    print(LINE_SEPARATOR)
    print(msg[key].format(**kwargs))
    print(LINE_SEPARATOR)

def tic_tac_toe():
    """
    Initialises the game board and alternates turns between players until
    there is a win or a draw.
    """
    player = "X"
    board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    print(msg["uvodni_text"])
    print_message("uvodni_text_rules")
    print(msg["uvodni_text_lets_start"])
    print(LINE_SEPARATOR_SINGLE)

    for _ in range(BOARD_SIZE * BOARD_SIZE):
        display_board(board)
        print(LINE_SEPARATOR)
        make_move(board, player)

        if check_win(board, player):
            display_board(board)
            print_message("player_wins", player=player.lower())
            break

        player = "O" if player == "X" else "X"

    else:
        display_board(board)
        print_message("its_a_draw")

# Launch the game
tic_tac_toe()