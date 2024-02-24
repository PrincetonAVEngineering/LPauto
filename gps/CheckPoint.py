# Princeton Autonomous Vehicle Engieering (PAVE)
# CheckPoint.py

import math
#import gps_module as gps_mod
#import compass_module as compass

class CheckPoint:
    # GPS Coords: [lat, long]
    # Label: Lap#_Checkpoint#
    def __init__(self, gps_coords, label):
        lat, long = gps_coords[0], gps_coords[1]
        self.__lat = lat
        self.__long = long
        self.__label = label
        # Setting to label of next node
        self.__segNext = None 

    def get_coordinates(self):
        return self.__lat, self.__long

    def __str__(self):
        coordinates = self.get_coordinates()
        return f"{self.__label} ({coordinates[0]}, {coordinates[1]})"

    def __repr__(self):
        coordinates = self.get_coordinates()
        return f"{self.__label} ({coordinates[0]}, {coordinates[1]})"

    def get_label(self):
        return self.__label

    def set_segNext(self, nextGPS):
        self.__segNext = self.get_label(nextGPS) 

    def get_segNext(self):
        return self.__segNext

    # Returns true if the checkpoint has been passed
    # Only works in 1D increasing x 
    # Need to make work in both directions
    # DEPRACATE LOL
    #    def passed_checkpoint(self, long):
    #       return long >= self.__long

    # Get angle between boat and checkpoint 
    def get_bearing(self, lat, long):
        if self.passed_checkpoint(long): 
            return None
        dist_lat = self.__lat - lat
        dist_long = self.__long - long
        return math.atan2(dist_long, dist_lat) * 180 / math.PI
    
    def get_label(self):
        return self.__label