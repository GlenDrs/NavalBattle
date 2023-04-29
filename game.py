from string import ascii_uppercase as letters

class Game:

    def first_player(func):
        def inner():
            global name, choice
            print("Hi, welcom to Ship batle game, please choose your name and the dimention of the game!")
            name = input("What is you name player 1: ")
            dimention = input(" Welcome "+name+", you're the first player, the first player have the right to chose the dimention of the game \n what's the dimention of the game that you want to play? \n press 1 if you want a 8 x 8 dimention game \n press 2 if you want a  16 x 16 game\n press 3 if you want a  26 x 26 game\n ")
            choice = int(dimention)
            while choice != 1 and choice != 2 and choice != 3:
                choice = int(input(" Wrong choice. you can only press 1, 2 or 3. \n press 1 if you want a 8 x 8 dimention game \n press 2 if you want a  16 x 16 game \n press 3 if you want a  26 x 26 game\n "))

            func()

        return inner


    @first_player
    def start_game():
        global name2
        print("The second player turn now.")
        print(' ')
        name2 = input("Hello the player 2, what's your name? ")
        accept_dim = input("Welcome "+name2+", if you accept the dimention type 'Yes' ")
        if accept_dim != "Yes":
            print(" "); print("You didn't accept the game dimentios. Let's start over again than"); print(" ")
            return False


    def choosing():
        match choice:
            case 1:
                return 8
            case 2:
                return 16
        return 26


    def name_players():
        return [name, name2]


    def decorator_game_board(func):
        def inner(dim):
            print(" ")
            print(" Hi this will be the Ship Batle game board!")
            print(" ")

            func(dim)

        return inner

    @decorator_game_board
    def show_game_board(dim):
        show_grid = [['\x1b[34m(:)\x1b[0m'] * dim for i in range(dim)]
        a_f = list(letters[:dim])
        print("     " + "   ".join(a_f))
        for index, row in enumerate(show_grid):
            print(" ", (a_f[index]), end = " ")
            print(" ".join(row)); print(" ")


    def player_game_board(name_player, grid, dim):
        print(" "); print(name_player+" this is your origin game board")
        a_f = list(letters[:dim])
        print("     " + "   ".join(a_f))
        for index, row in enumerate(grid):
            print(" ", (a_f[index]), end = " ")
            print(" ".join(row))
        print(" ")
