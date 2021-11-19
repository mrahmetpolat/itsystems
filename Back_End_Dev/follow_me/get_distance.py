import RPi.GPIO as g
import time

def distance_parser():
    g.setmode(g.BCM)

    trig = 21
    echo = 20


    g.setup(trig, g.OUT)
    g.setup(echo, g.IN)
    g.output(trig, False)


    while True:    
        #Sends a signal by the transmitter
        g.output(trig, True)
        #waits for a 0.00001 seconds for the ultrasound to return
        time.sleep(0.000001)
        #Then, set the Transmitter to False, so no more signals are emitted
        g.output(trig, False)

        try:
            #Below blockes get the time it takes to return
            while g.input (echo) == 0:
                pulse_start = time.time()
            
            
            while g.input(echo) == 1:
                pulse_end = time.time()
                
                
                
            #Time it takes the reflection to return  
            pulse_duration = pulse_end - pulse_start
            #Converting the time to time it takes to the Centimeter
            distance = pulse_duration * 17150
            #Having only 2 digits after the decimal
            distance = round(distance, 2)
               
            
        
            return distance
        except:
            return 9
