import RPi.GPIO as GPIO

import time
from pynput.keyboard import *
import get_distance

def distance_parser():
    GPIO.setmode(GPIO.BCM)

    trig = 21
    echo = 20


    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    GPIO.output(trig, False)


    while True:    
        #Sends a signal by the transmitter
        GPIO.output(trig, True)
        #waits for a 0.00001 seconds for the ultrasound to return
        time.sleep(0.0000000001)
        #Then, set the Transmitter to False, so no more signals are emitted
        GPIO.output(trig, False)

        try:
            #Below blockes get the time it takes to return
            while GPIO.input (echo) == 0:
                pulse_start = time.time()
            
            
            while GPIO.input(echo) == 1:
                pulse_end = time.time()
                
                
                
            #Time it takes the reflection to return  
            pulse_duration = pulse_end - pulse_start
            #Converting the time to time it takes to the Centimeter
            distance = pulse_duration * 17150
            #Having only 2 digits after the decimal
            distance = round(distance, 2)
               
            
        
            return distance
        except:
            return 11

def main():

    ena = 12
    in1 = 14
    in2 = 15


    enb = 13
    in3 = 17
    in4 = 27
    
    
    def dc_prep():
    #BCM mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    #dc_a
        GPIO.setup(ena,GPIO.OUT)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
    #dc_b
        GPIO.setup(enb,GPIO.OUT)
        GPIO.setup(in3,GPIO.OUT)
        GPIO.setup(in4,GPIO.OUT)


    def dc_down():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)


    dc_prep()
    dc_down()


    pwm_a = GPIO.PWM(ena, 100)
    pwm_a.start(0)

    pwm_b = GPIO.PWM(enb, 100)
    pwm_b.start(0)

    class torque:
        #Motor A configuration for clockwise rotation
        def dc_a_fward():
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            pwm_a.ChangeDutyCycle(100)

        #Motor A configuration for anti-clockwise rotation
        def dc_a_bward():
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            pwm_a.ChangeDutyCycle(100)

        #Motor B configuration for clockwise rotation
        def dc_b_fward():
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            pwm_b.ChangeDutyCycle(100)

        #Motor A configuration for anti-clockwise rotation
        def dc_b_bward():
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            pwm_b.ChangeDutyCycle(100)


    class move:
    #goes forward
        def fward():
            torque.dc_a_fward()
            torque.dc_b_fward()
            
    #goes backward      
        def bward():
            torque.dc_a_bward()
            torque.dc_b_bward()
            
    #turns right        
        def right():
            torque.dc_a_fward()
            torque.dc_b_bward()

    #turns left
        def left():
            torque.dc_a_bward()
            torque.dc_b_fward()
    
    
    def press(key):
        print(str(key))
        if str(key) == "Key.up":
            
            obstacle = distance_parser()
            
            if obstacle > 10:
                print(obstacle)
                move.fward()
            else:
                print(obstacle)
                print("obtacle detected")
                dc_down()
        
            
                
                
        elif str(key) == "Key.down":
            move.bward()
        elif str(key) == "Key.right":
            move.right()
        elif str(key) == "Key.left":
            move.left()
        elif str(key) == "Key.esc":
            return False

    def release(key):
        dc_down()


    with Listener(on_press = press, on_release = release) as L:
        L.join()

main()
