from gpiozero import LED
from time import sleep
from multiprocessing import Process

def blinkLed():
    led = LED(2)
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

p1 = Process(target=blinkLed)

while True:
    print("What do you want to do?")
    s = input()
    if(s == "start"):
        p1.start
    elif(s == "stop"):
        p1.kill    
    elif(s == "exit"):
        exit(0)
    else:
        print("That is not an option!")



