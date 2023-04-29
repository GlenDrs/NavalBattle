from ship import Ship

class DetectDestrutedShip:
    def __init__(self, playr_name, player_grid):
        self.player_name = playr_name
        self.player_gride = player_grid
    def check(self,coord_h):
        limit = 3
        player_h = coord_h[self.player_name]
        for k in range(0,2):
            if player_h['horizontal'][k] == 1:
                count_horizontal = 0
                for j in range(player_h['start_y'][k],player_h['end_y'][k]+1):
                    # checking the state of the ship.
                    ship_nb = player_h['ship_nb'][k]
                    if self.player_gride[player_h['start_y'][k]][j] != "\033[1;32;40m[O]":
                        count_horizontal = count_horizontal + 1
                if count_horizontal == (k+1)*2+1:
                    print("You have destroyd the ship number "+str(ship_nb)+ " of your enemy!")
                    print("  *[*]*    *[*]*    *[*]*   ")
            else:
                count_vertical = 0
                for l in range((player_h['start_x'][k]),player_h['end_x'][k]+1):
                    # checking the state of the ship.
                    ship_nb = player_h['ship_nb'][k]
                    if self.player_gride[l][player_h['end_y'][k]] != "\033[1;32;40m[O]":
                        count_vertical = count_vertical + 1
                if  count_vertical == (k+1)*2 +1:
                    print("You have destroyd the ship number "+str(ship_nb)+ " of your enemy!")
                    print("  *[*]*    *[*]*    *[*]*   ")


    def signal_destruction(self):
        pass
