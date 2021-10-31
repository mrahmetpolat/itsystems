# importing  cv2 a library designed to solve computer vision problems. 
# importing NumPy which stands for Numerical Python a library 
# that consist of multidimensional array objects and 
# a batch of routines for processing those arrays.

import cv2
import numpy as np


# Defining a function named any

def any(x):

    # any operation
    pass

# defining a variable named cam to load and read video from
# a system primary camera

cam = cv2.VideoCapture(0)

# trackbar is implemented from
# https://docs.opencv.org/3.4.15/d9/dc8/tutorial_py_trackbar.html 
# and used for educational purposes only.
# Creating trackbars to find lower and upper values of HSV for a specfic colour
# very precise method to get desired result for obtaining
# a perfect mask of an object to detect shape

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, any)
cv2.createTrackbar("L-S", "Trackbars", 66, 255, any)
cv2.createTrackbar("L-V", "Trackbars", 134, 255, any)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, any)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, any)
cv2.createTrackbar("U-V", "Trackbars", 243, 255, any)

font = cv2.FONT_HERSHEY_COMPLEX


while True:


# we create frame to show/ read the video captured from primary camera

    _, frame = cam.read()
    
# defining a variable named hsv to convert frame colors 
# from blue green red to Hue Saturation and value

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Defining 6 variables for upper and lower values of HSV

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    
# using erosing method to remove noise to get a clearer mask.

    mask = cv2.erode(mask, kernel)

# Contours detection
 
    if int(cv2.__version__[0]) > 3:
        

# using a findContours() function to find the contours of the object # Opencv 4.x.x

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:

# using a findContours() function to find the contours of the object for # Opencv 3.x.x
        
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# using for loop

    for cnt in contours:
        area = cv2.contourArea(cnt)

# using cv2.approxPloyDP() function to approximate the shape

        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:

 # using drawContours() function to draw contours
 
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
            elif 10 < len(approx) < 20:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

# Showing the video in a window called "frame"

    cv2.imshow("Frame", frame)

# Showing mask of an object in a window named "mask"

    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:

# breaking the loop

        break
# release the camera
cam.release()

# close all the windows

cv2.destroyAllWindows()
