import cv2
import numpy as np
from motor_take_control import move
import motor_take_control as motor
import get_distance

class color:
    
    low = None
    up = None
    
    def red():
        color.low = np.array([100, 0, 0])
        color.up = np.array([255, 80, 80])
    
    def blue():
        print("Code here")
        
        

cap = cv2.VideoCapture(0)
cap.set(3, 260)
cap.set(4, 172)
void, frame = cap.read()
h, w, channels = frame.shape

geo_middle = int(w/2)


while True:
    try:
        void, frame = cap.read()
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        low = np.array([95, 0, 0])
        up = np.array([255, 80, 80])
        
        mask = cv2.inRange(RGB_frame, low, up)
        contours= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        
        
        
        obj_middle = None
        
        for elem in contours:
            (x, y, w, h) = cv2.boundingRect(elem)
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            obj_middle = int((x+x+w)/2)
            
            cv2.line(frame, (obj_middle, 0), (obj_middle, 480), (0,255,0), 2)
            
            cv2.line(frame, (geo_middle, 0), (geo_middle, 480), (0,255,0), 2)
            
            break
        
        try:
            if obj_middle > geo_middle + 40:
                move.right()
                print("Moving right")
            elif obj_middle < geo_middle - 40:
                move.left()
                print("Moving left")
            else:
                print("Middle")
                motor.dc_down()
            
            if get_distance.distance_parser() > 40:
                print("going forward")
                move.fward()
            elif get_distance.distance_parser() < 20:
                print("going back")
                move.bward()
            else:
                print("Stopped")
        
        except:
            print("No object was detected yet")
            motor.dc_down()
        
        cv2.imshow("Object", frame)
        cv2.imshow("mask", mask)
        
        key = cv2.waitKey(1)
    
    except KeyboardInterrupt:
        break

motor.dc_down()
cap.release()
cv2.destroyAllWindows()
