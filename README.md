# Bounding Boxes and Ellipses Detection

This Python script detects bounding boxes and ellipses in an image using OpenCV.
Installation

## Make sure you have Python installed on your system. Additionally, install the following dependencies:

 - OpenCV (pip install opencv-python)
 - NumPy (pip install numpy)

## Usage

- Clone the repository or download the bounding_boxes.py file.
- Place your image in the same directory as the script or provide the correct path to your image.
- Run the script using Python: python bounding_boxes.py.
- The script will display the original image with detected contours, bounding boxes, and ellipses.

## Description

The script performs the following steps:

- Reads an image from the file system.
- Resizes the image.
- Converts the image to grayscale and applies Gaussian blur and bilateral filtering for noise reduction.
- Applies Otsu's thresholding method and Canny edge detection to detect edges.
- Finds contours in the edge-detected image.
- Detects bounding boxes and ellipses around the contours.
- Draws bounding boxes and ellipses on the original image.
- Displays the original image with detected bounding boxes and ellipses.

## Functions

- bounding_boxes(contours, img): Detects bounding boxes and ellipses around contours and displays them on the input image.
- find_points(minEllipse, drawing): Finds points of interest for ellipses (currently hardcoded for demonstration purposes).
- find_ellipse(): Placeholder function for future development.

## Contributors

    Mahesh Joseph Sadashiv

Feel free to contribute to this project by improving the code or adding new features!
