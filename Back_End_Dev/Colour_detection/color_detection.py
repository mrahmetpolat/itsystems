import cv2
import numpy as np
import imutils
import argparse


i = 0
frame_width= 640
frame_height=480



cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)

colours = []



#trackbar is implemented from https://docs.opencv.org/3.4.15/d9/dc8/tutorial_py_trackbar.html and used for educational purposes only
def nothing (x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing )
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing )
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing )
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing )
cv2.createTrackbar("US", "Tracking", 255, 255, nothing )
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing )


while True:
    key = cv2.waitKey(1)
    ret, frame  = cap.read()

    frame_blur=cv2.GaussianBlur(frame, (7,7),1)
    frame_gray=cv2.cvtColor(frame_blur,cv2.COLOR_BGR2GRAY)


    #capture the image , convert the bgr colours to hsv and store in a hsv_image variable    
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #we want to set upper limit and lower limit for each colour so we can only filter the colours
    #trackbar is implemented from https://docs.opencv.org/3.4.15/d9/dc8/tutorial_py_trackbar.html and used for educational purposes only    
    low_hue = cv2.getTrackbarPos("LH", "Tracking")
    low_saturation = cv2.getTrackbarPos("LS", "Tracking")
    lov_value = cv2.getTrackbarPos("LV", "Tracking")
    upper_hue = cv2.getTrackbarPos("UH", "Tracking")
    upper_saturation = cv2.getTrackbarPos("US", "Tracking")
    upper_value = cv2.getTrackbarPos("UV", "Tracking")
   

    #to display the modified vales on the trackbar
    lower_test = np.array([low_hue , low_saturation , lov_value])
    upper_test = np.array([upper_hue , upper_saturation , upper_value])
    test_mask = cv2.inRange(hsv_image, lower_test, upper_test)
    test = cv2.bitwise_and(frame, frame, mask=test_mask)
   

    #reds
    lower_red = np.array([160, 100, 50])
    upper_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
   

  
    #green color range
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    greens = cv2.bitwise_and(frame, frame, mask=green_mask)


    #blue color range
    lower_blue = np.array([98, 109, 20])
    upper_blue = np.array([112, 255, 255])
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    blues = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #yellow color range
    lower_yellow = np.array([20, 190, 20,])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellows = cv2.bitwise_and(frame, frame, mask=yellow_mask) 


    #to show overall colors
    overall_colors = red + blues + yellows + greens
    masks = red_mask + blue_mask + yellow_mask + green_mask

    red_items  = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont_red  = imutils.grab_contours(red_items)
    
    green_items  = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont_green  = imutils.grab_contours(green_items)

    blue_items  = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont_blue  = imutils.grab_contours(blue_items)

    yellow_items  = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont_yellow  = imutils.grab_contours(yellow_items)

    text_show = ""
    
    red = "red"
    blue = "blue"
    yellow = "yellow"
    green = "green"

    def contour_drawer (contour, text_show):

        for c in contour:
            cont_area = cv2.contourArea(c)
            if cont_area > 500:
                cv2.drawContours(frame, [c], -1, (0,255,0),3)

                # to calculate the center of the contour
                M = cv2.moments(c)
                cx = int(M["m10"]/ M["m00"])
                cy = int(M["m01"] / M["m00"])

                #find the center of hthe obhject
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx,cy),7,(255.255,255),-1)
                cv2.putText(frame, text_show,
                            (cx-20, cy-20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.5,
                            (255,255,255),
                            3)

    contour_drawer (cont_red,red)
    contour_drawer (cont_blue,blue)
    contour_drawer (cont_green,green)
    contour_drawer (cont_yellow,yellow)

  
    #test if the mask is working properly - donot forget to delete
    cv2.imshow('colors', frame)

    #basic escape with q button.

    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()