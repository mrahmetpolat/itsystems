import RPi.GPIO as GPIO
import time
from pynput.keyboard import * 




#motor_A pinout
ena = 12
in1 = 14
in2 = 15

#motor_B pinout
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
    print("DC prepper")


def dc_down():
#Setting GPIO signal to low
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("dc down")



dc_prep()
dc_down()

#Setting PWM perimeter for motor_A
pwm_a = GPIO.PWM(ena, 100)
pwm_a.start(0)

#Setting PWM perimeter for motor_B
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
