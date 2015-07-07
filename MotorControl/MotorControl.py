import RPi.GPIO as GPIO
from time import sleep

class MotorControl:
  #The following tuples contains GPIO input pins for forward and backward motion (Forward,Backward)
  left = [0,0]
  right = [0,0]
  state = {}
  FORWARD = 0
  BACKWARD = 1

  #L = Left , R = Right
  #F = Forward , B = Backward
  #e.g L_F_GPIO is the Left Forward GPIO pin
  #Sets up the board to activate pins
  def __init__(self,L_F_GPIO,L_B_GPIO,R_F_GPIO,R_B_GPIO):
	self.FORWARD = 0
	self.BACKWARD = 1
    	self.left[self.FORWARD] = L_F_GPIO
    	self.left[self.BACKWARD] = L_B_GPIO
    	self.right[self.FORWARD] = R_F_GPIO
    	self.right[self.BACKWARD] = R_B_GPIO
    	#not sure we need to do it before or after
    	GPIO.setmode(GPIO.BOARD)
    	GPIO.cleanup()
    	GPIO.setmode(GPIO.BOARD)
    	GPIO.setup(self.left[self.FORWARD],GPIO.OUT)
    	GPIO.setup(self.left[self.BACKWARD],GPIO.OUT)
    	GPIO.setup(self.right[self.FORWARD],GPIO.OUT)
    	GPIO.setup(self.right[self.BACKWARD],GPIO.OUT)

  def cleanUp(self):
    	GPIO.output(self.left[self.FORWARD],False)
    	GPIO.output(self.left[self.BACKWARD],False)
    	GPIO.output(self.right[self.FORWARD],False)
    	GPIO.output(self.right[self.BACKWARD],False)
    	GPIO.cleanup()


  def printInputs(self):
  	print "Left Forward:" + self.left[self.FORWARD]
  	print "Left Backward:" + self.left[self.BACKWARD]
  	print "Right Forward:" + self.right[self.FORWARD]
  	print "Right Backward:" + self.right[self.BACKWARD]

  def setLeftForwardHigh(self):
	if((self.state.get(self.left[self.FORWARD],None) != "High") and (self.state.get(self.left[self.BACKWARD],None) != "High")):
		GPIO.output(self.left[self.FORWARD],True)
		self.state[self.left[self.FORWARD]] = "High"
		print "Left Forward Set High"
	elif((self.state.get(self.left[self.BACKWARD],None) == "High")):
		GPIO.output(self.left[self.BACKWARD],False)
		self.state[self.left[self.BACKWARD]] = "Low"
		print "Left Backward Set Low before Forward High"
		GPIO.output(self.left[self.FORWARD],True)
		self.state[self.left[self.FORWARD]] = "High"
		print "Left Forward Set High"
	else:
		print "Skip: Left Forward is already High"

  def setLeftBackwardHigh(self):
	if((self.state.get(self.left[self.BACKWARD],None) != "High") and (self.state.get(self.left[self.FORWARD],None) != "High")):
		GPIO.output(self.left[self.BACKWARD],True)
		self.state[self.left[self.BACKWARD]] = "High"
		print "Left Backward Set High"
	elif((self.state.get(self.left[self.FORWARD],None) == "High")):
		GPIO.output(self.left[self.FORWARD],False)
		self.state[self.left[self.FORWARD]] = "Low"
		print "Left Forward Set Low before Backward High"
		GPIO.output(self.left[self.BACKWARD],True)
		self.state[self.left[self.BACKWARD]] = "High"
		print "Left Backward Set High"
	else:
		print "Skip: Left Backward is already High"

  def setRightForwardHigh(self):
	if((self.state.get(self.right[self.FORWARD],None) != "High") and (self.state.get(self.right[self.BACKWARD],None) != "High")):
		GPIO.output(self.right[self.FORWARD],True)
		self.state[self.right[self.FORWARD]] = "High"
		print "Right Forward Set High"
	elif((self.state.get(self.right[self.BACKWARD],None) == "High")):
		GPIO.output(self.right[self.BACKWARD],False)
		self.state[self.right[self.BACKWARD]] = "Low"
		print "Right Backward Set Low before Forward High"
		GPIO.output(self.right[self.FORWARD],True)
		self.state[self.right[self.FORWARD]] = "High"
		print "Right Forward Set High"
	else:
		print "Skip: Right Forward is already High"

  def setRightBackwardHigh(self):
 	if((self.state.get(self.right[self.BACKWARD],None) != "High") and (self.state.get(self.right[self.FORWARD],None) != "High")):
 		GPIO.output(self.right[self.BACKWARD],True)
 		self.state[self.right[self.BACKWARD]] = "High"
 		print "Right Backward Set High"
 	elif((self.state.get(self.right[self.FORWARD],None) == "High")):
		GPIO.output(self.right[self.FORWARD],False)
 		self.state[self.right[self.FORWARD]] = "Low"
 		print "Right Forward Set Low before Backward High"
 		GPIO.output(self.right[self.BACKWARD],True)
 		self.state[self.right[self.BACKWARD]] = "High"
 		print "Right Backward Set High"
 	else:
 		print "Skip: Right Backward is already High"

  def setLeftForwardLow(self):
        if((self.state.get(self.left[self.FORWARD],None) != "Low")):
        	GPIO.output(self.left[self.FORWARD],False)
     		self.state[self.left[self.FORWARD]] = "Low"
     		print "Left Forward Set Low"
   	else:
     		print "Skip: Left Forward is already Low"

  def setLeftBackwardLow(self):
    	if((self.state.get(self.left[self.BACKWARD],None) != "Low")):
      		GPIO.output(self.left[self.BACKWARD],False)
      		self.state[self.left[self.BACKWARD]] = "Low"
      		print "Left Backward Set Low"
    	else:
      		print "Skip: Left Backward is already Low"

  def setRightForwardLow(self):
    	if((self.state.get(self.right[self.FORWARD],None) != "Low")):
      		GPIO.output(self.right[self.FORWARD],False)
      		self.state[self.right[self.FORWARD]] = "Low"
     	 	print "Right Forward Set Low"
    	else:
      		print "Skip: Right Forward is already Low"

  def setRightBackwardLow(self):
    	if((self.state.get(self.right[self.BACKWARD],None) != "Low")):
      		GPIO.output(self.right[self.BACKWARD],False)
      		self.state[self.right[self.BACKWARD]] = "Low"
      		print "Right Backward Set Low"
    	else:
      		print "Skip: Right Backward is already Low"
   
  			


