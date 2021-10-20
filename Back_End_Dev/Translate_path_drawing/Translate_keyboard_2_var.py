from pynput.keyboard import *
import time
import turtle


class keyb():
    i = 0

        
    def press(key):
        print(str(key))
        if str(key) == "Key.up":
            keyb.i += 1
            print(keyb.i)
 

            
        elif str(key) == "Key.down":
            keyb.i += 1

            
        
        elif str(key) == "Key.right":
            keyb.i += 1

            
        
        elif str(key) == "Key.left":
            keyb.i += 1

            
        
        elif str(key) == "Key.esc":
            print(str(key), "test")
            open("user_defined_path.csv", "a").write("\n")
            return False
            
        
    def release(key):
        print(str(key))
        if str(key) == "Key.up":
            print(keyb.i)
            open("user_defined_path.csv", "a").write("f," + str(keyb.i) + ",")
        
        elif str(key) == "Key.down":
            print(keyb.i)
            open("user_defined_path.csv", "a").write("b," + str(keyb.i) + ",")
    
        elif str(key) == "Key.right":
            print(keyb.i)
            open("user_defined_path.csv", "a").write("r," + str(keyb.i) + ",")
            
        elif str(key) == "Key.left":
            print(keyb.i)
            open("user_defined_path.csv", "a").write("l," + str(keyb.i) + ",")
        
        keyb.i = 0

dest = input("PLease name the destination:")
open("user_defined_path.csv", "a").write(str(dest) + ",")


with Listener(on_press = keyb.press, on_release = keyb.release) as L:
    L.join()
