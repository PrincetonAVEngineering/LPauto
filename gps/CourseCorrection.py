# Course Correction

from pathPlanning import PathPlanning
from CheckPoint import CheckPoint 
import testPathPlan
import math
import numpy as np
from boatSim import Vector2, VirtualBoat

# 2D vector with corresponding methods.

# Example usage:
# boat = VirtualBoat(Vector2(0, 0), Vector2(1, 0), Vector2(0, 0))
# boat.set_rudder(math.pi / 6)  # Set rudder angle to 30 degrees
# boat.__throttle__ = 0.8  # Set throttle to 80%
# boat.refresh_logic()  # Update rudder angle
# boat.sim_update()  # Update boat state based on throttle, rudder, etc.    def set_rudder(angle: float):

if __name__ == '__main__':
    plan = PathPlanning()

    # Add checkpoints to plan
    file_path = 'C:\\Users\\meghd\\PAVE\\LPauto\\gps\\points.txt'
    label_num = 0
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            coords = line.split(',')
            coords[0] = float(coords[0])
            coords[1] = float(coords[1])
            label_num += 1
            plan.add_checkpoint(coords, "label" + str(label_num))

    #print("PLAN:" + str(plan))
    plan.initialize_visual()

    # Update simulated position:
    # TODO: convert first line of points.txt to starting vector pos
    virtual_boat = VirtualBoat(Vector2(36.897945, -76.391512), Vector2(1, 0), Vector2(0, 0))
    virtual_boat.set_rudder(math.pi / 4)
    virtual_boat.set_throttle(0.0001)
    for i in range(100):
        virtual_boat.set_throttle(virtual_boat.__throttle__)
        virtual_boat.sim_update()
        plan.visualize_coords((virtual_boat.__position__.x, virtual_boat.__position__.y))
        print(virtual_boat)
