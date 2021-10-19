import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    key = cv2.waitKey(1)
    ret, frame  = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(3))

    #capture the image , convert the bgr colours to rgb and store in a rgb variable
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #we want to set upper limit and lower limit for each colour so we can only filter the colours

    #red color range
    lower_red = np.array([0, 150, 50])
    upper_red = np.array([10, 255, 255])q
    red_mask = cv2.inRange(rgb, lower_red, upper_red)
    reds = cv2.bitwise_and(frame, frame, mask=red_mask)

    #green color range
    lower_green = np.array([90, 50, 50])
    upper_green = np.array([130, 255, 255])
    green_mask = cv2.inRange(rgb, lower_green, upper_green)
    greens = cv2.bitwise_and(frame, frame, mask=green_mask)



    #blue color range
    lower_blue = np.array([115, 150, 0])
    upper_blue = np.array([125, 255, 255])
    blue_mask = cv2.inRange(rgb, lower_blue, upper_blue)
    blues = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #show newly created RGB image
    cv2.imshow('frame', blues)
    #test if the mask is working properly - donot forget to delete
    cv2.imshow('mask', blue_mask)

    #basic escape with q button.

    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()