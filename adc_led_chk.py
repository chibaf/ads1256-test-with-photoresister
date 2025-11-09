#!/usr/bin/python3
#
import RPi.GPIO as GPIO
import time
import sys
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#
GPIO.setup(3, GPIO.OUT) 
GPIO.setup(5, GPIO.OUT)  
GPIO.setup(7, GPIO.OUT)  
GPIO.setup(11, GPIO.OUT)  
GPIO.setup(13, GPIO.OUT)  
GPIO.setup(15, GPIO.OUT)  
GPIO.setup(19, GPIO.OUT)  
GPIO.setup(21, GPIO.OUT)  
#
on=1;off=0
#
while True:
  try:
#
    GPIO.output(int(sys.argv[1]), 1) # 250331
    time.sleep(1)
#
    GPIO.output(int(sys.argv[1]), 0) # 250331
    time.sleep(1)
  except KeyboardInterrupt:
    GPIO.output(3, False) 
    GPIO.output(5, False)  
    GPIO.output(7, False)  
    GPIO.output(11, False)  
    GPIO.output(13, False)  
    GPIO.output(15, False)  
    GPIO.output(19, False)  
    GPIO.output(21, False)  
    exit()
