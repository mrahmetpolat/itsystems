import cv2
import numpy as np

i = 0

cap = cv2.VideoCapture(0)

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
    width = int(cap.get(3))
    height = int(cap.get(3))


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
    lower_red = np.array([0, 193, 135])
    upper_red = np.array([83, 255, 255])
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

  
    #green color range
    lower_green = np.array([36, 0, 0])
    upper_green = np.array([70, 255, 255])
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    greens = cv2.bitwise_and(frame, frame, mask=green_mask)


    #blue color range
    lower_blue = np.array([108, 64, 0])
    upper_blue = np.array([125, 255, 255])
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    blues = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #yellow color range
    lower_yellow = np.array([15, 0, 0,])
    upper_yellow = np.array([36, 255, 255])
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellows = cv2.bitwise_and(frame, frame, mask=yellow_mask) 


    #to show overall colors
    overall_colors = red + blues


    masks = red_mask + blue_mask
    contour  = cv2.findContours(masks, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
 
    if len(contour)>0:
        red_area = max(contour, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(red_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)

    #show newly created hsv_image image    
    #test if the mask is working properly - donot forget to delete
    cv2.imshow('colors', frame)
    cv2.imshow('colorsa', overall_colors)
    cv2.imshow('colorsb', masks)
    i += 1
    #basic escape with q button.

    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()