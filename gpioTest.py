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

p1 = Process(target=blinkLed, daemon=True)

while True:
    print("What do you want to do?")
    s = input()
    if(s == "start"):
        if(p1.is_alive):
            print("Blink is already running!")
        else:
            p1.start()
    elif(s == "stop"):
        if(p1.is_alive):
            p1.kill()
        else:
            print("Blink isn't running!")
    elif(s == "exit"):
        exit(0)
    else:
        print("That is not an option!")



