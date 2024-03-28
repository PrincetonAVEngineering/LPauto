import sys

import matplotlib.pyplot as plt
import staticmaps
import CheckPoint as cp

def import_map(points):
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_ArcGISWorldImagery)

    lat, lng = points[-1].get_coordinates()
    prev_point = staticmaps.create_latlng(lat, lng)

    points_to_add = []

    for pt in points:
        lat, lng = pt.get_coordinates()
        points_to_add.append(staticmaps.create_latlng(lat, lng))
    
    for v in points_to_add:
        context.add_object(staticmaps.Line([prev_point, v], color=staticmaps.BLUE, width=4))
        prev_point = v

    image = context.render_pillow(800, 500)
    return image, context

def create_zoomed_in_view(boat_position):
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_ArcGISWorldImagery)
    print('boat pos', boat_position)
    boat = staticmaps.create_latlng(*boat_position)
    context.set_center(boat)
    context.set_zoom(17)
    image = context.render_pillow(800, 500)
    return image, context

if __name__ == '__main__':
    plt.imshow(image)
    plt.show()