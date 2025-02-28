# Coin Detection

## Overview
This script detects and counts coins in an image using OpenCV and image processing techniques. The detected coins are outlined, and the total number of coins is displayed.

## Dependencies
Ensure you have the following libraries installed before running the script:
- OpenCV (`cv2`)
- NumPy
- Matplotlib

You can install them using:
```sh
pip install opencv-python numpy matplotlib
```

## How to Run

Place your image in the existing folder and name it img3.png, or update the script to use your image.
Run the script using:
```sh
python coinDetection.py
```

## Methods Used
Grayscale Conversion: Converts the input image to grayscale for easier processing.
Gaussian Blur: Applies a smoothing filter to reduce noise.
Canny Edge Detection: Detects edges in the image.
Dilation: Expands detected edges to highlight contours.
Contour Detection: Finds and counts individual coins based on their contours.

## Results & Observations
The script effectively detects and counts coins in the image.
If coins are touching or overlapping, the count may be inaccurate.
Adjusting Gaussian blur and Canny edge detection thresholds can improve accuracy.


