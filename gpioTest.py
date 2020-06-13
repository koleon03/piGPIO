from gpiozero import LED
from time import sleep
from threading import Thread, Lock

class GlobalVars():
    pass

def blinkLed():
    led = LED(2)
    while True:
        if(g.kill):
            return
        led.on()
        sleep(1)
        led.off()
        sleep(1)

def genNewThread():
    th = Thread(target=blinkLed, daemon=True)
    return th

g = GlobalVars()
g.kill = False


while True:
    print("What do you want to do?")
    s = input()
    if(s == "start"):
        th = genNewThread
        th.start()  
    elif(s == "stop"):
        g.kill = True  
    elif(s == "exit"):
        exit(0)
    else:
        print("That is not an option!")



