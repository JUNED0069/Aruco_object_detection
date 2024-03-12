import cv2 as cv
from cv2 import aruco
import os

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Create a directory to store the markers in the same directory as the script
markers_directory = os.path.join(current_directory, "markers")
os.makedirs(markers_directory, exist_ok=True)

# dictionary to specify the type of the marker
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

# MARKER_ID = 0
MARKER_SIZE = 400  # pixels

# generating unique IDs using a for loop
for id in range(20):
    # using the function to draw a marker
    marker_image = aruco.generateImageMarker(marker_dict, id, MARKER_SIZE)

    # Save the marker image in the "markers" directory
    cv.imwrite(os.path.join(markers_directory, f"marker_{id}.png"), marker_image)
