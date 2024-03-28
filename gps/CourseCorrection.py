# Princeton Autonomous Vehicle Engieering (PAVE): TigerAuto
# February 2024
# CourseCorrection.py

# CourseCorrection is a client implementation of the boat simulation
# over the defined path given by a text file (checkpoints on each 
# line)

from pathPlanning import PathPlanning
import math
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

    # Labeling and creating checkpoints
    label_num = 0
    start_coord = None
    with open(file_path) as file:
        lines = file.readlines()

        # Initialize start coordinates
        start_coord = lines[0].split(',')

        # Create checkpoints with labels
        for line in lines:
            coords = line.split(',')
            coords[0] = float(coords[0])
            coords[1] = float(coords[1])
            label_num += 1
            plan.add_checkpoint(coords, "label" + str(label_num))

    # Draw visualization of the plot
    plan.initialize_visual()

    # Update simulated position
    virtual_boat = VirtualBoat(Vector2(float(start_coord[0]), float(start_coord[1])), Vector2(1, 0), Vector2(0, 0))

    #-----------------------------
    virtual_boat.set_rudder(0)
    virtual_boat.set_throttle(1)
    for i in range(100):
        # Update boat movement
        virtual_boat.set_throttle(virtual_boat.__throttle__)
        #virtual_boat.set_rudder(Vector2.angle_between(self, Vector2(plan.)))
        virtual_boat.sim_update()

        print(virtual_boat)
        # Visualize the updated position
        plan.visualize_coords((virtual_boat.__position__.x, virtual_boat.__position__.y))
        
