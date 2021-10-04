
import RPi.GPIO as gpio
import time

def initialise();
    gpio.setmode(gpio.BOARD)
    gpio.setup(5,gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(9, gpio.OUT)
    gpio.setup(11, gpio.OUT)

def forward(time):
    initialise()
    gpio.output(5, False)
    gpio.output(7, True)
    gpio.output(9, True)
    gpio.output(11, False)
    time.sleep(time)
    gpio.cleanup()

def reverse(time):
    initialise()
    gpio.output(5, True)
    gpio.output(7, False)
    gpio.output(9, False)
    gpio.output(11, True)
    time.sleep(time)
    gpio.cleanup()

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

forward(2)
reverse(2)




