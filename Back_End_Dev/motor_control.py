#import the gpio and time to initialise later
import RPi.GPIO as gpio
import time

# once the gpio board is finalised this section will be updated
def initialise():
    gpio.setmode(gpio.BOARD)
    gpio.setup(5,gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(9, gpio.OUT)
    gpio.setup(11, gpio.OUT)


# once we know  how many degree the robot turn per second we can pass paramater  to rotate cetrain degree
def forward(time):
    initialise()
    gpio.output(5, False)
    gpio.output(7, True)
    gpio.output(9, True)
    gpio.output(11, False)
    time.sleep(time)
    #cleanup is a critical item to not to miss at the end of every function
    gpio.cleanup()

def reverse(time):
    initialise()
    gpio.output(5, True)
    gpio.output(7, False)
    gpio.output(9, False)
    gpio.output(11, True)
    time.sleep(time)
    gpio.cleanup()

# intension is to  activate 1 motor only to turn..  alternatively the opposite motor can turn reverse drection
def turn_left(time):
    initialise()
    gpio.output(5, True)
    gpio.output(7, False)
    gpio.output(9, False)
    gpio.output(11, False)
    time.sleep(time)
    gpio.cleanup()

def turn_right(time):
    initialise()
    gpio.output(5, False)
    gpio.output(7, False)
    gpio.output(9, True)
    gpio.output(11, False)
    time.sleep(time)
    gpio.cleanup()

#test part. it ic critical if the robot is moving forward and backwards properly.. otherwise swap the code
forward(2)
reverse(2)




