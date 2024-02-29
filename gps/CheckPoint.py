# Princeton Autonomous Vehicle Engieering (PAVE): TigerAuto
# February 2024
# CheckPoint.py

# CheckPoint API provides functionality for creating paths through
# enumerated checkpoints. Checkpoints are connected via linear segments
# and are labeled according to lap number and checkpoint number 

from typing import List
import math

class CheckPoint:
    # GPS Coordinates: [lat, long]

    # Label: LapX_CheckpointX
    def __init__(self, gps_coords, label):
        # Define latitute and longitude
        self.__lat = gps_coords[0]
        self.__long = gps_coords[1]

        # Define label for the checkpoint
        self.__label = label

        # Setting to Checkpoint of next node
        self.__segNext = None 

    # Getter function for checkpoint coordinates
    def get_coordinates(self) -> tuple:
        return self.__lat, self.__long

    # Getter function for label
    def get_label(self) -> str:
        return self.__label
    
    # Getter function for next segment
    def get_segNext(self) -> dict:
        return self.__segNext
    
    # Setter function for renaming label
    def set_label(self, label: str):
        self.__label = label
        
    # Setter function for next segment
    def set_segNext(self, nextPoint):
        """
        nextPoint: CheckPoint        
        """
        self.__segNext = nextPoint

    # Returns the squared distance (for runtime efficiency)
    # between self and given checkpoint
    def get_coord_dist_sq(self, coords) -> float:
        """
        coords: List[float, float]: coordinates in latitude, longitude order
        """
        return (self.__lat - coords[0]) ** 2 + (self.__long - coords[1]) ** 2

    # Get angle between this checkpoint and parameter checkpoint 
    def get_bearing(self, otherPoint) -> float:
        """
        Args:
            otherPoint: CheckPoint 

        Returns: 
            bearing: float
        """
        # Get coordinates of both checkpoints
        lat, long = otherPoint.get_coordinates()
        this_lat, this_long = self.get_coordinates()

        # Calculate distances
        dist_lat = this_lat - lat
        dist_long = this_long - long

        # Return angle (via arctan)
        return math.atan2(dist_long, dist_lat) * 180 / math.PI
    
    # String representation
    def __str__(self) -> str:
        coordinates = self.get_coordinates()
        return f"{self.__label} ({coordinates[0]}, {coordinates[1]})"

    # Printable representation
    def __repr__(self) -> str:
        coordinates = self.get_coordinates()
        return f"{self.__label} ({coordinates[0]}, {coordinates[1]})"