import cv2
import numpy as np


cap = cv2.VideoCapture(0)
i = 0
while True:
    #read the image
    void, frame = cap.read()

    #coverting frames to RGB or HSV
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #define the colour profiles
    lower_red = np.array([125, 0, 0])
    upper_red = np.array([255, 80, 80])

    #Create a mask of your preferred colour
    mask = cv2.inRange (rgb, lower_red, upper_red)
    #looks at the mask and selected area. Then finds the extreme contours
    redcnt = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    #if there is some red in other words, more than 0,
    #this block executes
    if len(redcnt)>0:
        red_area = max(redcnt, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(red_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
        
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    i += 1
    print("Pass", i)

    k = cv2.waitKey(5) 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
