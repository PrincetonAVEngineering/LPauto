# Course Correction

from pathPlanning import PathPlanning
from CheckPoint import CheckPoint 
import testPathPlan
import math
import numpy as np

# 2D vector with corresponding methods.
class Vector2:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

    def dot_product(self, other):
        return self.x * other.x + self.y + other.y
    
    def angle_between(self, other):
        return math.acos(self.self.dot_product(self, other) / (self.mag() + other.mag()))

    def mag(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
 
    def dist_to_squared(self, other):
        return (self.x - Vector2.x)**2 + (self.y - Vector2.y)**2

    def dist_to(self, other):
        return np.math.sqrt(self.dist_squared_to(other))
    
    def __mul__(self, scale):
        return Vector2(self.x * scale, self.y * scale)
            
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
        
    __rmul__ = __mul__

    def __str__(self):
        return str(self.x) + ", " + str(self.y)


class VirtualBoat:
    def __init__(self, pos: Vector2, lookVector: Vector2, velocity: Vector2):
        self.__position__ = pos
        self.__direction__ = lookVector
        self.__vel__ = velocity
        self.__rudder_angle__ = 0
        self.__target_rudder__ = 0
        self.__throttle__ = 0  # Number between 0 and 1 representing the corresponding accel
        self.__RUDDER_SPEED__ = 3.1415  # Radians per second
        self.__TICK_TIME__ = 0.05  # Seconds per frame
        self.__MAX_ACCELERATION__ = 100  # At top throttle, what is the acceleration

    def set_rudder(self, angle: float):
        # Limit rudder angle to a reasonable range
        self.__target_rudder__ = max(min(angle, math.pi / 4), -math.pi / 4)        

    def set_throttle(self, t: float):
        if t < 0 or t > 1:
            return False
        self.__throttle__ = t
        return True

    def sim_update(self):
        # Update rudder angle gradually
        rudder_diff = self.__target_rudder__ - self.__rudder_angle__
        rudder_change = math.copysign(self.__RUDDER_SPEED__ * self.__TICK_TIME__, rudder_diff)

        # Apply rudder change
        self.__rudder_angle__ += rudder_change

        # Ensure rudder angle stays within limits
        self.__rudder_angle__ = max(min(self.__rudder_angle__, math.pi / 4), -math.pi / 4)

        # Update boat position, velocity, direction based on throttle, rudder, etc.
        
        self.__direction__ = Vector2(math.cos(self.__rudder_angle__), math.sin(self.__rudder_angle__))

        # Calculate acceleration based on throttle
        acceleration = self.__throttle__ * self.__MAX_ACCELERATION__

        # Update velocity based on acceleration and DIRECTION VECTOR
        acceleration_vector = self.__direction__ * acceleration

        """acceleration_vector = Vector2(acceleration * math.cos(self.__rudder_angle__),
                                      acceleration * math.sin(self.__rudder_angle__))"""
        
        self.__vel__ = self.__vel__ + acceleration_vector * self.__TICK_TIME__

        # Update position based on velocity
        self.__position__ = self.__position__ + self.__vel__ * self.__TICK_TIME__

        # Update direction based on rudder angle
       
    
    #
    def __str__(self): 
        return "Pos: " + str(self.__position__) + " Vel: " + str(self.__vel__)

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
    virtual_boat.set_rudder(0)
    virtual_boat.set_throttle(0.001)
    for i in range(100):
        virtual_boat.sim_update()
        plan.visualize_coords((virtual_boat.__position__.x, virtual_boat.__position__.y))
        print(virtual_boat)
