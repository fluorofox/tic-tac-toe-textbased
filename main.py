#Text based tic tac toe - two player game, currently no one player option

import os

RULES = """
RULES 
1. The aim of the game is to get 3 of your symbol in a row on the grid
2. You can line these up vertically, horizontally, or diagonally
3. The game ends once one person reaches this goal
4. If nobody reaches this goal and the grid is filled then the game ends in a draw
"""

STARTING_INSTRUCTIONS = """
        
To fill a square, type the number shown on the grid:

         |     |
      1  |  2  |  3  
    _____|_____|_____
         |     |     
      4  |  5  |  6  
    _____|_____|_____
         |     |     
      7  |  8  |  9  
         |     |     
"""

WINNING_COMBOS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

START_GRID = """
         |     |
      1  |  2  |  3  
    _____|_____|_____
         |     |     
      4  |  5  |  6  
    _____|_____|_____
         |     |     
      7  |  8  |  9  
         |     |     
"""

POS_OPTIONS = ['1','2','3','4','5','6','7','8','9']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_round(player_1, player_2):
    playing = True
    clear()
    player_turn = player_1
    player_1_pos = []
    player_2_pos = []
    while playing:
        clear()
        print(update_grid(player_1_pos, player_2_pos))
        print(f"It is {player_turn}'s turn")
        player_choice = int(input("Choose square: "))
        if player_turn == player_1:
            player_1_pos.append(player_choice)
        else:
            player_2_pos.append(player_choice)
            
        print(update_grid(player_1_pos, player_2_pos))
        if check_win(player_1_pos):
            playing = False
            return player_1
        elif check_win(player_2_pos):
            playing = False
            return player_2
        elif check_draw(player_1_pos, player_2_pos):
            playing = False
            return 'draw'
        else:
            if player_turn == player_1:
                player_turn = player_2
            else:
                player_turn = player_1
 
    
def check_win(player_pos):
    for combo in WINNING_COMBOS:
        if set(combo).issubset(player_pos):
            return True
    return False
 
def check_draw(pos_1, pos_2):
     if len(pos_1) + len(pos_2) == 9:
         return True
 
 
def update_grid(pos_1, pos_2):
    clear()     
    grid = START_GRID
    for char in pos_1:
        char = str(char)
        grid = grid.replace(char, 'x')
    for char in pos_2:
        char = str(char)
        grid = grid.replace(char, 'o')
    for char in POS_OPTIONS:
        grid = grid.replace(char, ' ')
    return grid



program_running = True

while program_running:
    clear()
    print("Welcome to Tic Tac Toe.")
    menu_option = int(input("""
    What would you like to do?
    1. Play a round
    2. See the rules
    3. Quit the game
    """))
    
    if menu_option == 2:
        clear()
        print(RULES)
        input("Press any key to return to the menu")
        
    elif menu_option == 1:
        clear()
        player_1 = input("What is the name of player 1? ")
        player_2 = input("What is the name of player 2? ")
        clear()
        print(f"{player_1} is x, and {player_2} is o.")
        print(STARTING_INSTRUCTIONS)
        input("Press any key to start")
        winner = play_round(player_1, player_2)
        if winner == 'draw':
            print("It's a draw!")
        else:
            print(f"{winner} won the round!")
        input("Press any button to return to menu")
        
    elif menu_option == 3:
        clear()
        program_running = False
        break
    

print("Thanks for playing!")