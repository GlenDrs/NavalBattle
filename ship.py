from interact_conditions import InteractConditions
from game import Game
from coordinates_ships import CoordinatesOfShips
import os, time

class Ship:
    def __init__(self, player1, player2, dimention_game):
        self.player1 = player1
        self.player2 = player2
        self.dimention_game = dimention_game
        self.ship_start, self.ship_end  = [], []
        self.coordinates_ships_plr1 = {
            'ship_nb': [],
            'horizontal': [],
            'start_x': [],
            'start_y': [],
            'end_x': [],
            'end_y': []
        }
        self.coordinates_ships_plr2 = {
            'ship_nb': [],
            'horizontal': [],
            'start_x': [],
            'start_y': [],
            'end_x': [],
            'end_y': []
        }

    def creat_ship(self, grid):
        try:
            #building a horizontal ship
            if self.ship_start[0] == self.ship_end[0]:
                for j in range(self.ship_start[1],(self.ship_end[1]+1)):
                    # Avoiding the deployment of the ship on top of an existing ship!
                    if grid[self.ship_start[0]][j] == "\033[1;32;40m[O]":
                        raise ValueError
                    grid[self.ship_start[0]][j] = "\033[1;32;40m[O]"
            #building a vertical ship
            elif self.ship_start[1] == self.ship_end[1]:
                for k in range((self.ship_start[0]),self.ship_end[0]+1):
                    # Avoiding the deployment of the ship on top of an existing ship!
                    if grid[k][self.ship_end[1]] == "\033[1;32;40m[O]":
                        raise ValueError
                    grid[k][self.ship_end[1]] = "\033[1;32;40m[O]"
            print("____________________________________")
            return grid
        except ValueError:
            print(" Error you can't place your ship on top of an existing ship, please try it again! "); time.sleep(1)
            return False


    def clear_screen(self, n, player_name, player_grid):
        if n > 1:
            Game.player_game_board(player_name, player_grid, self.dimention_game)
            clear_screen = input(" Press 'h' to hide your ship field and to continu ")
            while clear_screen != 'h':
                clear_screen = input(" Press 'h' to hide your ship field and to continu ")
            os.system('clear')


    def create_ships(self,):

        for player in [self.player1, self.player2]:
            print("_____________________"); print("Hi "+player.name+" you can start creating your three ships"); print("_____________________");
            for n in range(1,4):
                k = n -1
                while k < n:
                    begining_ship_x =  InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, 1, "of the begining of yur ship "+str(n)+": ")
                    begining_ship_y = InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, 2, "of the begingin of yur ship "+str(n)+": ")
                    ''''
                    this method will check if thee coordinates of the end of the ship will be outside
                    the board game because of the coordinates of the begining. If so it will sugest to the player
                    to choose the again coordinates of the begining of the ship.
                    Example: A game dimention of 8x8, let's say that the player for the third
                    ship of seven unit dimention give the position (C:G), the only two possibilities
                    for the end of the ship will be (C:O) or (J:G), wich are otside
                    the game dimention.
                    '''
                    while self.dimention_game < begining_ship_x +  n * 2 and self.dimention_game < begining_ship_y + n * 2:
                        print("Attention the coordinates of the begingin of the ship might be in order that the end of the ship will not be outside the game gride")
                        begining_ship_x =  InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, 1,"of the begining of yur ship "+str(n)+": ")
                        begining_ship_y = InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, 2,"of the begingin of yur ship "+str(n)+": ")

                    end_ship_x =  InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, 1, "of the end of yur ship "+str(n)+": ")
                    end_ship_x = InteractConditions(player.name, n).verticla_length(begining_ship_x, end_ship_x)
                    end_ship_y = InteractConditions(player.name, n).coordinate_conditions(self.dimention_game,  2, "of the end of yur ship "+str(n)+": ")
                    end_ship_y = InteractConditions(player.name, n).ship_conditions(begining_ship_x, begining_ship_y, end_ship_x, end_ship_y)
                    self.ship_start.append(begining_ship_x); self.ship_start.append(begining_ship_y); self.ship_end.append(end_ship_x); self.ship_end.append(end_ship_y)

                    if self.creat_ship(player.grid) == False:
                        k = n -1; self.ship_start, self.ship_end = [], []
                        continue
                    k = n
                    if player == self.player1:
                        x = CoordinatesOfShips().coordinate_n(self.coordinates_ships_plr1,n,begining_ship_x,begining_ship_y,end_ship_x,end_ship_y)
                    else:
                        y = CoordinatesOfShips().coordinate_n(self.coordinates_ships_plr2,n,begining_ship_x,begining_ship_y, end_ship_x, end_ship_y)
                    self.ship_start, self.ship_end = [], []
            self.clear_screen(n, player.name, player.grid)

        return {self.player1.name: x, self.player2.name: y}
