import os
from attack import Attack
from string import ascii_uppercase as letters
from interact_conditions import InteractConditions
from game import Game


class Fighting:
    def __init__(self, gamer1, gamer2, dimention):
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.dimention = dimention
        self.missile_coordinate = []
        self.succes = False

    def recreate_grid(self,new_grid):
        mat = []
        while new_grid != []:
            mat.append(new_grid[:self.dimention])
            new_grid = new_grid[self.dimention:]
        a_f = list(letters[:self.dimention])
        print("Your ennemy gamefield!")
        print("     " + "   ".join(a_f))
        index = 0
        for row in mat:
            print(" ", (a_f[index]), end = " ")
            print(" ".join(row))
            index = index+1

    def show_ennemy_grid(self, var1, var2):
        count = 0
        for r in var1:
            for cel in r:
                if cel != "\033[1;32;40m[O]":
                    var2.append(cel)
                elif cel == "\033[1;32;40m[O]":
                    var2.append('\x1b[34m(:)\x1b[0m')
                    count = count + 1 # Will be used to check win

        if count == 0:
            self.succes = True

        self.recreate_grid(var2)

    def show_your_own_grid(self, player, grid):
        print(" ---____----___---")
        print("Hi "+player+" Do you want to see your own game field?")
        print(" write 'yes' if you want to see your game field and 'no' if not ")
        answer = input("yes/no ")
        if answer == "yes":
            a_f = list(letters[:self.dimention])
            print( " YOUR OWN GAMEFIELD")
            print("     " + "   ".join(a_f))
            index = 0
            for row in grid:
                print(" ", (a_f[index]), end = " ")
                print(" ".join(row))
                index = index + 1
            print("    ")


    def check_win(self, player):
        if self.succes == True:
            print(" ")
            print("*********************")
            print(" ")
            print("CONGRATS "+player+" YOU WON!!!")
            print(" ")
            print("*********************")


    def adjust_screen(self, name):
        self.check_win(name)
        clear_screen = input(" Press 'h' to hide your game and to continu ")
        while clear_screen != 'h':
            clear_screen = input(" Press 'h' to hide your game and to continu ")
        os.system('clear')


   
    
    def player_hit(self):
        count = 0
        xy_show, xy = [[],[]], [[],[]]
        while self.succes != True:
            gamers = [self.gamer2, self.gamer1]
            for index, hit in enumerate(gamers):
                if count > 0:
                    self.show_your_own_grid(hit.name,xy[1 - index])
                    self.show_ennemy_grid(xy[index], xy_show[index])
                    xy_show[index] = []
                else:
                    Game.show_game_board(self.dimention)
                for j in range(1,3):
                    ele = InteractConditions(hit.name, j).coordinate_conditions(self.dimention, j,"of your missile attack:")
                    self.missile_coordinate.append(ele)

                xy[index] = Attack(hit.grid, self.missile_coordinate).result_attack()
                self.show_ennemy_grid(xy[index], xy_show[index])
                xy_show[index] = []

                self.adjust_screen(hit.name)
                if self.succes == True:
                    break
                self.missile_coordinate = []
            count = count + 1
