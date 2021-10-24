import cv2
import numpy as np


class color:
    
    low = None
    up = None
    
    def red():
        color.low = np.array([100, 0, 0])
        color.up = np.array([255, 80, 80])
    
    def blue():
        print("Ahmet will write the RGB values here")
        
    def green():
        print("Ahmet will write the RGB values here")
    
    def white():
        print("Ahmet will write the RGB values here")
    
    def black():
        print("Ahmet will write the RGB values here")
    
    def manual():
        print("Ahmet will write the RGB values here")
        


video = cv2.VideoCapture(0) 
def win():
    cv2.imshow("mask", mask)
    cv2.imshow("Webcam", img)


while True:
    success, img = video.read()
    color.red()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(image, color.low, color.up)
    win()
    
    
    cv2.waitKey(1)
    
    print("Up")
