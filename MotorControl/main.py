from MasterControl import MasterControl
from time import sleep

masterControl = MasterControl(7,11,13,15)
sleep_period = raw_input("How long should I sleep inbetween?")
while True:
  command = raw_input("Please select action: w - forward / s - backward / a - left turn / d - right turn / q - stop / e - exit?")
  if command == "w":
   masterControl.forward()
  elif command == "s":
    masterControl.backward()
  elif command == "a":
    masterControl.turnLeft() 
  elif command == "d":
    masterControl.turnRight()
  elif command == "q":
    masterControl.stop()
  else:
    masterControl.stop()
    break

  #sleep(float(sleep_period))
  #masterControl.stop()
masterControl.exit()
