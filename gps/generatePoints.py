# Princeton Autonomous Vehicle Engieering (PAVE): TigerAuto
# February 2024
# generatePoints.py 

# generatePoints provides a user interface for generating a path
# defined by longitudinal/latitudinal coordinates. Final checkpoints
# are stored in a points.txt file. 

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

# Global points variable
lons_list = []
lats_list = []

# Global draw lists
lons_list_draw = []
lats_list_draw = []

# Global variable for map size
scale = 15.e3

# Function to handle mouse clicks
def onclick(event):
    # LEFT OFF HERE
    global toolbar, ax
    state = toolbar.mode
    #state = plt.get_current_fig_manager()
    if event.xdata and event.ydata and state == '':
        lon, lat = bmap(event.xdata, event.ydata, inverse=True)
        print(f"Added to points list: (lon, lat): ({lon:.2f}, {lat:.2f})")
        lons_list.append(lon)
        lats_list.append(lat)

        lons_list_draw.append(event.xdata)
        lats_list_draw.append(event.ydata)
        
    print(lons_list, lats_list, lons_list_draw, lats_list_draw)

    #line, = ax.plot([], [], '-r')
    ## Update line segments
    line.set_xdata(lons_list_draw)
    line.set_ydata(lats_list_draw)

    #line, = ax.plot(lons_list, lats_list)

    # Redraw the plot
    ax.draw_artist(ax.patch)
    ax.draw_artist(line)
    canvas.draw()
    canvas.flush_events()

# Function to close the plot and exit
def close_plot():
    plt.close()
    root.destroy()

# Function to remove the most previous point
def remove_point():
    global lons_list, lats_list
    lons_list.pop()
    lats_list.pop()

# Function to control starting coords window
def submit():
    global entry, start_coords, temp_root
    start_coords = entry.get().split(",")
    temp_root.destroy()

if __name__ == '__main__':
    # Desired File Path
    file_path = "points3.txt"

    # Starting coordinates
    start_coords = None
    
    # Create initial window for starting coordinates
    temp_root = Tk()
    temp_root.title("Starting Coordinates")
    temp_root.geometry('500x250')

    # Place label in temp_root window
    label = Label(temp_root, text="If necessary, enter starting coordinates (lat, lon)")
    label.pack()

    # Entry box for temp_root window
    entry = Entry(temp_root, width=40)
    entry.focus_set()
    entry.pack()

    # Confirmation button for temp_root window
    ttk.Button(temp_root, text="Confirm", width=20, command=submit).pack(pady=20)

    temp_root.mainloop()

    print(start_coords)

    # Create main map tkinter window
    root = Tk()
    root.title("PAVE TigerAuto: Select Coordinates")
    loop_maintain = True

    # Create a matplotlib figure
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    line, = ax.plot([],[],"-r")

    # Create a Basemap
    bmap = Basemap(projection='gnom', ax=ax, 
                lat_0=float(start_coords[0]), lon_0=float(start_coords[1]),
                width=scale, height=scale, resolution="f")
    bmap.drawcoastlines()
    bmap.drawcountries()
    bmap.drawmapboundary(fill_color='aqua')
    bmap.fillcontinents(color='coral', lake_color='aqua')

    # Create the Tkinter Canvas with the MPL figure
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

    # Connect mouse click event to onclick function
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    # Add a button to close the window
    close_button = Button(root, text="Close", command=close_plot, anchor=SW)
    close_button.pack()

    # Button to remove the most previously added point
    remove_button = Button(root, text="Remove", command=remove_point, anchor=S)
    remove_button.pack()

    # Start the tkinter event loop
    root.mainloop()

    try:
        with open(file_path, 'w') as file:
            # Write content to the file
            for lat, lon in zip(lats_list, lons_list):
                file.write(f"{lat:.4f}, {lon:.4f}\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
