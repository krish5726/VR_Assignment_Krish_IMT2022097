# Panorama Stitching

## Overview
This script stitches multiple images together to create a panorama using OpenCV's `cv2.Stitcher_create()`.

## Dependencies
Ensure you have the following libraries installed:
- OpenCV (`cv2`)
- NumPy

You can install them using:
```sh
pip install opencv-python numpy
```
## How to Run
Place your images in the Assignment1 directory with filenames pano2.jpeg and pano3.jpeg, or modify the script to use your own images.
Run the script using:
```sh
python panorama.py
```

## Methods Used
Image Loading: Reads input images using OpenCV.
Feature Detection (SIFT): Detects keypoints and computes descriptors.
Image Stitching: Uses OpenCV’s Stitcher to merge images into a panorama.
Keypoint Visualization: Draws detected keypoints on the stitched image.

## Results & Observations
If the images have overlapping regions with distinct features, stitching works well.
Poor alignment or lack of common features can lead to errors.
The script saves the output as output.png and displays it.
