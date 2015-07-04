from MasterControl import MasterControl
from time import sleep
masterControl = MasterControl(7,11,13,15)
masterControl.forward()
sleep(5)
masterControl.stop()

masterControl.backward()
sleep(5)
masterControl.stop()

masterControl.turnLeft()
sleep(5)
masterControl.stop()

masterControl.turnRight()
sleep(5)
masterControl.stop()