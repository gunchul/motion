import RPi.GPIO as GPIO
import time
import sys

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 4

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

counter = 3590
Current_State  = 0
f = open(sys.argv[1], 'w')

try:
  print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "  Ready"     

  # Loop until users quits with CTRL-C
  while counter > 0 :  
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State != 0:
        f.write("1")
    else:
        f.write("0")
    f.flush()
    # Wait for 10 milliseconds
    time.sleep(1)      
    counter = counter - 1
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
  f.close()
