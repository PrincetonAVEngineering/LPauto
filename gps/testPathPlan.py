# Testing file for pathplanning.py

import pathPlanning as path
import CheckPoint as cpt

if __name__ == '__main__':
    test_path = path.PathPlanning()
    lap = 0
    number = 0
    while True:
        new_coords = input('ENTER NEW COORDINATES (LAT, LONG)\n')
        if new_coords is not None:
            lat, long = map(float, new_coords.split(','))

        number += 1
        test_path.add_checkpoint([lat, long], str(lap) + '_' + str(number))


        # points_to_add = [staticmaps.create_latlng(40.34434152905456, -74.65285827759239),
        #         staticmaps.create_latlng(40.34466043795825, -74.65370585561165),
        #         staticmaps.create_latlng(40.34599329728023, -74.65388824581694)]

        # test_coords = [(40.34286, -74.65451),
        #                (40.34336, -74.65291),
        #                (40.34434152905456, -74.65285827759239),
        #                (40.34466043795825, -74.65370585561165),
        #                (40.34599329728023, -74.65388824581694)]
        
        test_path.visualize_path()
        # pass