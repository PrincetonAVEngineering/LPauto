# Princeton Autonomous Vehicle Engieering (PAVE)
# pathPlanning.py
# SPECS:
# GPS: bn-880 gps
# COMPASS: hmc58831

# THINGS TO COMPLETE:
# 1) Test checkpoint creation (without visualization)
# 2) Visualize map + stationary checkpoints 
# 3) Create test script to test visualization 
# 4) Test with segments (ideal path with given checkpoints)
# 5) Test with different current locations (update bearings)
# 6) Test different implementations for curves around buoys

import CheckPoint 
import boatSim
#import gps_module as gps_mod
#import compass_module as compass_mod
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rand
from PIL import Image, ImageDraw

import staticmaps
import mapImport

class PathPlanning:
    # Constructor
    def __init__(self):
        self.__checkPoint_list = []
        self.__buoy_list = []
        self.__boat = None # dummy value
        #self.__boat = gps_mod.BN880.read()
        self.__bearing = None
        self.__fig = None
    
    # Return string representation of boat + checkpoints
    def __str__(self):
        dict = {
            "Current Location": self.get_location(),
            "Bearing": None, 
            "Checkpoints": self.__checkPoint_list,
            "Buoy Locations": self.__buoy_list
        }
        return str(dict) 
    
    def get_location(self):
        return self.__boat

    def add_checkpoint(self, gps_coords, label):       
        # Ensure no duplicate labels
        for checkPoint in self.__checkPoint_list:
            if (checkPoint.get_label() == label):
                return None
        
        # Add in the new checkpoint
        newPoint = CheckPoint.CheckPoint(gps_coords, label)
        self.__checkPoint_list.append(newPoint)
    
    def remove_checkpoint(self, label):
        # Ensure no empty label
        if label is None:
            return None
        for checkPoint in self.__checkPoint_list:
            if (checkPoint.get_label() == label):
                self.__checkPoint_list.remove(checkPoint)
                return
        # Only reaches here if label wasn't found in the list
        return None

    # Create segment with checkPoint1's next node
    def create_path_segments(self):
        enum_checkPoint_list = enumerate(self.__checkPoint_list)
        for count, checkPoint in enum_checkPoint_list:
            if (count == enum_checkPoint_list[:-1][0]):
                checkPoint.set_segNext(enum_checkPoint_list[0][1])
            else:
               checkPoint.set_segNext(next(enum_checkPoint_list)[1])

    # Frame update. 
    def update_bearing(self):
        pass 

    # Get the control command that will be sent to the Pico
    # Incorporate PID control
    def get_command():
        pass

    """def get_test_coords(points, number_of_points):   "Deprecated LOL"
        x_min, x_max, y_min, y_max = points
        for i in range(number_of_points):
            new_point = (rand.randrange(x_min * 1000, x_max * 1000) / 1000, 
                         rand.randrange(x_min * 1000, x_max * 1000) / 1000)"""

    def static_maps(self):
        pass
        
    def get_perp(self, index):
        x1, y1 = self.__checkPoint_list[index - 1].get_coordinates()
        x2, y2 = self.__checkPoint_list[index].get_coordinates()
        slope = (y2 - y1) / (x2 - x1)
        perp = - 1 / slope;        
        return perp
        
    def checkpoint_side(self, coords, index):
        perp = self.get_perp(index)
        c_lat, c_long = self.__checkPoint_list[index].get_coordinates()
        
        # lat = y, long = x <-- for non-sailors 
        # y - c_lat = perp (x - c_long)
        return coords[0] <= perp * coords[1] - perp * c_long + c_lat

    def get_pixel_from_GPS(self, coords):        
        pass

    def initialize_visual(self):
        plt.ion()
        img, self.staticmaps_context = mapImport.import_map(self.__checkPoint_list)
        fig, axis1 = plt.subplots(figsize=(10,10))
        cooler_fig, = plt.plot([], [], '.')
        axis1.imshow(img)

        #plt.show()
        self.__fig = fig
        self.__cool_line = cooler_fig

        # set up pixel transformer
        w = 800; h = 500
        center, zoom = self.staticmaps_context.determine_center_zoom(w, h)
        self.pixel_transformer = staticmaps.Transformer(
            w, h, zoom, center, self.staticmaps_context._tile_provider.tile_size()
        )
        

    def visualize_coords(self, coords):
        # convert lat/long to pixels
        x, y = self.pixel_transformer.ll2pixel(
            staticmaps.create_latlng(coords[0], coords[1])
        )
        print(x,y)

        # add data
        self.__cool_line.set_xdata(np.append(self.__cool_line.get_xdata(), x))
        self.__cool_line.set_ydata(np.append(self.__cool_line.get_ydata(), y))

        # draw
        self.__fig.canvas.draw()
        self.__fig.canvas.flush_events()
        plt.pause(0.05)


        #self.__fig.plot(coords[0], coords[1], '.')
        plt.show()
        return
        
    def visualize_path(self):

        img = mapImport.import_map(self.__checkPoint_list)

        fig, axis1 = plt.subplots(figsize =(10,10))
        axis1.imshow(img)
        plt.show()

        # # Load map image
        # image = Image.open('map.png', 'r') 
        # # tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))
        # test_coords = [(40.34286, -74.65451),
        #                (40.34336, -74.65291),
        #                (40.34434152905456, -74.65285827759239),
        #                (40.34466043795825, -74.65370585561165),
        #                (40.34599329728023, -74.65388824581694)]
        # img_points = []
        # points = (40.3488, -74.6597, 40.3418,-74.6445)
        # for d in self.__checkPoint_list:
        #     # Convert GPS coordinates
        #     x1, y1 = self.scale_to_img(points, d.get_coordinates(), (image.size[0], image.size[1]))
        #     img_points.append((x1, y1))
        # draw = ImageDraw.Draw(image)
        # draw.line(img_points, fill = (255, 0, 0), width = 2)
        # image.save('resultMap.png')
        
        # fig, axis1 = plt.subplots(figsize =(10,10))
        # axis1.imshow(plt.imread('resultMap.png'))
        # axis1.grid()
        # plt.show()
        # run a web browser

    # Helper function taken from 
    # #https://towardsdatascience.com/simple-gps-data-visualization-using-python-and-open-street-maps-50f992e9b676
    def scale_to_img(self, points, lat_lon, h_w):
        """
        Conversion from latitude and longitude to the image pixels.
        It is used for drawing the GPS records on the map image.
        :param lat_lon: GPS record to draw (lat1, lon1).
        :param h_w: Size of the map image (w, h).
        :return: Tuple containing x and y coordinates to draw on map image.
        """
        # https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
        old = (points[2], points[0])
        new = (0, h_w[1])
        y = ((lat_lon[0] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
        old = (points[1], points[3])
        new = (0, h_w[0])
        x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
        # y must be reversed because the orientation of the image in the matplotlib.
        # image - (0, 0) in upper left corner; coordinate system - (0, 0) in lower left corner
        return int(x), h_w[1] - int(y)
    
if __name__ == '__main__':
    path = PathPlanning()
    path.visualize_path()