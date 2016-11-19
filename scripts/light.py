#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [14]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

try:
  if (len(sys.argv) > 0):
    print sys.argv[1]+"ok"
    if (sys.argv[1] == "on"):
      print "ON"
      GPIO.output(14, GPIO.LOW)
    else:
      print "OFF"
      GPIO.output(14, GPIO.HIGH)
  
  #GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()

