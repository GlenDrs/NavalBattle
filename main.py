from interact_conditions import InteractConditions
from ship import Ship
from grid import Grid
from game import Game
from player import Player
from fight import Fighting
from coordinates_ships import CoordinatesOfShips

while Game.start_game() == False:
    Game.start_game()


dimention_game = Game.choosing()
Game.show_game_board(dimention_game)

player1 = Player(Game.name_players()[0], Grid(dimention_game).create_grid())
player2 = Player(Game.name_players()[1], Grid(dimention_game).create_grid())

coord = Ship(player1, player2, dimention_game).create_ships()
Fighting(player1, player2, dimention_game, coord).player_hit()
