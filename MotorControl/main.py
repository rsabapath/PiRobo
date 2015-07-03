from MasterControl import MasterControl
from time import sleep
masterControl = MasterControl(7,11,13,15)
masterControl.forward()
sleep(5)
masterControl.stop()
