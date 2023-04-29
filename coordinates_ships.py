

class CoordinatesOfShips:

    def coord_h(self,p1, p2,coord1,coord2):
        {p1:coord1, p2:coord2}


    def coordinate_n(self,ship_h,nb_ship,start_x,start_y,end_x,end_y):
        ship_h['ship_nb'].append(nb_ship)
        if start_x == end_x:
            ship_h[list(ship_h)[1]].append(1)
        else:
            ship_h[list(ship_h)[1]].append(0)
        ship_h[list(ship_h)[2]].append(start_x)
        ship_h[list(ship_h)[3]].append(start_y)
        ship_h[list(ship_h)[4]].append(end_x)
        ship_h[list(ship_h)[5]].append(end_y)
        return ship_h
