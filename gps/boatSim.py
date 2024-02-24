from math import sqrt
 
class Boat:
    def __init__(self, lat, long, heading):
        self.__lat = lat
        self.__long = long
        self.__heading = heading
        self.__vel = 0.01
 
    def get_vector(self):
        return sqrt(self.__lat**2 + self.__long**2)
    
    def get_pos(self):
        return self.__lat, self.__long
    
    def get_heading(self):
        pass

    def set_rudder(self):
        pass
    
    def set_throttle(self):
        pass

    def update(self):
        pass