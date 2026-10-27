# Python code for TIC-TAC-TOE GAME

# Create the board
board = [" "] * 9

# Function to display the board
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Function to check whether a player has won
def check_winner(player):
    winning_positions = [
        (0, 1, 2), # Row 1
        (3, 4, 5), # Row 2
        (6, 7, 8), # Row 3
        (0, 3, 6), # Column 1
        (1, 4, 7), # Column 2
        (2, 5, 8), # Column 3
        (0, 4, 8), # Diagonal
        (2, 4, 6)  # Diagonal
    ]
    
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
            
    return False

# Start the game
current_player = "X"

for turn in range(9):
    display_board()
    print("Player", current_player, "'s turn")
    
    # Get valid position from player
    while True:
        try:
            position = int(input("Enter position (1-9): "))
            
            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
            elif board[position - 1] != " ":
                print("Position already occupied. Choose another.")
            else:
                break
                
        except ValueError:
            print("Please enter a valid number.")
            
    board[position - 1] = current_player
    
   
    if check_winner(current_player):
        display_board()
        print("Player", current_player, "wins!")
        break
        
  
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        
else:
    display_board()
    print("Game Draw!")

"""
OUTPUT:
  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Player X 's turn
Enter position (1-9): 1

X |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Player O 's turn
Enter position (1-9): 3

X |   | O
--+---+--
  |   |  
--+---+--
  |   |  

Player X 's turn
Enter position (1-9): 5

X |   | O
--+---+--
  | X |  
--+---+--
  |   |  

Player O 's turn
Enter position (1-9): 6

X |   | O
--+---+--
  | X | O
--+---+--
  |   |  

Player X 's turn
Enter position (1-9): 9

X |   | O
--+---+--
  | X | O
--+---+--
  |   | X

Player X wins!
"""
