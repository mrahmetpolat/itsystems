import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(8, g.OUT, initial = g.LOW)
g.setup(10, g.OUT, initial = g.LOW)
g.setup(12, g.OUT, initial = g.LOW)
g.setup(16, g.OUT, initial = g.LOW)
g.setup(3, g.OUT, initial = g.LOW)
g.setup(5, g.OUT, initial = g.LOW)


#Look at the Virtual_LAB folder in the Team for Circuit Diagram


for i in range(5):
    
    g.output(8, g.HIGH)
    g.output(10, g.LOW)
    g.output(12, g.LOW)
    g.output(16, g.LOW)
    g.output(3, g.LOW)
    g.output(5, g.LOW)
    time.sleep(1)
    print("White")
    
    
    g.output(8, g.LOW)
    g.output(10, g.HIGH)
    g.output(12, g.LOW)
    g.output(16, g.LOW)
    g.output(3, g.LOW)
    g.output(5, g.LOW)
    time.sleep(1)
    print("Blue")
    
    
    g.output(8, g.LOW)
    g.output(10, g.LOW)
    g.output(12, g.HIGH)
    g.output(16, g.LOW)
    g.output(3, g.LOW)
    g.output(5, g.LOW)
    time.sleep(1)
    print("Yellow")
    
    
    g.output(8, g.LOW)
    g.output(10, g.LOW)
    g.output(12, g.LOW)
    g.output(16, g.HIGH)
    g.output(3, g.LOW)
    g.output(5, g.LOW)
    time.sleep(1)
    print("Red")
    
    
    g.output(8, g.LOW)
    g.output(10, g.LOW)
    g.output(12, g.LOW)
    g.output(16, g.LOW)
    g.output(3, g.HIGH)
    g.output(5, g.LOW)
    time.sleep(1)
    print("Yellow")
    
    
    g.output(8, g.LOW)
    g.output(10, g.LOW)
    g.output(12, g.LOW)
    g.output(16, g.LOW)
    g.output(3, g.LOW)
    g.output(5, g.HIGH)
    time.sleep(1)
    print("Red")
    
    
g.output(5, g.LOW)


