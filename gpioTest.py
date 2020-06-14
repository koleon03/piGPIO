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

def startThread():
    th = Thread(target=blinkLed, daemon=True)
    th.start()



g = GlobalVars()
g.kill = False


while True:
    print("What do you want to do?")
    s = input()
    if(s == 1):
        g.kill = False
        startThread()
    elif(s == 2):
        g.kill = True  
    elif(s == 3):
        exit(0)
    else:
        print("That is not an option!")



