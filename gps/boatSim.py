import numpy as np
import math

RUDDER_AREA = 0.3
RUDDER_COEF = 0.4 
BOAT_LENGTH = 6

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
        
    def __truediv__(self, scale):
        return Vector2(self.x / scale, self.y / scale)

    __rmul__ = __mul__

    def __str__(self):
        return str(self.x) + ", " + str(self.y)


class VirtualBoat:
    def __init__(self, pos: Vector2, lookVector: Vector2, velocity: Vector2):
        self.__position__ = pos
        self.__direction__ = lookVector
        self.__direction__ /= self.__direction__.mag()
        self.__vel__ = velocity
        self.__rudder_angle__ = 0
        self.__target_rudder__ = 0
        self.__throttle__ = 0  # Number between 0 and 1 representing the corresponding accel
        self.__RUDDER_SPEED__ = 3.1415  # Radians per second
        self.__TICK_TIME__ = 0.05  # Seconds per frame
        self.__MAX_ACCELERATION__ = 100  # At top throttle, what is the acceleration
        self.__ANGULAR_ACCELERATION__ = 2 * math.pi / (math.pi / 4) # Radians per second at max angle 

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

        rudder_effectiveness = RUDDER_AREA * RUDDER_COEF

        turning_radius = (BOAT_LENGTH ** 2) / (2 * self.__vel__.mag() * rudder_effectiveness * np.sin(np.deg2rad(self.__rudder_angle__)))

        dist_traveled = self.__vel__.mag() * self.__TICK_TIME__

        rotation_angle = dist_traveled / turning_radius

        print(turning_radius)

        new_direction = Vector2(self.__direction__.x * math.cos(rotation_angle) - self.__direction__.y * math.sin(rotation_angle),
                                self.__direction__.x * math.sin(rotation_angle) + self.__direction__.y * math.cos(rotation_angle))

        self.__direction__ = new_direction

        # consider that turning radius coould be infinity

        # Update boat position, velocity, direction based on throttle, rudder, etc.
        #rotation_angle = self.__ANGULAR_ACCELERATION__ * self.__TICK_TIME__ * self.__rudder_angle__

        #perp_accel = self.__vel__ *  math.cos(rotation_angle)

        #Vector2(math.cos(self.__rudder_angle__), math.sin(self.__rudder_angle__))

        # Calculate acceleration based on throttle
        acceleration = self.__throttle__ * self.__MAX_ACCELERATION__

        # Update velocity based on acceleration and DIRECTION VECTOR
        acceleration_vector = self.__direction__ * acceleration

        """acceleration_vector = Vector2(acceleration * math.cos(self.__rudder_angle__),
                                      acceleration * math.sin(self.__rudder_angle__))"""
        
        new_vel = self.__vel__ + (acceleration_vector * self.__TICK_TIME__)

        self.__vel__ = new_vel

        print("\nACCEL ANGLE: " + str(math.atan2(acceleration_vector.y, acceleration_vector.x)) + "\n")

        # Update position based on velocity
        self.__position__ = self.__position__ + (self.__vel__ * self.__TICK_TIME__)

        # Update direction based on rudder angle
    
    def __str__(self): 
        return "Pos: " + str(self.__position__) + " Vel: " + str(self.__vel__) + " Direction Angle: " + str(math.atan2(self.__direction__.y, self.__direction__.x))
