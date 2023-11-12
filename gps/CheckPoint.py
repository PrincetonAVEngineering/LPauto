# Princeton Autonomous Vehicle Engieering (PAVE)
# CheckPoint.py

import numpy as np
import math

class CheckPoint:
    def __init__(self, x, y, label):
        self.__x = x
        self.__y = y
        self.__label = label
        self.__segNext = None

    def __str__(self):
        coordinates = get_coordinates(self)
        return f"{self.__label} ({coordinates[0]}, {coordinates[1]})"

    #TODO
    def set_segNext(self, nextLabel):
        # Define bearing via compass
        self.__segNext = None #TODO FIX THIS

    def get_segNext(self):
        return self.__segNext

    def get_coordinates(self):
        return np.array(self.__x, self.__y)
    
    # Returns true if the checkpoint has been passed
    # Only works in 1D increasing x #
    def passed_checkpoint(self, x):
        return x >= self.__x

    # Get angle to checkpoint
    def get_bearing(self, x, y):
        if self.passed_checkpoint(x): 
            return None
        dist_x = self.__x - x
        dist_y = self.__y - y
        return math.atan2(dist_y, dist_x) * 180 / math.PI
    
    def get_label(self):
        return self.__label