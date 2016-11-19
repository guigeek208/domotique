import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR = 23
RELAI = 14
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(RELAI, GPIO.OUT) 
GPIO.output(RELAI, GPIO.HIGH)
TIMEOUT=200
try:
    print("PIR Module Test")
    print(" (CTRL+C to exit)")
    time.sleep(2)
    print "Ready"
    t = 0
    while True:
        print t
        if GPIO.input(PIR):
            print("Motion detected! ")
            t=0
            GPIO.output(RELAI, GPIO.LOW)
        else:
            if (t>TIMEOUT):
                GPIO.output(RELAI, GPIO.HIGH)
            else:
                t+=1
        time.sleep(1)
except KeyboardInterrupt:
    print("Quitting")
    GPIO.cleanup()
