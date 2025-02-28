import numpy as np
import cv2
import glob

image_paths = ['Assignment1/pano2.jpeg', 'Assignment1/pano3.jpeg']
images = [cv2.imread(path) for path in image_paths]
if any(img is None for img in images):
    print("Error: One or more images could not be loaded. Check file paths.")
    exit()

sift = cv2.SIFT_create()
imageStitcher = cv2.Stitcher_create()

error, stitched_img = imageStitcher.stitch(images)

if error == cv2.Stitcher_OK:  # cv2.Stitcher_OK is 0 => success
    gray_stitched = cv2.cvtColor(stitched_img, cv2.COLOR_BGR2GRAY)
    keypoints_stitched, descriptors_stitched = sift.detectAndCompute(gray_stitched, None)
    
    stitched_with_keypoints = cv2.drawKeypoints(stitched_img, keypoints_stitched, None, 
                                                color=(255, 0, 0), 
                                                flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite('output.png', stitched_with_keypoints)
    cv2.imshow("Stitched Image with Keypoints", stitched_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error", error)
