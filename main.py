#Text based tic tac toe - two player game, currently no one player option

import os #use this to clear screen

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

POS_OPTIONS = [1,2,3,4,5,6,7,8,9]

def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear') #clear screen between changes
    
    
def play_round(player_1, player_2): #player 1 player 2 is names of players
    """Goes through a round of the game and returns who the winner is"""
    playing = True
    clear()
    player_turn = player_1
    player_1_pos = []
    player_2_pos = []
    while playing:
        clear()
        print(update_grid(player_1_pos, player_2_pos)) #print the current grid
        print(f"It is {player_turn}'s turn")
        try:
            player_choice = int(input("Choose square: ")) #turn players choice into integer
        except ValueError:
            input("Invalid input. Press any key to continue") #covers error for user not inputting a number
        else:            
            if player_choice in POS_OPTIONS and player_choice not in player_1_pos and player_choice not in player_2_pos: #must be a valid option, and not an option that has been previously chosen
                if player_turn == player_1:
                    player_1_pos.append(player_choice)
                else:
                    player_2_pos.append(player_choice)
                    
                print(update_grid(player_1_pos, player_2_pos)) #print updated grid
                if check_win(player_1_pos):
                    playing = False
                    return player_1
                elif check_win(player_2_pos):
                    playing = False
                    return player_2
                elif check_draw(player_1_pos, player_2_pos): #check draw after check winner because this checks if game is over after there is no winner which means its a draw
                    playing = False
                    return 'draw'
                else:
                    if player_turn == player_1:
                        player_turn = player_2
                    else:
                        player_turn = player_1
            else:
                input("Invalid input. Press any key to continue") #covers if user enters a number that is not a grid option or has already been used

 
    
def check_win(player_pos):
    """Check the players positions against each winning combo, if player has a winning combo then return true"""
    for combo in WINNING_COMBOS:
        if set(combo).issubset(player_pos):
            return True
    return False
 
 
def check_draw(pos_1, pos_2):
    """If the length of positions for both players equals nine, then all nine squares are filled and the game is over"""
    if len(pos_1) + len(pos_2) == 9:
        return True

 
def update_grid(pos_1, pos_2):
    """Replace character numbers with either x, o, or a blank space depending on the numbers in the player positions"""
    clear()     
    grid = START_GRID
    for char in pos_1: #pos_1 is the positions that player one has chosen
        char = str(char)
        grid = grid.replace(char, 'x')
    for char in pos_2: #pos_1 is the positions that player one has chosen
        char = str(char)
        grid = grid.replace(char, 'o')
    for char in POS_OPTIONS: #pos_options is every pos on the board, so all remaining will be replaced with blank space
        char = str(char)
        grid = grid.replace(char, ' ')
    return grid



program_running = True

while program_running:
    print("Welcome to Tic Tac Toe.")
    try:
        menu_option = int(input("What would you like to do?\n1. Play a round\n2. See the rules\n3. Quit the game\n"))
    except ValueError:
        clear()
        print("Please choose a valid menu option")
    else:        
        if menu_option == 2:
            clear()
            print(RULES)
            input("Press any key to return to the menu")           
        elif menu_option == 1:
            clear()
            game_ready = False
            while not game_ready:
                print("Please enter a unique name for player 1 and player 2")
                player_1 = input("What is the name of player 1? ")
                player_2 = input("What is the name of player 2? ")
                if player_1 == player_2:
                    continue
                elif player_1.isspace() or player_2.isspace():
                        print("Name must contain at least one character")
                        continue
                else:
                    game_ready = True
                    break
            clear()
            print(f"{player_1} is x, and {player_2} is o.")
            print(STARTING_INSTRUCTIONS)
            input("Press any key to start")
            winner = play_round(player_1, player_2)
            if winner == 'draw':
                print("It's a draw!")
                input("Press any button to return to menu")
                clear()
            else:
                print(f"{winner} won the round!")
                input("Press any button to return to menu")
                clear()
        elif menu_option == 3:
            clear()
            program_running = False
            break
        else:
            clear()
            print("Please choose a valid menu option")

    

print("Thanks for playing!")