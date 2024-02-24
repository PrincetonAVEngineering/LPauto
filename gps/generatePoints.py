# Generate points
# Generate a smooth curve of points and connect them into a path
# Dump the points into a file called points.txt

def generate_curve():
    pass

def generate_straight():
    pass

if __name__ == '__main__':
    # File path - change it to your desired file path
    file_path = "points.txt"

    try:
        with open(file_path, 'w') as file:
            # Write content to the file
            file.write(points, '\n')

    except Exception as e:
        print(f"An unexpected error occurred: {e}")