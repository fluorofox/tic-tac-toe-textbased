#Text based tic tac toe - two player game, currently no one player option


RULES = """
RULES 
1. The aim of the game is to get 3 of your symbol in a row on the grid
2. You can line these up vertically, horizontally, or diagonally
3. The game ends once one person reaches this goal
4. If nobody reaches this goal and the grid is filled then the game ends in a draw
"""
playing = True

while playing:
    print("Welcome to Tic Tac Toe.")
    menu_option = int(input("""
    What would you like to do?
    1. Play a round
    2. See the rules
    3. Quit the game
    """))
    
    if menu_option == 2:
        print(RULES)
        input("Press any key to return to the menu")
        
    elif menu_option == 1:
        player_1 = input("What is the name of player 1 ")
        player_2 = input("What is the name of player 2? ")
        print(f"""
        {player_1} is x, and {player_2} is o.
        
        To fill a square, type the number shown on the grid:

             |     |
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     """)
        
        input("Press any key to start")