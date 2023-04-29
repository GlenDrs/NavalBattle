
class InteractConditions:
    def __init__(self, name_player, integer):
        self.name_player = name_player
        self.integer = integer
        self.add_value = integer * 2


    def coordinate_conditions(self, dimention, coord_nb, phrase):
        '''
        The method make sure that the given coordinates of a ship or of
        a missile will not be outside the game border
        '''
        coordinate_choice = ord(input(self.name_player+" Choose the coordinate "+str(coord_nb)+" "+phrase+" ")) - 65

        while coordinate_choice > dimention or coordinate_choice < -1:
            coordinate_choice = ord(input("Carefull the ccordinate must be between A and "+chr(dimention+64)+" choose the coordinate " +str(self.integer)+" "+phrase+" ")) - 65
        return coordinate_choice


    def ship_conditions(self, x1, y1, x2, y2):
        return self.ship_width(x1,y1,x2,y2)



    def ship_width(self, x1, y1, x2, y2):
        '''
        The mathod will garentie that the ship will not be biger or smaller
        than the game conditions.
        Example, if the first ship must be 3 units large and the player will
        make a ship of 2 or 4 units large, the method will stop it and sugest
        to the player the right size
        '''
        if x1 != x2:
            while y1 != y2:
                print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be "+(chr(y1+65)))
                y2= ord(input("Give the second coordinate of your ship: "))-65
            return y2
        while y2 != y1+ self.add_value:
            print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +chr(y1+self.add_value+65)+ ". Because he width of Ship "+str(self.integer)+" must be "+str(self.add_value + 1)+" units ")
            y2 = ord(input("Give the second coordinate of the end of your ship: ")) - 65
        return y2


    def verticla_length(self,x1,x2):
        '''
        The same thing like in the 'ship_width' method, but thise time for
        the vertical case
        '''
        if x2 == x1:
            return x2
        while x2 != x1 + self.add_value:
            print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +chr(x1 + self.add_value + 65)+ ". Because the vertical length of Ship "+str(self.integer)+" must be "+ str(self.add_value + 1)+" units ")
            x2 = ord(input("Give the first coordinate of the end of your ship: ")) - 65

        return x2
