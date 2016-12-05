#!/usr/bin/python

import time
import datetime
import sys
import RPi.GPIO as GPIO
from DetectState import DetectState
from config import Config
from action import Action


state = DetectState()
config = Config()
action = Action(config.state_file, config.email, config.url)

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 4

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
f = open(sys.argv[1], 'w')

try:
  print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "  Ready"     

  # Loop until users quits with CTRL-C
  while True :  
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    s, detected = state.input(Current_State)
    f.write("%d:%d:%d\n" % (s, Current_State, detected))
    if detected != 0:
        ts = time.time()
        f.write("Motion detected: " + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + "\n")
        action.do()
    f.flush()
    
    time.sleep(1)      
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
  f.close()
