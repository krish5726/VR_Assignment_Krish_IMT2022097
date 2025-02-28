import cv2
import numpy as np
import matplotlib.pyplot as plt

'''read images'''
image = cv2.imread('img3.png')
'''convert image to grayscale'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray');
'''use gaussian blur to reduce noise'''
blur = cv2.GaussianBlur(gray, (5,5), 0)
plt.imshow(blur, cmap='gray')
plt.title('1. Smoothed Grayscale Image')
plt.axis('off')  
plt.show()

'''use canny edge detection'''
canny = cv2.Canny(blur, 30, 150)
plt.imshow(canny, cmap='gray')
plt.title('2. Edge-Detected Image')
plt.axis('off')  
plt.show()

'''dilate the canny image'''
dilated = cv2.dilate(canny, (1,1), iterations = 2)
plt.imshow(dilated, cmap='gray')
contours, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.title('3. Image with Contours')
plt.axis('off') 
plt.show()

'''find contours for counting coins'''
(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)

plt.imshow(rgb)


print('Coins in the image: ', len(cnt))
plt.axis('off') 
plt.show()
