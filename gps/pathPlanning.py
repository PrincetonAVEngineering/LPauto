# Princeton Autonomous Vehicle Engieering (PAVE)
# pathPlanning.py
# SPECS:
# GPS: bn-880 gps
# COMPASS: hmc58831 

import CheckPoint
import numpy as np

class PathPlanning:
    # Constructor
    def __init__(self):
        self.checkPoint_list = np.array()
        self.buoy1_checkPoint = None
        self.buoy2_checkPoint = None
    
    # Return string representation
    def __string__(self):
        pass
    
    def add_checkpoint(self, x, y, margin):       
        newPoint = CheckPoint(x, y, margin)
        self.checkPoint_list.add(newPoint)
    
    #TODO: fix this
    def remove_checkpoint(self, label):
        checkpoint = np.where(self.checkPoint_list.index)
        pass

    def create_segment(checkPoint1):
        pass

    # Frame update. 
    def update_bearing(self):
        pass 

    # Get the control command that will be sent to the Pico
    # Incorporate PID control
    def get_command():
        pass

    def visualize_path(self):
        #https://towardsdatascience.com/simple-gps-data-visualization-using-python-and-open-street-maps-50f992e9b676
        # run a web browser